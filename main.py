import requests 

API_KEY = 'db202092afe140189ae03c36492fdd52'

url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-06-20&sortBy=publishedAt&apiKey=db202092afe140189ae03c36492fdd52' 

#Make a request 
request = requests.get(url)

#Get a dictionary with Data 
content = request.json()
#print(content['articles'])

#Access titles 
for article in content['articles']:
    print(article['title'])
