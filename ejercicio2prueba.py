meta=30
turno=1
import time
import random
j1=0
j2=0
while j1<=30 and j2<=30:
    if turno %2==0:
        print("turno de J1")
        time.sleep(1)
        dado=random.randint(1,6)
        j1=j1+dado
        turno=turno+1
        print("J1 sacó: ",dado)
        print("avanza hasta la casilla ",j1)
    else:
        print("turno de J2")
        time.sleep(1)
        dado=random.randint(1,6)
        j2= j2+dado
        turno=turno+1
        print("J2 sacó: ",dado)
        print("avanza hasta la casilla ",j2)

