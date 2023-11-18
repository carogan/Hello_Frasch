import os
import json

# Variables

directory = "backend/Data"

RDA = {
    "men": {
        "Vitamin A": {"value": 900, "unit": "mcg"},
        "Vitamin B6": {"value": 1.3, "unit": "mg"},
        "Vitamin B9": {"value": 400, "unit": "mcg"},
        "Vitamin B12": {"value": 2.4, "unit": "mcg"},
        "Vitamin C": {"value": 90, "unit": "mg"},
        "Vitamin D": {"value": 15, "unit": "mcg"},
        "Vitamin E": {"value": 15, "unit": "mg"},
        "Vitamin K": {"value": 120, "unit": "mcg"},
        "Calcium": {"value": 1000, "unit": "mg"},
        "Magnesium": {"value": 420, "unit": "mg"},
        "Potassium": {"value": 4700, "unit": "mg"},
        "Selenium": {"value": 55, "unit": "mcg"},
        "Zinc": {"value": 11, "unit": "mg"},
        "Iron": {"value": 8, "unit": "mg"},

    },
    "women": {
        "Vitamin A": {"value": 700, "unit": "mcg"},
        "Vitamin B6": {"value": 1.3, "unit": "mg"},
        "Vitamin B9": {"value": 400, "unit": "mcg"},
        "Vitamin B12": {"value": 2.4, "unit": "mcg"},
        "Vitamin C": {"value": 75, "unit": "mg"},
        "Vitamin D": {"value": 15, "unit": "mcg"},
        "Vitamin E": {"value": 15, "unit": "mg"},
        "Vitamin K": {"value": 90, "unit": "mcg"},
        "Calcium": {"value": 1000, "unit": "mg"},
        "Magnesium": {"value": 320, "unit": "mg"},
        "Potassium": {"value": 4700, "unit": "mg"},
        "Selenium": {"value": 55, "unit": "mcg"},
        "Zinc": {"value": 8, "unit": "mg"},
        "Iron": {"value": 18, "unit": "mg"},

    }
}

desired_nutrients = {
    "Vitamin A, RAE": {"unit": "mcg"},
    #"Vitamin A, IU": {"unit": "mcg"},
    "Vitamin B6": {"unit": "mg"},
    "Vitamin B9": {"unit": "mcg"},
    "Vitamin B-12": {"unit": "mcg"},
    "Vitamin C, total ascorbic acid": {"unit": "mg"},
    "Vitamin D (D2 + D3)": {"unit": "mcg"},
    "Vitamin E (alpha-tocopherol)": {"unit": "mg"},
    "Vitamin K (phylloquinone)": {"unit": "mcg"},
    "Calcium, Ca": {"unit": "mg"},
    "Magnesium, Mg": {"unit": "mg"},
    "Potassium, K": {"unit": "mg"},
    "Selenium, Se": {"unit": "mcg"},
    "Zinc, Zn": {"unit": "mg"},
    "Iron, Fe": {"unit": "mg"}
}

# Nutrient name mapping
nutrient_mapping = {
    "Vitamin A, RAE": "Vitamin A",
    "Vitamin B6": "Vitamin B6",
    "Vitamin B9": "Vitamin B9",
    "Vitamin B-12": "Vitamin B12",
    "Vitamin C, total ascorbic acid": "Vitamin C",
    "Vitamin D (D2 + D3)": "Vitamin D",
    "Vitamin E (alpha-tocopherol)": "Vitamin E",
    "Vitamin K (phylloquinone)": "Vitamin K",
    "Calcium, Ca": "Calcium",
    "Magnesium, Mg": "Magnesium",
    "Potassium, K": "Potassium",
    "Selenium, Se": "Selenium",
    "Zinc, Zn": "Zinc",
    "Iron, Fe": "Iron"
}


default_units = {
        "Vitamin A": {"unit": "mcg"},
        "Vitamin B6": {"unit": "mg"},
        "Vitamin B9": {"unit": "mcg"},
        "Vitamin B12": {"unit": "mcg"},
        "Vitamin C": {"unit": "mg"},
        "Vitamin D": {"unit": "mcg"},
        "Vitamin E": {"unit": "mg"},
        "Vitamin K": {"unit": "mcg"},
        "Calcium": {"unit": "mg"},
        "Magnesium": {"unit": "mg"},
        "Potassium": {"unit": "mg"},
        "Selenium": {"unit": "mcg"},
        "Zinc": {"unit": "mg"},
        "Iron": {"unit": "mg"}
}

def extract_nutrients(data):
    nutrients_dict = {}

    for item in data["foodNutrients"]:
        nutrient_info = item.get('nutrient', {})
        nutrient_name = nutrient_info.get('name')
        nutrient_details = {
            'id': nutrient_info.get('id'),
            'amount': item.get('amount'),
            'unit': nutrient_info.get('unitName')
        }
        nutrients_dict[nutrient_name] = nutrient_details

    return nutrients_dict

def load_json_to_dict(file_path):
    try:
        with open(file_path, 'r') as file:
            # Load the JSON content into a dictionary
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File not found.")
        return None
    except json.JSONDecodeError:
        print("Error parsing JSON.")
        return None



def create_nutrition_dict(directory, nutrient_mapping, default_units):
    nutrition_dict = {}
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            ingredient_name = filename[:-5]
            file_path = os.path.join(directory, filename)
            ingredient_data = load_json_to_dict(file_path)
            if ingredient_data:
                nutrition_info = ingredient_data.get("foodNutrients", [])
                
                # Create a dictionary for each nutrient with value and unit
                nutrient_data = {}
                for nutrient_info in nutrition_info:
                    nutrient_name = nutrient_info["nutrient"]["name"]
                    simplified_name = nutrient_mapping.get(nutrient_name, nutrient_name)
                    if simplified_name in default_units:
                        nutrient_data[simplified_name] = {
                            "value": nutrient_info["amount"],
                            "unit": nutrient_info["nutrient"]["unitName"]
                        }

                # Add missing nutrients with a value of 0 and the default unit
                for nutrient in default_units:
                    if nutrient not in nutrient_data:
                        nutrient_data[nutrient] = {"value": 0, "unit": default_units[nutrient]["unit"]}

                nutrition_dict[ingredient_name] = nutrient_data
    return nutrition_dict



ingredient_nutrition_dict = create_nutrition_dict(directory, nutrient_mapping, default_units)

#print(ingredient_nutrition_dict)