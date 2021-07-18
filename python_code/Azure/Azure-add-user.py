from  azure.mgmt.compute  import ComputeManagementClient
from azure.common.client_factory import get_client_from_cli_profile
import subprocess

compute_client = get_client_from_cli_profile(ComputeManagementClient)
count = 0

# print compute_client.virtual_machines.list_all()
for x in compute_client.virtual_machines.list_all():

    name = x.name
    rg = str(x.id).split("/")[4]
    status = compute_client.virtual_machines.instance_view(rg, name)
    vm_status = status.statuses[1].display_status

    if str(vm_status) == "VM running":
        print(name + " is running and os: " +status.os_name)

        if status.os_name == "ubuntu":
            # if name == "kube-master":
            #     subprocess.check_output(["az", "vm", "run-command", "invoke", "-g",
            #                          rg, "-n", name, "--command-id", "RunShellScript",
            #                          "--scripts", "@userdel.sh"])
                print("----------------")
        else:
            if str(name).startswith(""):
                subprocess.check_output(["az", "vm", "run-command", "invoke", "-g",
                                         rg, "-n", name, "--command-id", "RunShellScript",
                                         "--scripts", "@useradd.sh"])
                print("----------------")
    else:
        print(name + " is stopped or deallocated")
