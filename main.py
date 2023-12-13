import requests
from send_email import send_email

api_key = "49050dbeaf294ae7aba2217ac3b89038"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-11-13&sortBy=publishedAt&apiKey"
       "=49050dbeaf294ae7aba2217ac3b89038")


# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access articles titles and descriptions
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(body)



