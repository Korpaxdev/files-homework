def create_cooking_book(recipes_file):
    cooking_book = dict()
    with open(recipes_file, encoding='utf-8') as file:
        for line in file:
            recipe = line.strip()
            cooking_book[recipe] = []
            count = int(file.readline())
            for i in range(count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                cooking_book[recipe].append(
                    {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})

            file.readline()
    return cooking_book


RECIPES_FILE = 'recipes.txt'

book = create_cooking_book(RECIPES_FILE)
print(book)


def get_shop_list_by_dishes(dishes, person_count):
    ingredients = dict()
    for dish in dishes:
        if dish not in book:
            raise AttributeError(f"Атрибута {dish} нет в списке рецептов. См. файл рецептов - {RECIPES_FILE}")
        for i in book[dish]:
            ingredient_name, quantity, measure = i.values()
            if ingredient_name not in ingredients:
                ingredients[ingredient_name] = {'measure': measure, 'quantity': quantity * person_count}
            else:
                ingredients[ingredient_name]['quantity'] += quantity * person_count
    return ingredients


print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
