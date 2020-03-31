def Toplama(x, y):
	return x + y

def Cikarma(x, y):
	return x - y

def Carpma(x, y):
	return x * y

def Bolme(x, y):
	return x / y

print("Lütfen aşağıdakilerden birisini seçiniz.")
print("")
print("1 - Toplama")
print("2 - Çıkarma")
print("3 - Çarpma")
print("4 - Bölme")
print("")

secimSonuc = input()

sayiBir = int(input("Birinci sayı: "))
sayiIki = int(input("İkinci sayı: "))

if secimSonuc == '1':
	print(sayiBir, '+', sayiIki, '=', 
		Toplama(sayiBir, sayiIki))
elif secimSonuc == '2':
	print(sayiBir, '-', sayiIki, '=', 
		Cikarma(sayiBir, sayiIki))
elif secimSonuc == '3':
	print(sayiBir, '*', sayiIki, '=', 
		Carpma(sayiBir, sayiIki))	
elif secimSonuc == '4':
	print(sayiBir, '/', sayiIki, '=', 
		Bolme(sayiBir, sayiIki))
else:
	print('Gecersiz işlem.')
