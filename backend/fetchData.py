import requests
import json

def fetch_and_save_food_data(food_items, api_key):
    base_url = "https://api.nal.usda.gov/fdc/v1/food/"
    
    for food_name, food_id in food_items.items():
        url = f"{base_url}{food_id}?api_key={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            filename = f"{food_name.replace(' ', '_')}.json"
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Data for {food_name} saved to {filename}")
        else:
            print(f"Failed to fetch data for {food_name}: Status code {response.status_code}")

food_items = {
    "green olives": 2345616,
    "quinoa tricolor": 2404710,
    "onion": 170000,
    "garlic clove": 169230,
    "coriander": 170921,
    "spice mix hello harissa": 2093082,
    "lemon": 167746,
    "carrot": 170393,
    "chicken broth": 174536,
    "chopped chicken": 2646170,
    "ya'atar": 2437110,
    "scallions": 170005,
    "lime": 168155,
    "ground pork": 167903,
    "shredded red cabbage": 169977,
    "hoisin sauce": 172886,
    "sweet thai chili sauce": 2601338,
    "sweet soy glaze": 2024761,
    "jasmine rice": 2343892,
    "sesame seeds": 170150,
    "potatoes": 170032,
    "broccoli florets": 170382,
    "apple": 168171,
    "pork chops": 167823,
    "brown sugar bourbon seasoning": 2127372,
    "chicken stock concentrate": 2166982,
    "sour cream": 171257,
    "cilantro": 2345302,
    "garlic powder": 171325,
    "gochujang sauce": 2244609,
    "coleslaw mix": 2051926,
    "mayonnaise": 171009,
    "flour tortillas": 169724,
    "cashews": 170162,
    "yellow onion": 170004,
    "garlic": 169230,
    "kale": 169238,
    "italian seasoning": 1887966,
    "Crushed tomatoes": 170501,
    "veggie stock concentrate": 2399720,
    "israeli couscous": 2388833,
    "demi baguette": 2636666,
    "parmesan cheese": 171247,
    "chili flakes": 1135511,
    "yukon gold potatoes": 2251779,
    "monterey jack cheese": 2341123,
    "cajun spice blend": 1868450,
    "hot sauce": 171186,
    "kidney beans": 175196,
    "sliced dill pickle": 168558,
    "tempura mix": 2034431,
    "brioche buns": 1124666 



}

fetch_and_save_food_data(food_items, api_key)
