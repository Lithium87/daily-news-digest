import requests
from send_email import send_email

topic = "tesla"

api_key = "49050dbeaf294ae7aba2217ac3b89038"
url = (f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey"
       "=49050dbeaf294ae7aba2217ac3b89038&language=en")


# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access articles titles and descriptions
body = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    body = (body + article["title"] + "\n"
            + str(article["description"]) + "\n" + str(article["url"]) + 2*"\n")

body = body.encode("utf-8")
send_email(body)
