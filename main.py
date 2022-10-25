shopping_list = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
    
}
print('Lista zakupów')
for shop, products in shopping_list.items(): 
    shop = shop.capitalize()
    products = ' '.join(products)
    roducts = products.title()


    print('Idę do', shop, 'i kupuję tam', products)
for i in shopping_list.values():
    x = len(i) + len(i)
    

print('W sumie kupuję', x, 'produktów')
#zmiana 1

