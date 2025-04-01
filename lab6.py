'task 6.1'
def delna3(n):
    return n % 3 == 0
num = int(input("4islo: "))
if delna3(num):
    print(f"{num} del na 3")
else:
    print(f"{num} ne del na 3")
'task 6.2'
def del100naui(uinput):
    return 100 / uinput
while True:
    uinput = input("vved chislo(ili stop)")
    if uinput.lower() == 'stop':
        break
    try:
        uinput=float(uinput)
        res=del100naui(uinput)
        print(f"res delen 100 na {uinput} = {res}")
    except ValueError:
        print("oshibka: ne chislo")
    except ZeroDivisionError:
        print("oshibka: del na 0")
'task 6.3'
def magicdate(day,mon,year):
    return day * mon == year % 100
dateinput= input("vvedite daty dd.mm.gggg: ")
day,mon,year = map(int ,dateinput.split('.'))
if magicdate(day,mon,year):
    print("magic")
else:
    print("ne magic")
'task 6.4'
def lucktick(ticknum):
    hlen = len(ticknum) // 2
    fhsum = sum(int(dig) for dig in ticknum[:hlen])
    shsum = sum(int(dig) for dig in ticknum[hlen:])
    return fhsum == shsum
ticknum = input("vved n bileta: ")
if len(ticknum) % 2 != 0:
    print("nom bil soderj 4etn kolvo cifr")
else:
    if lucktick(ticknum):
        print("schasl")
    else:
        print("ne schastl")



