'task 4.1'
passw = input("parol")
conf_passw = input("podtv parol")
if passw == conf_passw:
    print("priniat")
else:
    print("ne priniat")
'task 4.2'
seat_number = int(input("vod nomera mesta: "))
if 1 <= seat_number <= 36: #plac
    if seat_number % 2 == 0:
        if seat_number <= 18:
            print("nijn mest")
        else:
            print("vehn mest")
    else:
        if seat_number <= 18:
            print("verhn mest")
        else:
            print("nijn mest")
else:
    if 37 <= seat_number <= 54: #kype
        if seat_number % 2 == 0:
            print("bok mest")
        else:
            print("nijn mest")
    else:
        print("neverno")
'task 4.3'
year = int(input("god: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"godd {year} - visok")
else:
    print("ne visok")
'task 4.4'
color1 = input("perv cvet(krasn , sin , jelt): ").strip().lower()
color2 = input("vtor cvet (krasn , sin , jelt): ").strip().lower()
if (color1 == "krasn" and color2 == "sin") or (color1 == "sin" and color2 == "krasn"):
    print("fiolet")
elif (color1 == "krasn" and color2 == "jelt") or (color1 == "jelt" and color2 == "krasn"):
    print("oranj")
elif (color1 == "sin" and color2 == "jelt") or (color1 == "jelt" and color2 == "sin"):
    print("zelen")
else:
    print("oshibka")




