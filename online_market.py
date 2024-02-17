# ██████╗  █████╗ ██╗  ██╗ █████╗ ██████╗ ██╗██████╗ 
# ██╔══██╗██╔══██╗██║  ██║██╔══██╗██╔══██╗██║██╔══██╗
# ██████╦╝███████║███████║██║  ██║██║  ██║██║██████╔╝
# ██╔══██╗██╔══██║██╔══██║██║  ██║██║  ██║██║██╔══██╗
# ██████╦╝██║  ██║██║  ██║╚█████╔╝██████╔╝██║██║  ██║
# ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/baxa_akee_2602





# online market calculation!


print('HELLO! Welcome to our online market! \nPlease enter your name: ')
name = input('')

print(f'Dear {name},\nWhat do you want to buy from our online market? \n')

fruits = input("\napple, banana, mango, Kiwi\n")

soni = float(input('How many kg will you get:\n'))
o = 20
b = 25
a = 18
n = 23

_list = []

if fruits=="apple":
    total=float(soni*o)
    _list.append('apple')
    print(f'Total amount: {total}soum')
elif fruits=="banana":
    total=float(soni*b)
    _list.append('banana')
    print(f'Total amount: {total}soum')
elif fruits=="mango":
    total=float(soni*a)
    _list.append('mango')
    print(f'Total amount: {total}soum')
elif fruits=="Kiwi":
    total=float(soni*n)
    _list.append('Kiwi')
    print(f'Total amount: {total}soum')
else:
    print('We do not have such a product!')
something_else = input('Do you get anything else? (y/n) ')

while something_else == 'y':
    print('Nima xarid qilasiz?')
    fruits = input("\napple, banana, mango, Kiwi\n")
    soni = float(input('How many kg will you get:\n'))
    if fruits=="apple":
     total += float(soni*o)
     _list.append('apple')
     print(f'Total amount: {total}soum')
    elif fruits=="banana":
     total += float(soni*b)
     _list.append('banana')
     print(f'Total amount: {total}soum')
    elif fruits=="mango":
     total += float(soni*a)
     _list.append('mango')
     print(f'Total amount: {total}soum')
    elif fruits=="Kiwi":
     total += float(soni*n)
     _list.append('Kiwi')
     print(f'Total amount: {total}soum')
    else:
     print('We do not have such a product!')
    something_else = input('Do you get anything else? (y/n) ')
if something_else == 'n':
    print('What you bought:')
    for item in _list:
        print(item)
    print(f'Total amount {total}soum.\nThank you for your purchase!')
