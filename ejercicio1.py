## pedimos sus datos básicos
name= (input ("Ingrese su nombre: "))
docu= int (input ("Ingrese su documento de identidad: "))
if docu > 0:
    i = 1
    while (i <= 1):
        sal1= int (input("Ingrese el salario: "))
        dayT= int (input("Ingresar días trabajados: "))
        hourD= int (input("Ingresar horas extras diurnas: "))
        hourN= int (input("Ingresar horas extras nocturnas: "))
        pr= int (input("Ingrese valor del prestamo: "))
        sal2 = (sal1/30) * dayT
        if pr > sal2:
            print("Valor prestamo invalido")
        else:
            vhor= int((sal2/dayT)/8)
            ved= vhor*1.25
            ven= vhor*1.75
            salD= ved * hourD
            salN= ven * hourN
            tsal = sal2 - pr
            Tsal = int((tsal + salD + salN))
            print("Documento:", docu)
            print("Nombre:", name)
            print("Salario a pagar:", Tsal)
            i += 1
else:
    print("Salió del proceso")

...

    
    
