import os
import openai 
from config import OPENAI_API_KEY
import json

openai.api_key = OPENAI_API_KEY
content = None
with open('backend/mockedRecipes.js','r') as f:
   content = f.readlines()

#content = json.load("backend/mockedRecipes.js")
completion = openai.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "Food lover"},
    {"role": "user", "content": "Replace in this receipe list the ingredient Pfeffer with Jasminreis where it appears and return just the new js file:" + str(content)}
  ]
)

f = open("backend/output.txt", "a")
f.write(str(completion.choices[0].message.content))
f.close()
