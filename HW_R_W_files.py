import pprint
def reader(files):# директорию файла подаем в виде аргумента функции, что б можно было вызывать с любым файлом
    with open(files,'r',encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            name_dish = line.strip()
            count_ingridient = int(file.readline())
            ingridients = []
            for i in range(count_ingridient):
                name_ingridient = file.readline().strip()
                ingredient_name, quantity, measure  = name_ingridient.split(' | ')
                ingridients.append(
                    {'ingredient_name':ingredient_name,
                     'quantity':quantity,
                     'measure':measure}
                     )
            cook_book[name_dish] = ingridients
            file.readline()
        return cook_book
#print (reader('recipes.txt')) # для проверки с файлом 'recipes.txt'
pprint.pprint (reader('recipes.txt'),width=50, sort_dicts=False)
def order_formation(list_dish, person):#Используем функцию reader возвращающую готовый cook_book
    list_ingridient = {}
    person = int(person)
    for dish in list_dish:
        ingridients = reader('recipes.txt')[dish] #вызываем готовый  cook_book из файла 'recipes.txt'
        for ingridient in ingridients:
            name, quantity, measure = ingridient['ingredient_name'],int(ingridient['quantity']), ingridient['measure']
            if name not in list_ingridient.keys():
                list_ingridient[name] = {
                    'measure': measure,
                    'quantity':quantity*person
                    }
            else:
                list_ingridient[name] = {
                    'measure': measure,
                    'quantity':list_ingridient[name]['quantity'] + quantity*person
                    }
    return list_ingridient
       
pprint.pprint (order_formation(['Омлет','Утка по-пекински'], 4),width=50, sort_dicts=False)# для проверки
