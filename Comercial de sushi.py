import os
import time
Limpieza_Pantalla = "cls"
boleta = 0
pika = 4500
otaku = 5000
pulpo = 5200
anguila = 4800
rolls = 0
menu = 0
os.system(Limpieza_Pantalla)
while menu < 4:
    time.sleep(2)
    print("Bienvenido a !Kentakmi Sushi rolls¡\n")
    print("Ingresa la opcion de tu preferencia en esta compra\n")
    print(f"1.- Pikachu Roll: {pika}")
    print(f"2.- Otaku Roll: {otaku}")
    print(f"3.- Pulpo Venesoso Roll: {pulpo}")
    print(f"4.- Anguila Electrica Roll: {anguila}")
   
    try:
        rolls = int(input("Ingrese la opción que desea comprar: "))
        respuesta = int(input(F"Has agregado {pika} a tu compra"))
        if respuesta == 1:
            print(f"Has agregado {pika} a tu compra")
            
    except ValueError:
        print("Ingrese el número de la opción para realizar la compra")

    try:
        respuesta = int(input(f"Has agregado {otaku} a tu compra"))
        if respuesta == 2:
            print(f"Has agregado {otaku} a tu compra")
        else:
            print(f"Has salido de la sección de ROLLS.")
            break
    except ValueError:
        print("Ingrese el número de la opción para realizar la compra")