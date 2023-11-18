import json
from nutriCount import ingredient_nutrition_dict

def format_string(input_string):
    # Großbuchstaben in Kleinbuchstaben umwandeln und Unterstriche durch Leerzeichen ersetzen
    formatted_string = input_string.lower().replace('_', ' ')
    return formatted_string

content = None
with open('backend/mockedRecipes_Without_Nutrions.json','r') as f:
   content = json.load(f)

nutrients = ingredient_nutrition_dict



for entry in content:
    ingredients = entry['recipe']['ingredients']
    for i in ingredients:
        if i.get("amount_gram") != None:
            i.update({"amount_per_100_gramm"  : float(i.get("amount_gram"))/100})
        if i.get("amount_tablespoon") != None:
            i.update({"amount_per_100_gramm"  : (float(i.get("amount_tablespoon"))*13)/100})
        if i.get("amount_ounce") != None:
            i.update({"amount_per_100_gramm"  : (float(i.get("amount_ounce"))*28.3495)/100})
        if i.get("amount_cup") != None:
            i.update({"amount_per_100_gramm"  : (float(i.get("amount_cup"))*200)/100})  
        i_nut = nutrients.get(i.get("name"))  

        if i_nut!=None:
            for nut in i_nut:
                print(nut)

                entry['recipe']['nutrition'][nut]['value'] = float(i.get("amount_per_100_gramm"))* (float(entry['recipe']['nutrition'][nut]['value']) + float(nutrients[i.get("name")][nut]["value"]))
                
            i.update(i_nut)

    
f = open("backend/mockedRecipes_with_Nutrition.json", "a")
json.dump(content,f)
f.close()