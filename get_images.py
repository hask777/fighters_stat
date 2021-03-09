import json
from GoogleImageScrapper import GoogleImageScraper
import os

#Define file path
webdriver_path = os.getcwd()+"\\webdriver\\chromedriver.exe"
image_path = os.getcwd()+"\\photos"

file = "fighter_name.json"
data =None
with open(file, 'r') as f:
    data = json.load(f)
    
# print(data)

for fighter in data:
    # print(fighter["FirstName"] + " " + fighter["LastName"])
    search_keys = [fighter["FirstName"] + " " + fighter["LastName"] + "png"]

    #Parameters
    number_of_images = 10
    headless = False
    min_resolution = (0,0)
    max_resolution = (1920,1080)

    #Main program
    for search_key in search_keys:
        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
        image_urls = image_scrapper.find_image_urls()
        image_scrapper.save_images(image_urls)