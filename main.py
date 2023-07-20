import requests 
from send_email import send_email 

topic = 'tesla'

API_KEY = 'db202092afe140189ae03c36492fdd52'

url = f'https://newsapi.org/v2/everything?q={topic}&from=2023-06-20&sortBy=publishedAt&apiKey=db202092afe140189ae03c36492fdd52&language=en' 

#Make a request 
request = requests.get(url)

#Get a dictionary with Data 
content = request.json()
#print(content['articles'])

#Access titles 
body = ''

for article in content['articles'][:20]:
    body = "Subject: Today's news" + '\n' + body + article['title'] + '\n' + article['description'] + '\n' + article['url'] + 2*'\n'

body = body.encode('utf-8')

send_email(body)