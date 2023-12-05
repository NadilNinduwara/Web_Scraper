import requests
from bs4 import BeautifulSoup
import csv

response = requests.get('https://www.yelp.com/search?find_desc=Gyms&find_loc=San%20Francisco%2C%20CA')

soup = BeautifulSoup(response.content, 'html.parser')

activities = soup.find_all('a', class_='css-19v1rkv')
ratings = soup.find_all('span', class_='css-gutk1c')

file_name = 'activities.csv'

with open(file_name, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Activity', 'Rating'])

    for name, rating in zip(activities, ratings):
        a_name = name.text.strip()
        rating = rating.text.strip()

        csvwriter.writerow([a_name, rating])
