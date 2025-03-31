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

variable "tf_home" {
  description = "Home directory for this location"
  type        = string
}

variable "pm_datacenter" {
  description = "A proxmox host connected to the DC"
  type        = string
}

variable "network_prefix_0" {
  description = "The prefix for the network ie: 192.168.20"
  type        = string
}

variable "network_prefix_1" {
  description = "The prefix for the network ie: 192.168.20"
  type        = string
  default = null
}

variable "nameserver" {
  description = "The nameserver"
  type        = string
}
