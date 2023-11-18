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
    "Green olives": 2345616,
    "Quinoa tricolor": 2404710,
    "Onion": 170000,
    "Garlic clove": 169230,
    "Coriander": 170921,
    "Spice mix hello harissa": 2093082,
    "Lemon": 167746,
    "Carrot": 170393,
    "Chicken broth": 174536,
    "Chopped chicken": 2646170,
    "Za'atar": 2437110,
    "Scallions": 170005,
    "Lime": 168155,
    "Ground Pork": 167903,
    "Shredded Red Cabbage": 169977,
    "Hoisin Sauce": 172886,
    "Sweet Thai Chili Sauce": 2601338,
    "Sweet Soy Glaze": 2024761,
    "Jasmine Rice": 2343892,
    "Sesame Seeds": 170150,
    "Potatoes": 170032,
    "Broccoli Florets": 170382,
    "Apple": 168171,
    "Pork Chops": 167823,
    "Brown Sugar Bourbon Seasoning": 2127372,
    "Chicken Stock Concentrate": 2166982,
    "Sour Cream": 171257
}

api_key = "36eBehLa4oHWUAFzCjY6YR20fD6J7o0WHPBeGrEB"

fetch_and_save_food_data(food_items, api_key)
