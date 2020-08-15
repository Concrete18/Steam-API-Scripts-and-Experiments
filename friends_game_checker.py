import requests
from bs4 import BeautifulSoup


profile_id = 'concretesurfer'
url = f'https://steamcommunity.com/id/{profile_id}/games/?tab=all'
source = requests.get(url)
if source.status_code == requests.codes.ok:
    soup = BeautifulSoup(source.text, 'html.parser')
    content = soup.find_all(class_="gameListRowItemName ellipsis ")
    for item in content:
        print(item.text)