variable "vm_name" {
  description = "Name of the virtual machine"
  type        = string
}

variable "vm_desc" {
  description = "Description of the virtual machine"
  type        = string
}

variable "vm_target" {
  description = "Target node for the virtual machine"
  type        = string
}

variable "vm_id" {
  description = "ID of the virtual machine"
  type        = number
  default = null
}

variable "vm_count" {
  description = "Number of virtual machines to create"
  type        = number
  default     = 1
}

variable "vm_mem" {
  description = "Memory for the virtual machine"
  type        = number
  default     = 2048
}

variable "vm_cores" {
  description = "Number of cores for the virtual machine"
  type        = number
  default     = 2
}
variable "vm_template" {
  description = "Template for the virtual machine"
  type        = string
}

variable "vm_mac" {
  description = "Number of cores for the virtual machine"
  type        = string
  default = null
}

variable "vm_network_tag0" {
  description = "Network tag for the virtual machine"
  type        = number
  default = null
}

variable "vm_network_tag1" {
  description = "Network tag for the virtual machine"
  type        = number
  default = null
}

variable "vm_ipconfig0" {
  description = "IPconfig string ie: ip=237.84.2.178/24,gw=237.84.2.178"
  type        = string
  default = "ip=dhcp"
}

variable "vm_ipconfig1" {
  description = "IPconfig string ie: ip=237.84.2.178/24,gw=237.84.2.178"
  type        = string
  default = "ip=dhcp"
}

variable "vm_ssh_public_key" {
  description = "Public SSH key"
  type        = string
}

variable "vm_cipass" {
  description = "Password"
  type        = string
}

variable "vm_ciuser" {
  description = "Username"
  type        = string
}

variable "vm_storage" {
  description = "Location to store the VM, ie: local-zfs, Ceph_VMS"
  type        = string
  default = "local-zfs"
}

variable "vm_pool" {
  description = "Resource Pool location"
  type        = string
  default = null
}

variable "vm_nameserver" {
  description = "Nameserver"
  type        = string
}

variable "vm_root_size" {
  description = "Size in G for the root disk"
  type        = number
  default = 30
}

variable "vm_disks" {
  description = "List of disks with their sizes and scsi slot numbers"
  type = list(object({
    slot     = number  # Example: 0 for scsi0, 1 for scsi1
    size     = number  # Disk size in GB
    storage  = string  # Storage location
    cache    = string  # Cache mode
    replicate = bool   # Whether to replicate the disk
  }))
  default = [
    { slot = 0, size = 30, storage = "local-zfs", cache = "writeback", replicate = true }
  ]
}




