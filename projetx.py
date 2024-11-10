import requests
for i in range(1,101):
    print(i)


text=requests.get("https://en.wikipedia.org/wiki/HTML").text
print(text)