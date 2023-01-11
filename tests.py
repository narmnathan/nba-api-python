import requests

page = requests.get(url="https://www.basketball-reference.com/players/d/doncilu01/gamelog/2023")
print(page.text)