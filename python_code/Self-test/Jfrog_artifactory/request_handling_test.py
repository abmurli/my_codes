import requests
from requests.auth import HTTPBasicAuth


def download_file(jfrog_username, jfrog_password, download_path, url):
    r = requests.get(url, verify=False, auth=HTTPBasicAuth(jfrog_username, jfrog_password))
    print(r.status_code)


if __name__ == '__main__':
    url = ""
    download_path = ""
    jfrog_username = ""
    jfrog_password = ""
    download_file(jfrog_username, jfrog_password, download_path, url)