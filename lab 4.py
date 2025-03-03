'task 4.1'
passw = input("parol")
conf_passw = input("podtv parol")
if passw == conf_passw:
    print("priniat")
else:
    print("ne priniat")
'task 4.2'
def proverka_nomera_mesta(seat_num):
    if seat_num < 1 or seat_num > 54:
        return "neverno, vsego 54 mesta v vagone"
    if seat_num <= 36:
        if seat_num % 2 == 1:
            return "nijn mesto , kype"
        else:
            return "verh mesto , kype"
    else:
        if seat_num % 2 == 1:
            return "nijn mesto , bokovoe"
        else:
            return "verh mesto , bokovoe"
seat_num = int(input("vash nomer: "))
seat_t = proverka_nomera_mesta(seat_num)
print(seat_t)
'task 4.3'
def visokosnii_li_god(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("vvedite god: "))
if visokosnii_li_god(year):
    print(f"god {year} - visokos")
else:
    print("ne visokos")
'task 4.4'
def smeshanie_cvetov(color1,color2):
    color_mix = {
        ("krasn", "sin"): "fiol",
        ("krasn", "jelt"): "oranj",
        ("sin", "jelt"): "zelen",
    }
    colors = (color1, color2)
    if colors in color_mix:
        return color_mix[colors]
    elif (color2, color1) in color_mix:
        return color_mix[(color2, color1)]
    else:
        return None
color1 = input("vved perv cvet: ").strip().lower()
color2 = input("vved vtor cvet: ").strip().lower()
valid_colors = ["krasn", "sin", "jelt"]
if color1 in valid_colors and color2 in valid_colors:
    sec_color = smeshanie_cvetov(color1, color2)
    print(f" {color1} + {color2} = {sec_color}")
else:
    print("oshibka")




