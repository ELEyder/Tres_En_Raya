#Programa creado por Eyder Huayta para Cisco - 2020
print('Bienvenido a el famoso juego: "¡Tres en raya!"');input("Pulsa ENTER para continuar")
tablero= [[1,2,3],[4,"X",6],[7,8,9]]
lugares=[1,2,3,4,6,7,8,9]
game=0
from random import choice

def cambio(a):
    if a == 1:tablero[0][0]="o"; 
    elif a == 2:tablero[0][1]="o"; 
    elif a == 3:tablero[0][2]="o"; 
    elif a == 4:tablero[1][0]="o"; 
    elif a == 6:tablero[1][2]="o"; 
    elif a == 7:tablero[2][0]="o"; 
    elif a == 8:tablero[2][1]="o"; 
    elif a == 9:tablero[2][2]="o";
    lugares.remove(a)
def pc(a):
    if a == 1:tablero[0][0]="X"; 
    elif a == 2:tablero[0][1]="X"; 
    elif a == 3:tablero[0][2]="X"; 
    elif a == 4:tablero[1][0]="X"; 
    elif a == 6:tablero[1][2]="X"; 
    elif a == 7:tablero[2][0]="X"; 
    elif a == 8:tablero[2][1]="X"; 
    elif a == 9:tablero[2][2]="X";
    lugares.remove(a)
def final():
    global game
    if (tablero[0][0]=="o" and tablero[0][1]=="o" and tablero[0][2]=="o")or(tablero[0][0]=="o" and tablero[1][0]=="o" and tablero[2][0]=="o"):print("\nGanaste");game=1
    elif (tablero[2][0]=="o" and tablero[2][1]=="o" and tablero[2][2]=="o")or(tablero[0][2]=="o" and tablero[1][2]=="o" and tablero[2][2]=="o"):print("\nGanaste");game=1
    elif(tablero[0][0]=="X" and tablero[0][1]=="X" and tablero[0][2]=="X")or(tablero[0][0]=="X" and tablero[1][0]=="X" and tablero[2][0]=="X"):print("\nPerdiste");game=1
    elif(tablero[2][0]=="X" and tablero[2][1]=="X" and tablero[2][2]=="X")or(tablero[0][2]=="X" and tablero[1][2]=="X" and tablero[2][2]=="X"):imprimir(); print("\nPerdiste");game=1
    elif(tablero[0][0]=="X" and tablero[1][1]=="X" and tablero[2][2]=="X")or(tablero[0][2]=="X" and tablero[1][1]=="X" and tablero[2][0]=="X"):imprimir(); print("\nPerdiste");game=1
    elif(tablero[0][1]=="X" and tablero[1][1]=="X" and tablero[2][1]=="X")or(tablero[1][0]=="X" and tablero[1][1]=="X" and tablero[1][2]=="X"):imprimir(); print("\nPerdiste");game=1
def imprimir():
    global tablero
    for a in [0,1,2]:
        print("\n+ ------- + ------- + ------- +")
        for i in tablero[a]:
            print("     ",i,end=" ")
    print()
while game==0:
    imprimir();elec=int(input("\nIngresa tu movimiento:\n"))
    for i in tablero:
        for a in i:
            if a == elec:
               cambio(a);imprimir();random=choice(lugares);pc(random);final()
    if sum(lugares)==0 :imprimir();print("Empate");game+=1           
#Quise hacer el reto de menos de 50 lineas y por eso se ve tan mal el codigo, pero sirve :), perdon :c (¡Esta linea es la num 50!)
