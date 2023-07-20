import requests 
from send_email import send_email 

API_KEY = 'db202092afe140189ae03c36492fdd52'

url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-06-20&sortBy=publishedAt&apiKey=db202092afe140189ae03c36492fdd52' 

#Make a request 
request = requests.get(url)

#Get a dictionary with Data 
content = request.json()
#print(content['articles'])

#Access titles 

body = ''

for article in content['articles']:
    body = body + article['title'] + '\n' + article['description'] + 2*'\n'

body = body.encode('utf-8')

send_email(body)