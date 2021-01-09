#input user and pass for login
usernameInput = input('Username :')
passwordInput = input('Password :')
# Check user amd pass if correct ,continue but if incorrect ,end
if usernameInput  == 'admin'  and passwordInput == '1234':
    priceBTC = 35000                                # set price product
    priceETH = 1236
    print('      Wellcome to ')
    print('----- Crypto Shop -----')
    print('1. Bitcoin   :   ',priceBTC, '$')
    print('2. Ethereum  :   ',priceETH, ' $')
    userSelected = int(input('Add to cart >>'))     # select product
    if userSelected == 1:
        qtyBTC = int(input('Quantity is : '))       # input quantity
        Fee = 0.0025
        Value = (qtyBTC + (qtyBTC * Fee))*priceBTC  # Cal value
        print('------Total amount------')
        print('Bitcoin Value is ',Value ,'$')
    elif userSelected == 2:
        qtyETH = int(input('Quantity is : '))       # input quantity
        Fee = 0.0025
        Value = (qtyETH + (qtyETH * Fee))*priceETH  # Cal value
        print('------Total amount------')
        print('Ethereum Value is ', Value,'$')
    else:
        print('You select incorrect !!!')           # if select other choice
else:
    print('Username or Password incorrect !!!')


