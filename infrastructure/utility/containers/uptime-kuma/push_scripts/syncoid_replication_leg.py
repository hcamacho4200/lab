import re
import subprocess
import time


test

def main(destination_host: str = 'proxmox-8'):
    """Main Entry Point
    The main idea here is to see how far replication has lagged to the destination host.  We will consider the following features:
    - if syncoid snaps are present on both side and zfs get written = 0 then replication has no lag.
    - if syncoid snaps are present on both side and zfs get written >0 then lag = current time - last syncoid snap on the source.
    - if syncoid snaps are only present on the source then replication may be in progress or failed.  Lag = current time - last syncoid snap on the source.

    The system performs the following:
    - gather the syncoid cron job configuration to determine sources and destinations of replication

    """

    raw_config = get_syncoid_replication_legs(destination_host)
    replication_legs = parse_syncoid_configuration(raw_config)

    for replication_leg in replication_legs:
        lag = compute_replication_leg(destination_host, replication_leg)
        print("------\n\n")

def compute_replication_leg(destination_host: str, replication_leg: dict):
    """Compute Replication Leg

    :param replication_leg: The replication leg dictionary
    :return: None
    """
    lag = 86400
    source_host = replication_leg['source_host']
    source_dataset = replication_leg['source_dataset']
    dest_dataset = replication_leg['dest_dataset']

    print(f"Source Host: {source_host}")
    print(f"Source Dataset: {source_dataset}")
    print(f"Destination Dataset: {dest_dataset}")

    source_snaps = get_snaps(source_host, source_dataset)
    print(f"Source Snapshots: {source_snaps}")

    dest_snaps = get_snaps(destination_host, dest_dataset)
    print(f"Dest Snapshots: {dest_snaps}")

    source_written = get_written(source_host, source_snaps[0]['name']) if source_snaps else None
    print(f"Source Written Data: {source_written}")

    matching_status = determine_matching_snaps(source_snaps, dest_snaps)

    if matching_status and source_written == '0':
        print("Replication has no lag.")
        lag = 0
    elif matching_status and source_written != '0':
        creation_time = determine_most_recent_snap_time(source_snaps)
        lag = int(time.time()) - creation_time
        print(f"replicating active/hung lag={lag}")
    else:
        print("Othercase")

def determine_most_recent_snap_time(snapshots: list):
    """
    Docstring for determine_most_recent_snap
    
    :param snapshots: Description
    :type snapshots: list
    """

    most_recent_time = 0

    for snap_key, snap_value in snapshots.items():
        snap_creation = int(snap_value['creation'])
        if snap_creation > most_recent_time:
            most_recent_time = snap_creation

    return most_recent_time

def determine_matching_snaps(source_snaps: list, dest_snaps: list):
    """
    Docstring for determine_matching_snaps
    
    :param source_snaps: Description
    :type source_snaps: list
    :param dest_snaps: Description
    :type dest_snaps: list
    """

    matching_status = False
    source_snap_names = strip_dataset_from_snapshots(source_snaps.keys())
    dest_snap_names = strip_dataset_from_snapshots(dest_snaps.keys())

    matching_status = True if source_snap_names == dest_snap_names else False
    # print(f"Matching Snapshots: {matching_status}")

    return matching_status

def strip_dataset_from_snapshots(snapshots: list):
    """
    Docstring for strip_dataset_from_snapshots
    
    :param snapshots: Description
    :type snapshots: dict
    """
    p_compiled = re.compile(r'(.*?)@(.*)')
    return [f'{m.group(2)}' for k in snapshots if (m := p_compiled.match(k))]

def get_written(host: str, dataset: str):
    """Get Written Data on Source

    :param source_host: The source host
    :param source_dataset: The source dataset
    :return: Written data between snapshots
    """
    cmd = f'ssh root@{host} zfs get written -H -o name,value -p {dataset}'
    print(f"Getting written {cmd}")
    response = execute_command(cmd)
    if response.returncode != 0:
        print(f"Failed to retrieve written data from {source_host}:{source_dataset}")
        return None
    
    written_value = response.stdout.strip().split()[1]
    return written_value

def get_snaps(host: str, dataset: str):
    """Get Snapshots from Host

    :param host: The source host
    :param dataset: The source dataset
    :return: List of snapshots
    """
    cmd = f'ssh root@{host} zfs list -t snapshot -o name,creation -s creation -pH {dataset} | grep syncoid'
    response = execute_command(cmd)
    if response.returncode != 0:
        print(f"Failed to retrieve snapshots from {host}:{dataset}")
        return []
    
    p_compiled = re.compile(r'(.*?)\s+(.*)')
    snapshots = {}
    for line in response.stdout.splitlines():
        m = p_compiled.match(line)
        if m:
            snap_name = m.group(1)
            snap_creation = m.group(2)
            snap_key = f"{snap_name}:{snap_creation}"
            snapshots[snap_key] = {'name': snap_name, 'creation': snap_creation}
        else:
            print(f"Failed to parse snapshot line: {line}")
    return snapshots


def parse_syncoid_configuration(raw_config: str):
    """Parse Syncoid Configuration

    :param raw_config: The raw configuration string
    :return: Parsed configuration data
    """

    p_compiled = re.compile(r'/usr\/local\/bin\/syncoid.*@(.*):(.*?)\s(.*?)\s.*')

    replication_legs = []
    lines = raw_config.splitlines()
    for line in lines:
        m = p_compiled.match(line)
        if m:
            replication_legs.append({'source_host': m.group(1), 'source_dataset': m.group(2), 'dest_dataset': m.group(3)})

    return replication_legs

def get_syncoid_replication_legs(destination_host: str):
    """Get Syncoid Replication Legs for a given destination host

    :param destination_host: The destination host to filter replication legs
    :return: List of replication legs
    """
    cmd = f'ssh root@{destination_host} cat /etc/cron.daily/syncoid'
    response = execute_command(cmd)
    if response.returncode != 0:
        print(f"Failed to retrieve cron configuration from {destination_host}")
        return []
    
    replication_configuration = response.stdout
    return replication_configuration


def execute_command(cmd: str):
    """
    Docstring for execute_command
    
    :param cmd: Description
    :type cmd: str
    """
    # print(f"Executing command: {cmd}\n")
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)


if __name__ == "__main__":
    from syncoid_replication_leg import main

    main()