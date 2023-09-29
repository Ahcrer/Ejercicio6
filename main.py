n1 = float(input("Introduce tu primer número: ") )
n2 = float(input("Introduce tu segundo número: ") )

opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los dos números
    5) Cambiar los números elegidos
    6) Exponente de un número
    0) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print("\nResultado: La suma de ",n1,"+",n2," es igual a: ",n1+n2)
    elif opcion == 2:
        print("\nResultado: La resta de ",n1,"-",n2,"es igual a: ",n1-n2)
    elif opcion == 3:
        print("\nResultado: El producto de ",n1,"*",n2," es igual a: ",n1*n2)
    elif opcion == 4:
        print("\nResultado: La división de ",n1,"/",n2," es igual a : ", n1/n2)
    elif opcion == 5:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
    elif opcion == 6:
        print("\nResultado: El numero: ",n1," exponenciado a la: ",n2," es igual a: ", n1**n2)
    elif opcion == 0:
        break
    else:
        print("Opción incorrecta")