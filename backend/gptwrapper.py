import os
import openai 
from config import OPENAI_API_KEY
import json
import re
import nutriCount
from ingredientsList import ingredients

openai.api_key = OPENAI_API_KEY
content = None


with open('backend/mockedRecipes_with_Nutrition.json','r') as f:
   recipes = json.load(f)

#content = json.load("backend/mockedRecipes.js")
nutri = "Iron"
content = recipes[1]
correct_json = False
while correct_json is False:

    completion = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Nutritional Diet"},
        {"role": "user", "content": "I want to make a recipe, but it is low in " + nutri +", please replace one or more ingredients so that the "+nutri+" amount increases. Only use inredients from \"" + str(ingredients) +" \" Return the whole receipe with all ingredients as new json object and the json object has to have correct syntax, thus the response should start with [{\"index\": 1,... and end with }] :" + json.dumps(content)}        ])
    #    json.dump(str(completion.choices[0].message.content), json_file, indent=1)
    response = str(completion.choices[0].message.content)
    try:
        dict = json.loads(response)
        correct_json = True
    except ValueError as e:
        correct_json = False
f = open("backend/ai_recommendation.json", "a")
f.write(response)
f.close()
