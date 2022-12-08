from pip._vendor import requests
import time
start = time.time()
response = requests.get("https://www.ynet.co.il/home/0,7340,L-8,00.html")
print(response)
end = time.time()
print (end - start)