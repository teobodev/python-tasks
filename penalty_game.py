# ██████╗  █████╗ ██╗  ██╗ █████╗ ██████╗ ██╗██████╗ 
# ██╔══██╗██╔══██╗██║  ██║██╔══██╗██╔══██╗██║██╔══██╗
# ██████╦╝███████║███████║██║  ██║██║  ██║██║██████╔╝
# ██╔══██╗██╔══██║██╔══██║██║  ██║██║  ██║██║██╔══██╗
# ██████╦╝██║  ██║██║  ██║╚█████╔╝██████╔╝██║██║  ██║
# ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/baxa_akee_2602

# penalty game


import random

footbalerScore = 0
compScore = 0

komp_zarba = 0

while komp_zarba!=5 :
    a = input("\nWhich way do you kick: \nleft, middle, right\n")
    b = ["left", "middle", "right"]
    c = random.choice(b) 

    print("Kiiiiick")
    print("The computer jumped into the " + c)
    if a==c:
        print ("Saveeee")
        print("You: " + str(footbalerScore) + "\nComputer: " + str(compScore))
    elif a!="left" and a!="middle" and a!="right":
        print("Wrong shot!")
        print("You: " + str(footbalerScore) + "\nComputer: " + str(compScore))
    else:
        print("Goaaaaaaal") 
        footbalerScore += 1
        print("You: " + str(footbalerScore) + "\nComputer: " + str(compScore))

    q = input("\nWhich way will you jump?: \nleft, middle, right\n")
    w = ["left", "middle", "right"]
    e = random.choice(b) 

    komp_zarba += 1    

    print("Kiiiiick")
    print("The computer kicked to the " + e)

    if q==e:
        print ("Saveeeeee")
        print("You: " + str(footbalerScore) + "\nComputer: " + str(compScore))
    
    else:
        print("Goaaaaaaaaal") 
        compScore += 1
        print("You: " + str(footbalerScore) + "\nComputer: " + str(compScore))

print("\nGame over!")
if footbalerScore>compScore:
    print("Congratulations, you won ☻") 
elif footbalerScore<compScore:
    print("Unfortunately, you lost ♣")
else:
    print("It was a draw!")  
