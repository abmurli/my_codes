
'''
This python executor stops the Azure VM based on the tag 'AutoStop'. If the tag values is 'yes' then the script will
stop the

CP: Azure
Input: None
'''

from  azure.mgmt.compute  import ComputeManagementClient
from azure.common.client_factory import get_client_from_cli_profile

compute_client = get_client_from_cli_profile(ComputeManagementClient)
count = 0

print (compute_client.virtual_machines.list_all())
for x in compute_client.virtual_machines.list_all():
    tag_list = []
    try:
        tags = x.tags
        rg = str(x.id).split("/")[4]
        if tags:
            # print type(tags)
            for key in tags:
                if key == "autoStop":
                    if tags[key] == "yes":
                        count+=1
                        print (count)
                        print("stopping the instance " + x.name)
                #         # compute_client.virtual_machines.deallocate(rg, x.name)
    except Exception as e:
        print (e)
