# Provider configuration (provider.tf)
terraform {
  required_providers {
    proxmox = {
      source = "telmate/proxmox"
      version = "3.0.1-rc4"
    }
  }
}

resource "proxmox_vm_qemu" "cloudinit-test" {
    name = var.vm_name
    desc = var.vm_desc
    vmid = var.vm_id
    pool = var.vm_pool
    target_node = var.vm_target
    agent = 1
    cores = var.vm_cores
    sockets = 1
    memory = var.vm_mem
    cpu = "host"
    os_type = "cloud-init"
    # The template name to clone this vm from
    clone = var.vm_template
    vcpus = 0
    scsihw = "virtio-scsi-pci"

    # Setup the disk
    disks {
        ide {
            ide2 {
                cloudinit {
                    storage = var.vm_storage0
                }
            }
        }
        scsi {
            scsi0 {
                disk {
                    size            = var.vm_root_size0
                    cache           = "writeback"
                    storage         = var.vm_storage0
                    replicate       = true
                }
            }
            dynamic "scsi1" {
                for_each = var.vm_storage1 != null ?[1] : []
                content {
                    disk {
                        size            = var.vm_root_size1
                        cache           = "writeback"
                        storage         = var.vm_storage1
                        replicate       = true
                    }
                }
            }
        }
    }

    # Setup the network interface and assign a vlan tag:
    network {
        model = "virtio"
        bridge = "vmbr0"
        tag = var.vm_network_tag0
        macaddr = var.vm_mac
    }

    network {
        model = "virtio"
        bridge = "vmbr1"
        tag = var.vm_network_tag1
    }

    # Setup the ip address using cloud-init.
    boot = "order=scsi0"
    ipconfig0 = var.vm_ipconfig0
    ipconfig1 = var.vm_ipconfig1
    nameserver = var.vm_nameserver
    ciuser     = var.vm_ciuser
    cipassword = var.vm_cipass
    sshkeys    = var.vm_ssh_public_key

    serial {
      id   = 0
      type = "socket"
    }
}