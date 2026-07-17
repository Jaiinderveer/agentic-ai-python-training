"""
    Create Virtual Environment
        1.Create the Environment
            python -m venv .nameofyourenv
            python -m venv .venv
        
        2. Activate the Environment
            Bash: source .venv/bin/activate
            windows: .venv/Scripts/activate.bat
        
        3. Install Libraries
            pip install requests
"""
import requests
import json
api_key = open('day11/api_key.txt','r').read().strip()
newsapi_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
response = requests.get(newsapi_url)
news_json = response.text
news_dictionary = json.loads(news_json)

print(news_dictionary)

articles = news_dictionary['articles']
for article in articles:
    print(article['title'])
    print(article['description'])
    print('~'*30)