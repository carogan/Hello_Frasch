import json
from nutriCount import ingredient_nutrition_dict

content = None
with open('backend/mockedRecipes.json','r') as f:
   content = json.load(f)

nutrients = ingredient_nutrition_dict



for entry in content:
    ingredients = entry['recipe']['ingredients']
    for i in ingredients:
        if i.get("amount_gram") != None:
            i.update({"amount per 100 gramm"  : float(i.get("amount_gram"))/100})
        if i.get("amount_tablespoon") != None:
            i.update({"amount per 100 gramm"  : (float(i.get("amount_tablespoon"))*13)/100})
        if i.get("amount_ounce") != None:
            i.update({"amount per 100 gramm"  : (float(i.get("amount_ounce"))*28.3495)/100})
        if i.get("amount_cup") != None:
            i.update({"amount per 100 gramm"  : (float(i.get("amount_cup"))*200)/100})  
        i_nut = nutrients.get(i.get("name"))  
    
        if i_nut!=None:
            if entry['recipe']['nutritions'].get(i_nut) != None:
                print("bla")
            i.update(i_nut)

    


print("bla")
def convertTo100Gramm(dict:dict):
    pass
