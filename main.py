import os
import json
import urllib.request.request
from multiprocessing import pool
from threading import Lock


dir_lock = Lock()
API_TO_READ = "https://jsonplaceholder.typicode.com/photos"


def download_url(url):
    url_file = urllib.request.urlopen(API_TO_READ)
    url_buffer = url_file.read()
    url_file.close()
    return url_buffer


def get_photos():
    return json.loads(download_url(API_TO_READ))


def safe_create_dir(dir_name):
   if os.path.exists(dir_name):
       return
   with dir_lock:
       if not os.path.exists(dirname):
           os.mkdir(dir_name)


def download_photo(photo_dict):
   photo_buff = download_url(photo_dict["thumbnailUrl"])
   dir_name = photo_dict["albumId"]
   safe_create_dir(dir_name)
   file_name = "%d.png" % (photo_dict["id"])
   file_path = os.path.join(dir_name, file_name)
   with open(file_path, 'wb') as file_handle:
       file_handle.write(photo_buff)


def main():
    photos = get_photos()
    with pool(workers=10) as process_pool:
        process_pool.map(photos, download_photo)


if __name__ == "__main__":
    main()
