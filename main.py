import openai
import os
from dotenv import load_dotenv
import random
from connection import Connection 
from createMessage import CreateMessage

load_dotenv()

openai.api_key = os.environ['API_KEY']

category = ["ロマンス", "ミステリ", "ファンタジー", "サスペンス", "ドラマ"]


def main():
    connection = Connection()
    user_id = connection.get_chatgpt_account()
    create_message = CreateMessage()
    categories = connection.get_categories()
    category = random.choice(categories)
    title_msg = create_message.create_title_message(category["name"])
    response1 = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                {'role': 'user', 'content': title_msg},
                ],
                temperature=1,
                )
    title = response1.choices[0].message.content
    content_msg =  create_message.create_content_message(title)
    response2 = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                {'role': 'user', 'content': content_msg},
                ],
                temperature=1,
                )
    content = response2.choices[0].message.content
    res = connection.post_novel(title, category, content, user_id)
    print(res.ok)
    return res

main()
