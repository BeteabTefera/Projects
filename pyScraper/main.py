import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github User: ')

#send a request to the github url
url = f'https://github.com/{github_user}'

#send request
r = requests.get(url)
soup = bs(r.content)
print(soup.prettify())
profile_image = soup.find('img',{'alt':'Avatar'})
print(profile_image)
