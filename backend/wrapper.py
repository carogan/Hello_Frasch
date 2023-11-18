import os
import openai 
from config import OPENAI_API_KEY
import json
import re
import nutriCount

openai.api_key = OPENAI_API_KEY
content = None


with open('backend/mockedRecipes.json','r') as f:
   content = json.load(f)

#content = json.load("backend/mockedRecipes.js")
ingredient = "Lime"
correct_json = False
while correct_json is False:

    completion = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Food lover"},
        {"role": "user", "content": "The user does not like " + ingredient +", Replace in this recipe all ingredients with " + ingredient +" where it appears with the right amount of a similar ingredient  which is used in another dish of the list. The replacement ingredient should have a similar usage, taste is not as important. The replacement ingredient has to have the exact same name and type as an ingredient used in a different recipe in this list. For example, an apple could be replaced with a pear but only if the pear is used in a recipe in the list. An apple could not be replaced by pear jelly since pear jelly has a different usage. If absolutely no possible replacement exists, do not replace it and instead change the name of the ingredient to the original name + no replacement possible. Only do this in the list of ingredients. Return just the new json object and the json object has to have correct syntax, thus the response should start with [{\"index\": 1,... and end with}] :" + json.dumps(content)}    
        ])
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
