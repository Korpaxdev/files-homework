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
