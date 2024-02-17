# ██████╗  █████╗ ██╗  ██╗ █████╗ ██████╗ ██╗██████╗ 
# ██╔══██╗██╔══██╗██║  ██║██╔══██╗██╔══██╗██║██╔══██╗
# ██████╦╝███████║███████║██║  ██║██║  ██║██║██████╔╝
# ██╔══██╗██╔══██║██╔══██║██║  ██║██║  ██║██║██╔══██╗
# ██████╦╝██║  ██║██║  ██║╚█████╔╝██████╔╝██║██║  ██║
# ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/baxa_akee_2602



print('HELLO!')
name_book = input('Enter the name of book: \n')
cost_book = int(input('How much did you buy the book for? ($) \n'))
percent_book = int(input('What percentage do you want to earn? (%) \n'))

overal_percent = 100 + percent_book
per = cost_book*overal_percent
total = int(per/100)


print(f'You need to sell the {name_book} book for ${total}')

a = int(input('How much money do you want to profit? ($)\n'))

clear = cost_book*percent_book
profit = int(clear/100)

amount = a//profit

print(f'you have to sell {amount} books for making ${a} profit!')
