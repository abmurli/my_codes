variable "vm_os_type" {
  description = "Type of OS. Allowed values are Windows and Linux. Defaults to Linux"
  default     = "linux"
}

variable "prefix" {
  description = "resource prefix"
  default     = ""
}

variable "username" {
  description = "user name of the VM"
  default     = "abmurli"
}

variable "password" {
  description = "password of the VM"
  default     = ""
}

variable "location" {
  description = "region"
  default = "West Europe"
}

variable "resource_group" {
  description = "resource group name"
  default = ""
}

variable "volume_type" {
  description = "volume type"
  default = "Premium_LRS"
}

variable "mount_point" {
  description = "mount point"
  default = ""
}

variable "ssh_key" {
  description = "Path to the public key to be used for ssh access to the VM"
  default     = ""
}

variable "auth_keys_path" {
  description = "Path to authorized keys file"
  default     = ""
}

variable "encrypt_operation" {
  default = "EnableEncryption"
}

variable "type_handler_version" {
  description = "Type handler version of the VM extension to use. Defaults to 2.2 on Windows and 1.1 on Linux"
  default     = ""
}

variable encryption_algorithm {
  description = " Algo for encryption"
  default     = "RSA-OAEP"
}

variable "encryption_volume_type" {
  description = "type of volume to be encrypted. Allowed values are All, DATA and OS"
  default = "All"
}

variable "subnet_id" {
  description = "id of the subnet in which the VM is to be launched"
  default = ""
}

variable "private_ip_address_allocation" {
  default = "dynamic"
}

variable "os_publisher" {
  default = "Canonical"
}

variable "operating_system" {
  default = "UbuntuServer"
}

variable "operating_sys_version" {
  default = "16.04-LTS"
}

variable "disk_caching" {
  default = "ReadWrite"
}

variable "os_disk_size" {
  description = "os disk size in GiB"
  default = "30"
}

variable "data_disk_size" {
  description = "data disk size in GiB"
  default = "10"
}

variable "lun" {
  default = "0"
}

variable "cloud-init" {
  default = "cloud-init-ubuntu-volume-encryption-ext.yaml"
}

variable "key_vault_url" {
  description = "key vault URL. eg. https://<vault_name>.vault.azure.net/"
  default = ""
}

variable "key_vault_resource_id" {
  description = "key vault resource id. eg. /subscriptions/<subscription_id>/resourceGroups/<resource_group_name>/providers/Microsoft.KeyVault/vaults/<vault_name>"
  default = ""
}

variable "key_encryption_url" {
  description = "key vault key URL. eg. https://<vault_name>.vault.azure.net/keys/<key_name>/<key_version>"
  default = ""
}
