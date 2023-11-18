import os
import openai 
from config import OPENAI_API_KEY
import json
import re
import nutriCount

openai.api_key = OPENAI_API_KEY
content = None


with open('backend/mockedRecipes_with_Nutrition.json','r') as f:
   recipes = json.load(f)

#content = json.load("backend/mockedRecipes.js")
ingredient = "Lime"
content = recipes[2]
correct_json = False
while correct_json is False:

    completion = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Food lover"},
        {"role": "user", "content": "I want to make a recipe, but it is low in Iron, please replace one ingredient so that the iron amount increases. Return just the new json object and the json object has to have correct syntax, thus the response should start with [{\"index\": 1,... and end with}] :" + json.dumps(content)}    #with open("backend/output.json", 'w') as json_file:
        ])
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
