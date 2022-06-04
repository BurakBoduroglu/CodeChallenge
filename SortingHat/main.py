import time
import random

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
houses = ["GRYFFINDOR!!!!!!",
          "RAVENCLAW!!!!!!",
          "HUFFLEPUFF!!!!!!",
          "SLYTHERIN!!!!!!"
          ]

def check(answer):
    global gryffindor
    global ravenclaw
    global hufflepuff
    global slytherin

    if answer == ("a" or "A"):
        gryffindor += 1
    elif answer == ("b" or "B"):
        ravenclaw += 1
    elif answer == ("c" or "C"):
        hufflepuff += 1
    elif answer == ("d" or "D"):
        slytherin += 1
    else:
        print("Geçersiz işlem.\n")

print("SEÇMEN ŞAPKA")
answer_1 = input("\nKendini nasıl tanımlarsın?"
                 "\na) Cesur"
                 "\nb) Özenli"
                 "\nc) Sadık"
                 "\nd) Hırslı\n")
check(answer_1)

answer_2 = input("\nHafta sonları ne yaparsın?"
                 "\na) Maceraya atılırım"
                 "\nb) Ödev yaparım"
                 "\nc) Arkadaşlarım ve ailem ile olurum."
                 "\nd) Oyunda düşmanlar ile savaşırım.\n")
check(answer_2)

answer_3 = input(
    "\nKaranlık Lord okulunuzu istila edecek olsa ne yapardınız?"
    "\na) Savaşırım "
    "\nb) Savunmak savunma sanatları kitabına bakarım. "
    "\nc) Arkadaşlarıma katılırım. "
    "\nd) Ona yardım ederim.\n")
check(answer_3)

print("\nSeçme Şapka karar veriyor...")
time.sleep(1)
if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print("GRYFFINDOR!!!!!!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("RAVENCLAW!!!!!!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
    print("HUFFLEPUFF!!!!!!")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
    print("SLYTHERIN!!!!!!")
else:
    print("Seçmek çok zor.")
    print(random.choice(houses))

