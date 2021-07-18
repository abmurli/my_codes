import datetime
from azure.mgmt.monitor import MonitorManagementClient
from azure.common.credentials import ServicePrincipalCredentials

# Get the ARM id of your resource. You might chose to do a "get"
# using the according management or to build the URL directly
# Example for a ARM VM
subscription_id = ""
resource_group_name = ""
vm_name = ""

TENANT_ID = ''
CLIENT = ''
KEY = ''

start_time = "2019-06-25"
end_time = "2019-09-21"
credentials = ServicePrincipalCredentials(
    client_id = CLIENT,
    secret = KEY,
    tenant = TENANT_ID
)

resource_id = (
    "/subscriptions/{}/"
    "resourceGroups/{}/"
    "providers/Microsoft.Compute/virtualMachines/{}"
).format(subscription_id, resource_group_name, vm_name)

# create client
client = MonitorManagementClient(credentials, subscription_id)

filter = ("eventTimestamp ge '{}' and eventTimestamp le '{}' and resourceUri eq '{}'").format(start_time, end_time, resource_id)
print (filter)
select = ",".join([
    "eventTimestamp",
    "eventName",
    "operationName",
    "resourceGroupName",
    "resourceId",
    "caller"
])

activity_logs = client.activity_logs.list(
    filter=filter,
    select=select
)
print (activity_logs)

for log in activity_logs:
    print(" ".join([
        str(log.event_timestamp),
        str(log.resource_group_name),
        log.event_name.value,
        log.operation_name.value,
        str(log.resource_id).split("/")[8]
    ]))