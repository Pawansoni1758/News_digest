import requests
from send_email import send_email

topic = "cricket"
api_key = "280f27cb7f164bfeb840e4017d801ff8"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2023-07-30&"
       "sortBy=publishedAt&"
       "apiKey=280f27cb7f164bfeb840e4017d801ff8&"
       "language=en")

# make request
request = requests.get(url)

# get a dictionary with data
contents = request.json()

# access the articles, titles and description
body = ""
for content in contents['articles'][:20]:
       if content['title'] != None:
           body = (body + "Subject: Today's news"+"\n"
                   +content['title']
                   + "\n" + content['description']
                   +"\n"+ content['url']+ 2*"\n")

body = body.encode("utf-8")
send_email(body)
