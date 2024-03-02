import requests
import re
from bs4 import BeautifulSoup

def parse_story(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} #to imitate browser
    response = requests.get(link, headers = headers)

    if response.status_code == 200: #success code
        soup = BeautifulSoup(response.content, "html.parser")
        txt = soup.find('p', align = 'center').text #the story is nested in the p tag with the headline which is aligned in the center
        namefile = re.search(r'/([^/]*)$', link).group(1) #the name of a story is part of its URL which starts after the final slash
        with open("stories/" + namefile+'.txt','w') as f:
            f.write(txt)
    else:
        print(f"Failed to retrieve the webpage, status code: {response.status_code}")
