'''
En una tienda de descuento se efectúa una promoción en la cual se hace un descuento sobre el valor de la compra total
según el color de la bolita que el cliente saque al pagar en caja. Si la bolita es de color blanco no se le hará descuento alguno,
si es verde se le hará un 10% de descuento, si es amarilla un 25%, si es azul un 50% y si es roja un 100%. Determinar la cantidad final
que el cliente deberá pagar por su compra. se sabe que solo hay bolitas de los colores mencionados.

blanco descuento = 0
verde descuento = 0.10
amarilla descuento = 0.25
azul descuento = 0.50
roja descuento = 1

'''
valor_compra = float(input("Ingrese el valor de la compra: "))
bolita = int(input("Ingrese el color de la bolita que le salió:\n1.Blanco\n2.Verde\n3.Amarillo\n4.Azul\n5.Roja\nOpción: "))

if bolita == 1:
  #Bolita Blanca sin descuento
  print(f"Sigue intentando! En estos momentos no tienes descuento. El valor de la compra es: {valor_compra}")
elif bolita == 2:
  #Bolita Verde descuento del 10%
  total = valor_compra * 0.90
  print(f"El valor final de la compar es: {total}")
elif bolita == 3:
  #Bolita Amarilla descuento del 25%  
  total = valor_compra * 0.75
  print(f"El valor final de la compar es: {total}")
elif bolita == 4:
  #Bolita Azul descuento del 50%
  total = valor_compra * 0.50
  print(f"El valor final de la compar es: {total}")
elif bolita == 5:
  #Bolita Roja descuento del 100% Compra Gratis
  total = valor_compra * 0
  print(f"El valor final de la compar es: {total} ES GRATIS!!!")
else:
  print("Introduce un valor entre el 1 y 5!")