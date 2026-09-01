sexo=input("[H]: Hombre / [M]: Mujer").upper()
edad=int(input("dame tu edad: "))

if sexo=="H" and edad>65:
    print("te jubilas")
elif sexo=="M" and edad>60:
    print("te jubilas") 
else:
    print("aun no te toca") 