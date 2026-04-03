import json
import os
import re
import sys

from src.syncoid_replication_leg import execute_command
from src.util import kuma_push

def main(proxmox_host: str, vmids_json: str, kuma_push_url: str):
    """Monitoring the number of snapshots for each VM, and then reporting if there are snaps that are present
    The point being to catch hanging or stale VM snapshots
    - get the node to scan ie: proxmox-1.home
    - get the vms from the qemu api
    - enumerate through each of the VMIDs looking for a snapshot count > 1
    - push the alert

    :param: proxmox_host: the hostname of the proxmox host
    :param: kuma_push_url: the push url to kuma
    """
    backup_counts = {}
    non_monitored_vmids = {}

    vmids = json.loads(vmids_json)
    for vmid in vmids:
        backup_counts[int(vmid)] = 0
 
    cmd = f'ssh root@{proxmox_host} \'find /data_root/PROXMOX/dump -type f -newermt "24 hours ago"\' | sort | egrep "zst$"'
    print(f"Getting written {cmd}")
    response = execute_command(cmd)
    if response.returncode != 0:
        print(f"Failed to retrieve written data from {host}:{dataset}")
        return None
    print(response.stdout)
    p_compiled = re.compile(r'\/data_root\/PROXMOX\/dump\/vzdump-qemu-(.*?)-.*')
    for line in response.stdout.splitlines():
        match = p_compiled.match(line)
        if match:
            vmid = int(match.group(1))
            if vmid in backup_counts:
                backup_counts[vmid] += 1
            else:
                if vmid not in non_monitored_vmids:
                    non_monitored_vmids[vmid] = 1
                else:
                    non_monitored_vmids[vmid] += 1

    push_status = "up"
    missing = []

    for vmid, count in backup_counts.items():
        if count < 1:
            missing.append(vmid)
    
    push_message = f"Missing {missing} backups " if missing else ""
    push_message += f"Non monitored {non_monitored_vmids}" if non_monitored_vmids else ""
    push_status = "down" if missing or non_monitored_vmids else "up"     

    print(backup_counts)
    print(non_monitored_vmids)
    print(push_message)
    print(push_status)
   
    kuma_push(kuma_push_url, push_status, push_message)
    
 
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
