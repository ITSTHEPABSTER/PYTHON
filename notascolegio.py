nota=float(input("¿Qué nota has sacado?: "))
if nota>=10:
    print("Has sacado una NOTAZA!")
elif nota>=9:
    print("Has sacado un sobresaliente!")
elif nota>=7:
    print("Has sacado un notable!")
elif nota>=5:
    print("Has aprobado!")
elif nota <5 and nota > 0:
    print("Has suspendido :( ")
elif nota<=0:
    print("Eres gilipollas ")
    
