resource "azurerm_network_interface" "vm_interface" {
  name                = "${var.projectName}-nic"
  location            = "${var.location}"
  resource_group_name = "${azurerm_resource_group.rg.name}"

  ip_configuration {
    name                          = "${var.projectName}-ip_configuration"
    subnet_id                     = "${azurerm_subnet.datastore_subnet.id}"
    private_ip_address_allocation = "dynamic"
  }
}


resource "azurerm_virtual_machine" "vm" {
  name                  = "${var.projectName}-vm"
  location              = "${var.location}"
  resource_group_name   = "${azurerm_resource_group.rg.name}"
  network_interface_ids = ["${azurerm_network_interface.vm_interface.id}"]
  vm_size               = "${var.zkcs_vm_size}"
  zones = ["${var.vm_az_1}"]
  # Uncomment this line to delete the OS disk automatically when deleting the VM
  # delete_os_disk_on_termination = true

  # Uncomment this line to delete the data disks automatically when deleting the VM
  # delete_data_disks_on_termination = true

  storage_image_reference {
    publisher = "${var.vm_image_publisher}"
    offer     = "${var.vm_image_offer}"
    sku       = "${var.vm_image_sku}"
    version   = "${var.vm_image_version}"
  }

  storage_os_disk {
    name              = "${var.projectName}-vm-os_disk"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }

  storage_data_disk {
    name              = "${var.projectName}-vm-Disk"
    create_option     = "Empty"
    lun               = 0
    disk_size_gb      = "${var.zkcs_data_disk_size_gb}"
    managed_disk_type = "${var.zkcs_data_sa_type}"
  }

  os_profile {
    computer_name  = "${var.projectName}-vm"
    admin_username = "${var.vm_username}"
    admin_password = "${var.vm_password}"
    custom_data = "${file("cloud-config.yaml")}"
  }

  os_profile_linux_config {
    disable_password_authentication = false
  }

  tags {
    environment = "staging"
  }
}

resource "azurerm_virtual_machine_extension" "vm" {
  name                 = "CustomScriptForLinux"
  location             = "${var.location}"
  resource_group_name  = "${azurerm_resource_group.rg.name}"
  virtual_machine_name = "${azurerm_virtual_machine.vm.name}"
  publisher            = "Microsoft.OSTCExtensions"
  type                 = "CustomScriptForLinux"
  type_handler_version = "1.2"
  auto_upgrade_minor_version = true
  depends_on            = ["azurerm_virtual_machine.vm"]

  settings = <<SETTINGS
  {
    "fileUris": ["${var.script_location}"],
    "commandToExecute": "sh script.sh"
  }
SETTINGS
}

# resource "azurerm_virtual_machine_extension" "createApigeeDir" {
#   name                 = "CustomScriptForLinux"
#   location             = "${var.location}"
#   resource_group_name  = "${azurerm_resource_group.rg.name}"
#   virtual_machine_name = "${azurerm_virtual_machine.vm.name}"
#   publisher            = "Microsoft.OSTCExtensions"
#   type                 = "CustomScriptForLinux"
#   type_handler_version = "1.2"
#   auto_upgrade_minor_version = true
#   depends_on            = ["azurerm_virtual_machine_extension.mkfs"]
#
#   settings = <<SETTINGS
#     {
#         "commandToExecute": "sudo mkdir /opt/apigee"
#     }
# SETTINGS
# }
#
# resource "azurerm_virtual_machine_extension" "MountVolume" {
#   name                 = "CustomScriptForLinux"
#   location             = "${var.location}"
#   resource_group_name  = "${azurerm_resource_group.rg.name}"
#   virtual_machine_name = "${azurerm_virtual_machine.vm.name}"
#   publisher            = "Microsoft.OSTCExtensions"
#   type                 = "CustomScriptForLinux"
#   type_handler_version = "1.2"
#   auto_upgrade_minor_version = true
#   depends_on            = ["azurerm_virtual_machine_extension.createApigeeDir"]
#
#   settings = <<SETTINGS
#     {
#         "commandToExecute": "sudo mount /dev/sdc /opt/apigee/"
#     }
# SETTINGS
# }
#
# resource "azurerm_virtual_machine_extension" "fstabBackUp" {
#   name                 = "CustomScriptForLinux"
#   location             = "${var.location}"
#   resource_group_name  = "${azurerm_resource_group.rg.name}"
#   virtual_machine_name = "${azurerm_virtual_machine.vm.name}"
#   publisher            = "Microsoft.OSTCExtensions"
#   type                 = "CustomScriptForLinux"
#   type_handler_version = "1.2"
#   auto_upgrade_minor_version = true
#   depends_on            = ["azurerm_virtual_machine_extension.MountVolume"]
#
#   settings = <<SETTINGS
#     {
#         "commandToExecute": "cp /etc/fstab /etc/fstab.bak"
#     }
# SETTINGS
# }
#
# resource "azurerm_virtual_machine_extension" "fstabEntry" {
#   name                 = "CustomScriptForLinux"
#   location             = "${var.location}"
#   resource_group_name  = "${azurerm_resource_group.rg.name}"
#   virtual_machine_name = "${azurerm_virtual_machine.vm.name}"
#   publisher            = "Microsoft.OSTCExtensions"
#   type                 = "CustomScriptForLinux"
#   type_handler_version = "1.2"
#   auto_upgrade_minor_version = true
#   depends_on            = ["azurerm_virtual_machine_extension.fstabBackUp"]
#
#   settings = <<SETTINGS
#     {
#         "commandToExecute": "echo \"/dev/sdc /opt/apigee ext4  defaults,nofail 0 0\" >> /etc/fstab"
#     }
# SETTINGS
# }

resource "azurerm_virtual_machine_extension" "vm-vmextensionlinux" {
  count                      = "${lower(var.vm_os_type) == "linux" ? 1 : 0}"
  name                       = "ldap1-vm-extension"
  location              = "${var.location}"
  resource_group_name   = "${azurerm_resource_group.rg.name}"
  virtual_machine_name       = "${azurerm_virtual_machine.vm.name}"
  publisher                  = "Microsoft.Azure.Security"
  type                       = "AzureDiskEncryptionForLinux"
  type_handler_version       = "${var.type_handler_version == "" ? "1.1" : var.type_handler_version}"
  auto_upgrade_minor_version = true
  # depends_on            = ["azurerm_virtual_machine_extension.script"]
  depends_on            = ["azurerm_virtual_machine_extension.vm"]

  settings = <<SETTINGS
    {
        "EncryptionOperation": "${var.encrypt_operation}",
        "KeyVaultURL": "${var.key_vault_url}",
        "KeyVaultResourceId": "${var.key_vault_resource_id}",
        "KeyEncryptionKeyURL": "${var.key_encryption_url}",
        "KekVaultResourceId": "${var.key_vault_resource_id}",
        "KeyEncryptionAlgorithm": "${var.encryption_algorithm}",
        "VolumeType": "${var.encryption_volume_type}"
    }
SETTINGS

  tags {
  environment = "test"
  created_by = "murali"
  }
}
