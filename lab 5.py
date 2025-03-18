'task 5.1'
N = int(input("kolvo slov: "))
result = ""
for i in range(N):
    word = input(f"vvedite slovo {i + 1}: ")
    result += word + " "
result = result.strip()
print("resultat:", result)
'task 5.2'
result = ""
while True:
    word = input("vvedite slovo (ili 'stop' ): ")
    if word.lower() == "stop":
        break
    result += word + " "
result = result.strip()
print("resultat:", result)
'task 5.3'
while True:
    word = input("vvedite slovo (ili 'stop' ): ")
    if word.lower() == "stop":
        break
    if 'f' in word:
        print("ogo! eto redkoe slovo!")
    else:
        print("eh, eto ne o4en redkoe slovo...")
'task 5.4'
import random
cor_ans = 0
wrong_ans = 0
while wrong_ans < 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    ans = int(input(f"{num1} + {num2} = "))

    if ans == num1 + num2:
        print("pravilno!")
        cor_ans += 1
    else:
        print("otvet nevern")
        wrong_ans += 1
print(f"end. prav otvet: {cor_ans}")