import json
import os
import re
import sys

from enum import Enum
from typing import Optional

import typer

from syncoid_replication_leg import execute_command
from util import kuma_push

app = typer.Typer(help="SPX options data collector")

class HostType(str, Enum):
    """Enum for report types"""
    PVE = "pve"
    PBS = "pbs"

    # /mnt/datastore/backup_pool/vm
    # client.log.blob
def main(
    ctx: typer.Context,
    proxmox_host: str = typer.Argument(..., help="Hostname of the proxmox host to monitor"),
    vmids_json: str = typer.Argument(..., help="JSON array of VMIDs to monitor"),
    kuma_push_url: str = typer.Argument(..., help="Kuma push URL to send the monitoring results to"),
    host_type: Optional[HostType] = typer.Option(HostType.PVE, "--host-type", help="Proxmox PVE is pve, Backup Server is pbs"),
    datastore_path: Optional[str] = typer.Option("/data_root/PROXMOX/dump", "--datastore-path", 
                                                 help="Path to the Proxmox datastore where backups are stored, default is /data_root/PROXMOX/dump"),
    selector: Optional[str] = typer.Option("zst$", "--selector", help="Selects a specific file to verify"),
    lookback: Optional[int] = typer.Option(24, "--lookback", help="Number of hours to look back for backups, default is 24")
) -> None:
    """Monitoring the number of snapshots for each VM, and then reporting if there are snaps that are present
    The point being to catch hanging or stale VM snapshots
    - get the node to scan ie: proxmox-1.home
    - get the vms from the qemu api
    - enumerate through each of the VMIDs looking for a snapshot count > 1
    - push the alert

    :param: proxmox_host: the hostname of the proxmox host
    :param: kuma_push_url: the push url to kuma
    """
    print(f"Running with host {proxmox_host} and vmids {vmids_json} and kuma_push_url {kuma_push_url} and host_type {host_type} and datastore_path {datastore_path}")
    return process(proxmox_host, vmids_json, kuma_push_url, datastore_path, selector, lookback, host_type)

def process(host, vmids_json, kuma_push_url, datastore_path, selector, lookback_hours, host_type):
    non_monitored_vmids = {}
    backup_counts = extract_vmids(vmids_json)
 
    cmd = f'ssh root@{host} \'find {datastore_path} -type f -newermt "{lookback_hours} hours ago"\' | sort | egrep "{selector}"'
    # cmd = f'ssh root@{host} \'find {datastore_path} -type f -newermt "144 hours ago"\' | sort | egrep "{selector}"'
    print(f"Getting written {cmd}")
    response = execute_command(cmd)
    if response.returncode != 0:
        print(f"Failed to retrieve written data from {host}:{datastore_path}")
        return None
    print(response.stdout)
    p_compiled = re.compile(rf'{re.escape(datastore_path)}\/vzdump-qemu-(.*?)-.*') if host_type == HostType.PVE else re.compile(rf'{re.escape(datastore_path)}\/(.*?)\/.*')
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

def extract_vmids(vmids_json):
    backup_counts = {}
    vmids = json.loads(vmids_json)
    for vmid in vmids:
        backup_counts[int(vmid)] = 0
    return backup_counts
 
if __name__ == '__main__':
    typer.run(main)
