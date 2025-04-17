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
    k8s-master-01 = {  
      vm_id = 1101, vm_name = "k8s-master-01", vm_desc = "K8s Master", 
      vm_target = "proxmox-1", vm_mem = 4096, vm_cores = 2, 
      vm_network_tag0 = 20, vm_ipconfig0 = "ip=${var.network_prefix_0}.101/24,gw=${var.network_prefix_0}.1", 
      vm_network_tag1 = 21, vm_ipconfig1 = "ip=${var.network_prefix_1}.101/24",
      vm_storage0 = "local-zfs", vm_root_size0 = 30,
      vm_storage1 = "local-zfs", vm_root_size1 = 50
    }

    k8s-master-02 = {  
      vm_id = 2102, vm_name = "k8s-master-02", vm_desc = "K8s Master", 
      vm_target = "proxmox-2", vm_mem = 4096, vm_cores = 2, 
      vm_network_tag0 = 20, vm_ipconfig0 = "ip=${var.network_prefix_0}.102/24,gw=${var.network_prefix_0}.1", 
      vm_network_tag1 = 21, vm_ipconfig1 = "ip=${var.network_prefix_1}.102/24",
      vm_storage0 = "local-zfs", vm_root_size0 = 30,
      vm_storage1 = "local-zfs", vm_root_size1 = 50
    }

    k8s-master-03 = {  
      vm_id = 3103, vm_name = "k8s-master-03", vm_desc = "K8s Master", 
      vm_target = "proxmox-3", vm_mem = 4096, vm_cores = 2, 
      vm_network_tag0 = 20, vm_ipconfig0 = "ip=${var.network_prefix_0}.103/24,gw=${var.network_prefix_0}.1", 
      vm_network_tag1 = 21, vm_ipconfig1 = "ip=${var.network_prefix_1}.103/24",
      vm_storage0 = "local-zfs", vm_root_size0 = 30,
      vm_storage1 = "local-zfs", vm_root_size1 = 50
    }

    k8s-worker-01 = {  
      vm_id = 1111, vm_name = "k8s-worker-01", vm_desc = "K8s Worker", 
      vm_target = "proxmox-1", vm_mem = 4096, vm_cores = 2,
      vm_network_tag0 = 20, vm_ipconfig0 = "ip=${var.network_prefix_0}.111/24,gw=${var.network_prefix_0}.1", 
      vm_network_tag1 = 21, vm_ipconfig1 = "ip=${var.network_prefix_1}.111/24",
      vm_storage0 = "local-zfs", vm_root_size0 = 30,
      vm_storage1 = "local-zfs", vm_root_size1 = 50
    }

    k8s-worker-02 = {  
      vm_id = 2112, vm_name = "k8s-worker-02", vm_desc = "K8s Worker", 
      vm_target = "proxmox-2", vm_mem = 4096, vm_cores = 2,
      vm_network_tag0 = 20, vm_ipconfig0 = "ip=${var.network_prefix_0}.112/24,gw=${var.network_prefix_0}.1", 
      vm_network_tag1 = 21, vm_ipconfig1 = "ip=${var.network_prefix_1}.112/24",
      vm_storage0 = "local-zfs", vm_root_size0 = 30,
      vm_storage1 = "local-zfs", vm_root_size1 = 50
    }

    k8s-worker-03 = {  
      vm_id = 3113, vm_name = "k8s-worker-03", vm_desc = "K8s Worker", 
      vm_target = "proxmox-3", vm_mem = 4096, vm_cores = 2,
      vm_network_tag0 = 20, vm_ipconfig0 = "ip=${var.network_prefix_0}.113/24,gw=${var.network_prefix_0}.1", 
      vm_network_tag1 = 21, vm_ipconfig1 = "ip=${var.network_prefix_1}.113/24",
      vm_storage0 = "local-zfs", vm_root_size0 = 30,
      vm_storage1 = "local-zfs", vm_root_size1 = 50
    }

    k8s-worker-04 = {  
      vm_id = 4114, vm_name = "k8s-worker-04", vm_desc = "K8s Worker", 
      vm_target = "proxmox-4", vm_mem = 4096, vm_cores = 2,
      vm_network_tag0 = 20, vm_ipconfig0 = "ip=${var.network_prefix_0}.114/24,gw=${var.network_prefix_0}.1", 
      vm_network_tag1 = 21, vm_ipconfig1 = "ip=${var.network_prefix_1}.114/24",
      vm_storage0 = "local-zfs", vm_root_size0 = 30,
      vm_storage1 = "local-zfs", vm_root_size1 = 50
    }

    k8s-worker-05 = {  
      vm_id = 5115, vm_name = "k8s-worker-05", vm_desc = "K8s Worker", 
      vm_target = "proxmox-5", vm_mem = 4096, vm_cores = 2,
      vm_network_tag0 = 20, vm_ipconfig0 = "ip=${var.network_prefix_0}.115/24,gw=${var.network_prefix_0}.1", 
      vm_network_tag1 = 21, vm_ipconfig1 = "ip=${var.network_prefix_1}.115/24",
      vm_storage0 = "local-zfs", vm_root_size0 = 30,
      vm_storage1 = "local-zfs", vm_root_size1 = 50
    }
  }

  vm_id = each.value.vm_id
  vm_name = each.value.vm_name
  vm_desc = each.value.vm_desc
  vm_target =  each.value.vm_target
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
