from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.compute.models import DiskCreateOption

compute_client = get_client_from_cli_profile(ComputeManagementClient)
storage_client = get_client_from_cli_profile(StorageManagementClient)

GROUP_NAME = ''
LOCATION = ''
VM_NAME = ''

disk_creation = compute_client.disks.create_or_update(
        GROUP_NAME,
        '',
        {
            'location': LOCATION,
            'disk_size_gb': 10,
            'creation_data': {
                'create_option': 'Empty'
            },
            'encryption_settings': {
                'enabled': 'true',
                'disk_encryption_key': {
                  'source_vault': {
                    'id': '/subscriptions/<subscription_id>/resourceGroups/<resource_group_name>/providers/Microsoft.KeyVault/vaults/<vault_name>'
                  },
                  'secret_url': 'https://<vault_name>.vault.azure.net/secrets/<id>/<id>'
                },
                'key_encryption_key': {
                  'source_vault': {
                    'id': '/subscriptions/<subscription_id>/resourceGroups/<resource_group_name>/providers/Microsoft.KeyVault/vaults/<vault_name>'
                  },
                  'key_url': 'https://<vault_name>.vault.azure.net/keys/<key_name>/<Key_id>'
                }
            }

        }
    )
print (disk_creation.result())

vm = compute_client.virtual_machines.get(GROUP_NAME, VM_NAME)
add_result = vm.storage_profile.data_disks.append({
  'lun': 1,
  'name': '',
  'create_option': DiskCreateOption.attach,
  'managed_disk': {
      'id': disk_creation.result().id
  }
  })
add_result = compute_client.virtual_machines.create_or_update(
        GROUP_NAME,
        VM_NAME,
        vm)