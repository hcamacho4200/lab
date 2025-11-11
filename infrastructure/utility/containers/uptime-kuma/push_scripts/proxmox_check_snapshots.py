import requests
import os
import sys

from proxmoxer import ProxmoxAPI
from util import kuma_push

def main(proxmox_host: str, kuma_push_url: str):
    """Monitoring the number of snapshots for each VM, and then reporting if there are snaps that are present
    - get the node to scan ie: proxmox-1.home
    - get the vms from the qemu api
    - enumerate through each of the VMIDs looking for a snapshot count > 1
    - push the alert

    :param: proxmox_host: the hostname of the proxmox host
    :param: kuma_push_url: the push url to kuma
    """

    proxmox = ProxmoxAPI(
        proxmox_host,
        user=os.getenv("PROXMOX_USER"),                 # user who owns the token
        token_name=os.getenv("PROXMOX_TOKEN_NAME"),     # token ID (after the '!')
        token_value=os.getenv("PROXMOX_TOKEN"),
        verify_ssl=False
    )

    offending_snaps = []

    for node in proxmox.nodes.get():
        node_name = node['node']
        node_status = node['status']
        if node_status != 'online':
            print(f"Node: {node_name} skipping -> {node_status}")
            continue

        print(f"Node: {node['node']} {node['status']}")
        vms = proxmox.nodes(node['node']).qemu.get()
        for vm in vms:
            snapshot_total = len(proxmox.nodes(node['node']).qemu(vm['vmid']).snapshot.get())
            if snapshot_total > 1:
                offending_snaps.append(f"{node['node']} -> {vm['vmid']}-{vm['name']}: {snapshot_total}")

            print(f"  {node['node']} -> {vm['vmid']} — {vm['name']} ({vm['status']}) {snapshot_total}")

    push_status = "up" if len(offending_snaps) == 0 else "down"
    push_message = "" if len(offending_snaps) == 0 else ",".join(offending_snaps)

    kuma_push(kuma_push_url, push_status, push_message)    


if __name__ == '__main__':
    main(*sys.argv[1:])
