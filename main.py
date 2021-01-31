from pixabay import extract_pixabay_api
from save import sav_to_csv
from dowload import download_images
import csv

food_list = {}

f = open('foodlist.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

for line in rdr:
    food_name = line[0]
    img_url = extract_pixabay_api(food_name)
    food_list[food_name] = img_url
f.close()

new_list = []
for name, url in food_list.items():
    new_list.append([name, url])
print(new_list)

download_images(new_list)
# sav_to_csv('food_url', new_list)
