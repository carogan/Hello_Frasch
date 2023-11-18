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
ingredient = "Chicken Stock Concentrate"
correct_json = False
while correct_json is False:

    completion = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Food lover"},
        {"role": "user", "content": "The user does not like " + ingredient +", Replace in this receipe all ingredients with " + ingredient +" where they appears with the right amount of a similar ingredient in usage which is used in another dish of the list. If absolutly no possible replacemant exists, do not replace it and instead change the name of the ingredient to the original name +  no replacement possible. Only do this in the list of ingredients. Do not invent a new ingredient name that was not used in a different ingredient. Return just the new json object thus the response should start with [{\"index\": 1,... and end with}]. THe json object has to compile:" + json.dumps(content)}
    ]
    )
    #with open("backend/output.json", 'w') as json_file:
    #    json.dump(str(completion.choices[0].message.content), json_file, indent=1)
    response = str(completion.choices[0].message.content)
    try:
        dict = json.loads(response)
        correct_json = True
    except ValueError as e:
        correct_json = False
f = open("backend/output.json", "a")
f.write(response)
f.close()
