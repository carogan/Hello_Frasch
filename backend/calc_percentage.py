from nutriCount import RDA
import json

with open('backend/mockedRecipes_with_Nutrition.json','r') as f:
   recipes = json.load(f)

daily = RDA.get("women")
percentages = []
for item in recipes:
    recipe = item.get("recipe")
    nutris = recipe.get("nutrition")
    perc = []
    for n in nutris:
        if daily.get(n) != None:
            perc.append((str(n),100.0*(float(nutris.get(str(n))["value"])/float(daily[n]["value"]))))
    percentages.append(perc)

f = open("backend/calc_results.py", "a")
for list in percentages:
    f.write(str(list))
    f.write("\n")
f.close()