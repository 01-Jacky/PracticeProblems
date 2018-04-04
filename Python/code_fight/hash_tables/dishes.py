def groupingDishes(dishes):
    ingredient_map = {}

    # Get the ingredient -> dishes mapping
    for dish in dishes:
        dish_name = dish[0]
        for ingredient in dish[1:]:
            if ingredient in ingredient_map:
                ingredient_map[ingredient].add(dish_name)
            else:
                ingredient_map[ingredient] = set()
                ingredient_map[ingredient].add(dish_name)

    # Get rid of all the ingredient that don't have more than 1 dish
    ingredient_map_more_than_one = {}
    for ingredient, dish_list in ingredient_map.items():
        if len(dish_list) > 1:
            ingredient_map_more_than_one[ingredient] = dish_list

    sorted_results = []
    for ingredient, dish_set in sorted(ingredient_map_more_than_one.items()):
        tmp = [ingredient]
        tmp.extend(sorted(list(dish_set)))
        sorted_results.append(tmp)

    return sorted_results



dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
          ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
          ["Quesadilla", "Chicken", "Cheese", "Sauce"],
          ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

for x in groupingDishes(dishes):
    print(x)
