import os
import json

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


RDA = {
    "men": {
        "Vitamin A": {"value": 900, "unit": "mcg"},
        "Vitamin B6": {"value": 1.3, "unit": "mg"},
        "Vitamin B9": {"value": 400, "unit": "mcg"},
        "Vitamin C": {"value": 90, "unit": "mg"},
        "Calcium": {"value": 1000, "unit": "mg"},
        "Iron": {"value": 8, "unit": "mg"},

    },
    "women": {
        "Vitamin A": {"value": 700, "unit": "mcg"},
        "Vitamin B6": {"value": 1.3, "unit": "mg"},
        "Vitamin B9": {"value": 400, "unit": "mcg"},
        "Vitamin C": {"value": 75, "unit": "mg"},
        "Calcium": {"value": 1000, "unit": "mg"},
        "Iron": {"value": 18, "unit": "mg"},

    }
}

directory = "backend/Data"

# Desired nutrients based on RDA
desired_nutrients = {
    "Vitamin A, RAE": {"unit": "mcg"},
    "Vitamin A, IU": {"unit": "mcg"},
    "Vitamin B6": {"unit": "mg"},
    "Vitamin B9": {"unit": "mcg"},
    "Vitamin B-12": {"unit": "mcg"},
    "Vitamin C, total ascorbic acid": {"unit": "mg"},
    "Vitamin D (D2 + D3)": {"unit": "mcg"},
    "Vitamin E (alpha-tocopherol)": {"unit": "mg"},
    "Vitamin K (phylloquinone)": {"unit": "mcg"},
    "Calcium, Ca": {"unit": "mg"},
    "Iron, Fe": {"unit": "mg"}
}


def create_nutrition_dict(directory, desired_nutrients):
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
                    if nutrient_name in desired_nutrients:
                        nutrient_data[nutrient_name] = {
                            "value": nutrient_info["amount"],
                            "unit": nutrient_info["nutrient"]["unitName"]
                        }

                # Add missing nutrients with a value of 0 and the appropriate unit
                for nutrient in desired_nutrients:
                    if nutrient not in nutrient_data:
                        nutrient_data[nutrient] = {"value": 0, "unit": desired_nutrients[nutrient]["unit"]}

                nutrition_dict[ingredient_name] = nutrient_data
    return nutrition_dict

ingredient_nutrition_dict = create_nutrition_dict(directory, desired_nutrients)

