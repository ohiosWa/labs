'task 7.1'
num = [4,2,6,7,15]
unum = int(input("vved 4islo: "))
if unum in num:
    print("pozdrav, vi ugadali ")
else:
    print("net takogo chisla")
print("ishod spis: ", num)
print("vashe 4isl: ",unum)
'task 7.2'
list =[1,3,4,7,9,1]
povtor = set([x for x in list if list.count(x) > 1])
if povtor:
    print("povtor elem: ",povtor)
else:
    print("net povtor elem")
'task 7.3'
dweek= ("pon","vtor","sred","4etv","piatnc","subb","voskr")
wekndc= int(input("skolk vihodn na nedele vi hotite?"))
wekndd = dweek[-wekndc:]
workd = dweek[:-wekndc]
print("vih dni:",wekndd)
print("rab dni:",workd)
'task 7.4'
group_a = ["ivanov", "bobrkur", "semenov", "kyzminof", "bratishkinof", "semenyk", "lebedev", "nolimov", "rongov", "chefov"]
group_b = ["bekin", "buloven", "alexandrof", "nobel", "rogov", "trump", "buhov", "chirov", "slonikov", "ornik"]
team = tuple(group_a[:5]+group_b[:5])
print("gr a:", group_a)
print("gr b:", group_b)
print("sportteam:", team)
print("dlin kom:", len(team))
sortteam= sorted(team)
print("otsortir kom:", sortteam)
ivanovc = team.count("ivanov")
if ivanovc > 0:
    print(f"ivanov vhod v kom {ivanovc} raz")
else:
    print("ivanov ne vhodit v kom")