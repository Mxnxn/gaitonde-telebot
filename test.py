import requests

API = 'https://torrents-csv.ml/service/search?q=uncharted&size=6&page=1&type_=torrent'

res = requests.get(API,headers={'USER-AGENT':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})

print(res.json())