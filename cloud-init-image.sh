
export  VMID=10005

qm create $VMID --memory 2048 --net0 virtio,bridge=vmbr0 --scsihw virtio-scsi-pci --name "ubuntu-2410-cloudinit-template"
qm set $VMID --scsi0 local-zfs:0,import-from=/mnt/pve/cephfs/template/iso/oracular-server-cloudimg-amd64.img
qm set $VMID --ide2 local-zfs:cloudinit
qm set $VMID --serial0 socket --vga serial0
qm set $VMID --boot c --bootdisk scsi0
qm template $VMID