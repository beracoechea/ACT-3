from ctypes.wintypes import INT
from os import system


def circulo():
    radio=float(input("INGRESE EL VALOR DE EL RADIO: "))
    area=radio*radio*3.1416
    print("EL AREA DEL CIRCULO ES: "+ str(area))
    print("\n")


def cuadrado():
    lado=float(input("INGRESE EL VALOR DE EL LADO: "))
    area=lado*lado
    print("EL AREA DEL CUADRADO ES: "+str(area))
    print("\n")

def triangulo():
    altura=float(input("INGRESE LA ALTURA DEL TRIANGULO: "))
    base=float(input("INGRESE LA BASE DEL TRIANGULO: "))
    area=base*altura
    area=area/2
    print("EL AREA DEL TRIANGULO ES: "+str(area))
    print("\n")


figura=int((input("SELECCIONE LA FIGURA A CALCULAR EL AREA\n[1]CIRCULO\n[2]CUADRADO]\n[2]TRIANGULO\n"))) 
if figura==1:
   circulo()
else :
 if figura==2:
    cuadrado() 
 else:
  if figura==3:
    triangulo()        
      

        
              
    





