import json
'12.1'
json_file = 'products.json'
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)
for product in data['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product['available']:
        print("В наличии\n")
    else:
        print("Нет в наличии!\n")
'12.2'
json_file = 'products.json'
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)
name = input("Введите название продукта: ")
price = int(input("Введите цену: "))
weight = int(input("Введите вес: "))
available_input = input("Есть в наличии? (да/нет): ").strip().lower()
available = True if available_input == 'да' else False
new_product = {
    "name": name,
    "price": price,
    "available": available,
    "weight": weight
}
data['products'].append(new_product)
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("\nОбновленное содержимое файла:")
for product in data['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product['available']:
        print("В наличии\n")
    else:
        print("Нет в наличии!\n")
'12.3'
en_ru_dict = {}
with open('en-ru.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        parts = line.split('-')
        if len(parts) != 2:
            continue
        en_word = parts[0].strip()
        ru_meanings = parts[1].strip()


        ru_list = [ru.strip() for ru in ru_meanings.split(',')]

        for ru_word in ru_list:

            if ru_word in en_ru_dict:

                if en_word not in en_ru_dict[ru_word]:
                    en_ru_dict[ru_word].append(en_word)
            else:
                en_ru_dict[ru_word] = [en_word]
ru_en_dict = {}
for ru_word, en_words in en_ru_dict.items():
    unique_en_words = sorted(set(en_words))
    ru_en_dict[ru_word] = unique_en_words
sorted_items = sorted(ru_en_dict.items(), key=lambda item: item[0])

with open('ru-en.txt', 'w', encoding='utf-8') as f:
    for ru_word, en_words in sorted_items:
        line = f"{ru_word} – {', '.join(en_words)}\n"
        f.write(line)


