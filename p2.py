shopping_basket=list()
count=0
print("Shopping basket options choose one option")
print("1.Add item 0.exit")
option = int(input("enter one option"))
while option == 1:
    item = input("enter item")
    quntitity = int(input("enter the quantity:"))
    shopping_basket.append(quntitity)
    shopping_basket.append(item)
    ans = input("enter y to continue n to exit")
    if ans == 'n':
        break
def convert(s):
    init = iter(shopping_basket)
    res_dct = dict(zip(init,init))
    return res_dct
print(convert(shopping_basket))
for Key in convert(shopping_basket).keys():
    price = float(input("enter price of item"))
    GST = 12 / 100
    GST_amt = (price * GST) / 100
    total = 0
    total += quntitity * price + GST_amt
    print(total)

if(option!=0):
    ans = input(print('do you want to remove any item press y for yes and n for no'))
    if ans == 'y':
        if shopping_basket._len_() > 0:
            item = input('Enter item')
            shopping_basket.remove(item)
            print('item removed')
            print(shopping_basket)
        else:
            print('Thank you vist again!!!')
exp=input(print('Rate your experiance'))

if(option==0):
    print('Thank you vist again!!!')