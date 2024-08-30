spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for spice in spicy_foods:
        name = spice['name']
        names.append(name)
    return names

# print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    spicy_food = []
    for spice in spicy_foods:
        if spice['heat_level'] > 5:
            spicy_food.append(spice)
    return spicy_food

# print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
   for item in spicy_foods:
        print(
            f"{item.get('name')} ({item.get('cuisine')}) | Heat Level: {'🌶' * item.get('heat_level') }")

# print(print_spicy_foods(spicy_foods))


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spice in spicy_foods:
        if spice['cuisine'] == cuisine:
            return spice
        
# print(get_spicy_food_by_cuisine(spicy_foods, 'Thai'))


def print_spiciest_foods(spicy_foods):
   for item in spicy_foods:
        if item.get("heat_level") > 5:
            print(
                f"{item.get('name')} ({item.get('cuisine')}) | Heat Level: {'🌶' * item.get('heat_level') }")

        
print(print_spiciest_foods(spicy_foods))



def get_average_heat_level(spicy_foods):
    numbers = []
    for spice in spicy_foods:
        number = spice['heat_level']
        numbers.append(number)
    return sum(numbers) / len(numbers)

# print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
