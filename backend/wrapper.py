import os
import openai 
from config import OPENAI_API_KEY
import json
import re

openai.api_key = OPENAI_API_KEY
content = None
with open('backend/mockedRecipes.json','r') as f:
   content = json.load(f)

#content = json.load("backend/mockedRecipes.js")
completion = openai.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "Food lover"},
    {"role": "user", "content": "The user does not like pork, Replace in this receipe all ingredients with pork where they appears with the right amount of a similar ingedrient which is used in another dish of the list (with the exact same title) and return just the new json object thus the response should start with [{\"index\": 1,... and end with}]:" + json.dumps(content)}
  ]
)
response = str(completion.choices[0].message.content)
f = open("backend/output.json", "a")
f.write(response)
f.close()
