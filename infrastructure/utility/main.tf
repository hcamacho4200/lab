# Provider configuration (provider.tf)
terraform {
  required_providers {
    proxmox = {
      source = "telmate/proxmox"
      version = "3.0.1-rc4"
    }
  }
}

provider "proxmox" {
   pm_api_url   = "https://${var.pm_datacenter}:8006/api2/json"
   pm_tls_insecure = true
}

module "vm_module" {
  source      = "../../modules/terraform-cloud-init-vm"

   for_each = {
    util-01 = {  
      vm_id = 1010, vm_name = "utility-01", vm_desc = "Utility VM for Running Various items", 
      vm_target = "proxmox-1", vm_mem = 2048, vm_cores = 2, vm_mac = "02:00:00:00:10:10", 
      vm_network_tag0 = 20, vm_ipconfig0 = "ip=${var.network_prefix_0}.11/24,gw=${var.network_prefix_0}.1", 
      vm_network_tag1 = 21, vm_ipconfig1 = "ip=${var.network_prefix_1}.11/24",
      vm_storage0 = "local-zfs", vm_root_size0 = 30,
      vm_storage1 = "local-zfs", vm_root_size1 = 50
    }

    db-01 = {  
      vm_id = 5010, vm_name = "db-01", vm_desc = "Database VM for Running Various items", 
      vm_target = "proxmox-5", vm_mem = 2048, vm_cores = 2, vm_mac = "02:00:00:00:50:10", 
      vm_network_tag0 = 20, vm_ipconfig0 = "ip=${var.network_prefix_0}.12/24,gw=${var.network_prefix_0}.1", 
      vm_network_tag1 = 21, vm_ipconfig1 = "ip=${var.network_prefix_1}.12/24",
      vm_storage0 = "local-zfs", vm_root_size0 = 30,
      vm_storage1 = "local-zfs", vm_root_size1 = 50
    }
  }

  vm_id = each.value.vm_id
  vm_name = each.value.vm_name
  vm_desc = each.value.vm_desc
  vm_target =  each.value.vm_target
  vm_mac = each.value.vm_mac
  vm_mem = each.value.vm_mem
  vm_cores = each.value.vm_cores
  vm_network_tag0 = each.value.vm_network_tag0
  vm_ipconfig0 = each.value.vm_ipconfig0
  vm_network_tag1 = each.value.vm_network_tag1
  vm_ipconfig1 = each.value.vm_ipconfig1
  vm_template = "ubuntu-2410-cloudinit-template"
  vm_ssh_public_key = var.vm_ssh_public_key
  vm_ciuser = var.vm_ciuser
  vm_cipass = var.vm_cipass
  vm_nameserver = var.nameserver
  vm_storage0 = each.value.vm_storage0
  vm_root_size0 = each.value.vm_root_size0
  vm_storage1 = each.value.vm_storage1
  vm_root_size1 = each.value.vm_root_size1
}
