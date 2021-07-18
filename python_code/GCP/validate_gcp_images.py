from googleapiclient import discovery

compute = discovery.build('compute', 'v1')
project = ""
zone = ""
ami = ""
result = compute.images().list(project=project).execute()['items']

images_list = [images['name'] for images in result if ami == images['name']]
if images_list:
    print(f"image {images_list[0]} found")
else:
    print(f"image {images_list[0]} not found")