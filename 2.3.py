n = int(input("Укажите начальную цену акций: "))
k = int(input("Укажите процент, на который ежегодно возрастает цена акций: "))
#print("Новая цена акций: ", n*(n+k/12)*12, "$")*
print("Новая цена акций: ", ((n*(n+k))**12)/10000, "$")