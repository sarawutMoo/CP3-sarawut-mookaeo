def vatCalclate(totalPrice):
    result = totalPrice +(totalPrice*7/100)
    return result
price = int(input('Price is :'))
print('vat include : ',int(vatCalclate(price)))