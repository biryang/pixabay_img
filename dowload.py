import os
import time


def download_images(list):
    for data in list:
        if data[1] is not None:
            name = data[0]
            url = data[1]
            # curl 요청
            os.system(f"curl {url} > images/{name}.jpg")
