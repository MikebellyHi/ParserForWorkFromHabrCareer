from unittest import result
from bs4 import BeautifulSoup
import requests



url = "https://career.habr.com/vacancies?qid=3&skills[]=446&type=all" #url Habr/Juniordev/Python
request = requests.get(url) #get requests from Habr

soup = BeautifulSoup(request.text, "html.parser") #to find HTML-code

#numbers = soup.find_all("a", class_="vacancy-card__title-link") 
#print(numbers) 

def GetLinks():
    links = []

    for link in soup.find_all('a', class_="vacancy-card__title-link"):
        links.append(link.get('href'))

    #print(links)

    kost = 'https://career.habr.com'

    for i in range (0, len(links)):
        a = links[i]
        b = kost + a
        links[i] = b

    return links

