# ------------- lesson 3 -------------
from os import listdir
from os.path import join, isfile, split

DIRECTORY_FILES = 'lessons_3_files'
YOUR_COPY_FILE_NAME = 'copy.txt'


def create_files_dict_from_directory(directory: str) -> dict:
    """
    DESCRIPTION:
        Функция создает dict из файлов лежащих в directory
    PARAMS:
        directory: строка директории, из которой необходимо сделать словарь
    RETURNS:
        Словарь формата: {'путь до файла': количество строк в файле}
    """
    files_names = [file for file in listdir(directory) if isfile(join(directory, file))]
    files_lines_count = dict()

    for name in files_names:
        file_path = join(directory, name)
        with open(file_path, encoding='utf-8') as file:
            files_lines_count[file_path] = 0
            for _ in file:
                files_lines_count[file_path] += 1
    return files_lines_count


def sort_dict_files(files: dict) -> dict:
    """
    DESCRIPTION
        Создает новый сортированный словарь из переданного files. Сортирует по значению ключей
    PARAMS:
        files: Словарь формата {key: value (типа int)}
    RETURNS:
        Отсортированный словарь типа {key: value}
    """
    sorted_files_count = dict()
    sorted_keys = sorted(files, key=lambda x: files[x])
    for k in sorted_keys:
        sorted_files_count[k] = files[k]
    return sorted_files_count


def create_empty_file(file_name: str) -> None:
    """
    DESCRIPTION:
        Создает пустой файл с именем file_name в корне проекта
    PARAMS:
        file_name: имя файла
    """
    with open(file_name, 'w+', encoding='utf-8') as f:
        f.write('')


def create_copy_file_from_files_dict(copy_file_name: str, files: dict) -> None:
    """
    DESCRIPTION:
        Создает в корне проекта файл с именем copy_file_name и копирует в него строки из файлов в словаре FILES
    PARAMS:
        copy_file_name: имя файла, который создается в корне проекта.
        files: словарь с файлами из которых нужно копировать строки.
    """
    create_empty_file(copy_file_name)
    for file_path, value in files.items():
        file_name = split(file_path)[-1]
        with open(file_path, encoding='utf-8') as f:
            with open(copy_file_name, 'a', encoding='utf-8') as copy_file:
                copy_file.write('ИМЯ ФАЙЛА: ' + file_name + '\n')
                copy_file.write('КОЛИЧЕСТВО СТРОК В ФАЙЛЕ: ' + str(value) + '\n')
                copy_file.writelines(f.readlines())
                copy_file.write('\n\n')


files_count = sort_dict_files(create_files_dict_from_directory(DIRECTORY_FILES))
create_copy_file_from_files_dict(YOUR_COPY_FILE_NAME, files_count)


# ------------- lessons 1-2 -------------
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
