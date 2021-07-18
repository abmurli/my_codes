'''
read the secret manager in GCP
input(s):
project_id: <project id of GCP account>
secret_id: <secret name>

output(s)
secret values : json
'''
import sys

from google.cloud import secretmanager
import os
import json


def get_secret_value(client, name):
    try:
        response = client.access_secret_version(request={"name": name})
        decoded_output = response.payload.data.decode()

        json_output = json.loads(decoded_output)
        return json_output
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


def import_gcp_creds():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "credential.json"
    print("gcp credentials imported")


if __name__ == "__main__":
    client = secretmanager.SecretManagerServiceClient()
    project_id = ""
    secret_id = ""
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    secret_value = get_secret_value(client, name)
    print(secret_value)