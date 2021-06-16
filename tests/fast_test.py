import requests
import json


print("Testing POST endpoint 😀 ")
data = {
    "title": "Israel-Gaza, Spa shootings, Obesity drugs: Your Tuesday Evening Briefing",
    "author": "Whet Moser and Jade-Snow Joachim",
    "source": "New York Times",
    "description": "random desc",
    "url": "https://www.nytimes.com/2021/05/11/briefing/israel-gaza-spa-shootings-obesity-drugs.html",
    "publishedAt": "2021-05-11",
    "content": "10. And finally, the warm embrace of Asian supermarkets.\r\nH Mart began as Han Ah Reum, Korean for an armful, in Woodside, Queens. In 2020, its 105 locations sold $1.5 billion worth of kimchi, banchanâ€¦ [+837 chars]"
  }

#{"detail":[{"loc":["query","sample"],"msg":"field required","type":"value_error.missing"}]}'
response = requests.post('http://127.0.0.1:8000/predict', json=data)

print(f"{response.status_code} -- {response.content}")

