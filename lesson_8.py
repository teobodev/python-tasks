import random

footbalerScore = 0
compScore = 0

komp_zarba = 0

while komp_zarba!=5 :
    a = input("\nQaysi tarafga tepasiz: \nchap, o'rta, o'ng\n")
    b = ["chap", "o'rta", "o'ng"]
    c = random.choice(b) 

    print("Zarbaaa")
    print("Kompyuter " + c + "ga otildi")
    if a==c:
        print ("Seyvvv")
        print("Siz: " + str(footbalerScore) + "\nKomp: " + str(compScore))
    elif a!="chap" and a!="o'rta" and a!="o'ng":
        print("Noto'g'ri zarba!")
        print("Siz: " + str(footbalerScore) + "\nKomp: " + str(compScore))
    else:
        print("Goool") 
        footbalerScore += 1
        print("Siz: " + str(footbalerScore) + "\nKomp: " + str(compScore))

    q = input("\nQaysi tarafga otilasiz?: \nchap, o'rta, o'ng\n")
    w = ["chap", "o'rta", "o'ng"]
    e = random.choice(b) 

    komp_zarba += 1    

    print("Zarbaaa")
    print("Kompyuter " + e + "ga tepdi")

    if q==e:
        print ("Seyvvv")
        print("Siz: " + str(footbalerScore) + "\nKomp: " + str(compScore))
    
    else:
        print("Goool") 
        compScore += 1
        print("Siz: " + str(footbalerScore) + "\nKomp: " + str(compScore))

print("\no'yin o'z nihoyasiga yetdi!")
if footbalerScore>compScore:
    print("Tabriklaymiz, siz g'olib buldingiz☻") 
elif footbalerScore<compScore:
    print("Afsuski, siz mag'lub buldingiz♣")
else:
    print("Durrang buldi!")  
