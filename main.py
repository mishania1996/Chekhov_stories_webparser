import requests 
import time, os
from bs4 import BeautifulSoup
from parsestory import parse_story

os.mkdir("stories")

url = "http://chehov-lit.ru/chehov/text/rasskazy.htm" #the main URL with around 600 stories
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} #to imitate the browser

response = requests.get(url, headers = headers)

if response.status_code == 200: #200 status code means the successful response
    soup = BeautifulSoup(response.content, "html.parser")
    i = 0
    for el in soup.find_all('a'): #the stories where in the a tags
        if i < 2: #the first 2 links were not the stories so we ignore those links
            i+=1
            continue
        if 'href' in el.attrs: #links with stories have href attribute in tag a
            x="http://chehov-lit.ru" + el['href'] 
            print(x)
            parse_story(x)
            time.sleep(2) #adding delay for each iteration
else:
    print(f"Failed to retrieve the webpage, status code: {response.status_code}")



