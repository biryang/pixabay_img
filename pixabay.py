import requests
import json
from bs4 import BeautifulSoup
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['KEY']['PIXABAY']
URL = f"https://pixabay.com/api/?key={API_KEY}&image_type=photo&pretty=true&per_page=3&q="


def extract_pixabay_api(food):
    result = requests.get(f"{URL}{food}")
    try:
        json_result = result.json()
        img_url = json_result['hits'][0]['largeImageURL']
    except:
        img_url = None

    return img_url
