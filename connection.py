import requests
import random
import json
import os
from dotenv import load_dotenv
import pprint 

class Connection:
    load_dotenv()

    api_url = os.getenv("DJANGO_API_URL")
    word_len = [1000, 2000, 3000, 4000, 5000]
    
    def api_connection(self):
        try:
            url = self.api_url
            return url
        except Exception as e:
            print(e)
            return e
    def get_chatgpt_account(self):
        try:
            url = self.api_url + "users/chat-gpt/"
            res = requests.get(url,verify=False)
            chatgpt_id = res.json()["pk"]
            return chatgpt_id
        except Exception as e:
            print(e)
            return e
    
    def get_categories(self):
        try:
            url = self.api_url + "categories/"
            res = requests.get(url,verify=False)
            return res.json()
        except Exception as e:
            print(e)
            return e
    
    def get_words_len(self):
        len = str(random.choice(self.sword_len))
        return len
    
    def post_novel(self, title, category, content, user_id):
        url = self.api_url + "novels/"
        novel_values = { "title": title, "user_id": user_id, "content": content, "categories": [category["name"]] }
        try:
            # data = 
            res = requests.post(url, data=json.dumps(novel_values), verify=False)
            return res
        except Exception as e:
            print(e)
            return e

    
