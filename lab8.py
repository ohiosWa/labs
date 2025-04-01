'task 8.1'
coandca = {
    "russia": "moscow",
    "usa": "vashington",
    "france": "paris",
    "italy": "rim",
}
print("spisok:")
for countr,capit in coandca.items():
    print(f"{countr}: {capit}")
country_input = input("vved nazv strani :")
capital = coandca.get(country_input)
if capital:
    print(f"stolica {country_input}: {capit}")
else:
    print("strana ne naiden")
sort_countr=dict(sorted(coandca.items()))
print("stani v alfavit poriadke: ")
for countr,capit in sort_countr.items():
    print(f"{countr}: {capit}")
'task 8.2'
letter_values = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1,
    'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Й': 4, 'Ы': 4,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Ф': 10, 'Щ': 10, 'Ъ': 10
}
user_word = input("vvedite slovo: ").upper()
total_value = sum(letter_values.get(letter, 0) for letter in user_word)
print(f"stoimost slova'{user_word}': {total_value} ")
'task 8.3'
studlang={
    "ivanov": {"rus", "eng", "jap"},
    "vovel": {"rus", "france"},
    "kozakov": {"eng", "ger"},
    "zybaref": {"rus", "jap", "fin"},
}
alllang = set()
for lang in studlang.values():
    alllang.update(lang)
sortlang = sorted(alllang)
print("razl iaziki sredi stud: ", sortlang)
studknowjap = [stud for stud , lang in studlang.items() if "jap" in lang]
print("stud,znaush jap:", studknowjap)
