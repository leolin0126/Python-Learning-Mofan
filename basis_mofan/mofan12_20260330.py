# def函数中的默认参数
def sale_car(price, colour, brand, second_hand):
    print('price:',price,
          'colour:',colour,
          'brand:',brand,
          'second_hand:',second_hand)
sale_car(1000,'red','凯美瑞',"True")
# 为def函数中的参数设置默认值
def sale_car2(price2=5000, colour2='gray', brand2='福克斯', second_hand2='True'):
    print('price:',price2,
          'colour:',colour2,
          'brand:',brand2,
          'second_hand:',second_hand2)
sale_car2(5000)
sale_car2(25000, colour2='white')
sale_car2(20000000, colour2='red', brand2='Ferrari')
