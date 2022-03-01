name= (input ("Ingrese su nombre: "))
docu= int (input ("Ingrese su documento de identidad: "))
if docu > 0:
    i = 1
    while (i <= 1):
        sal= int (input("ingrese el salario: "))
        vhr= (sal/30)/8
        hed= vhr*1.25
        hen= vhr*1.45
        #hourD= int (input("Ingresar horas extras diurnas: "))
        #hourN= int (input("Ingresar horas extras nocturnas: "))
        pr= int (input("Prestamos: "))
        Tsal = (sal + hed + hen + pr)
        print("Nombre:", name)
        print("Documento:", docu)
        print("Salario a pagar:", Tsal)
        i += 1
else:
    print("Salio del proceso")

    

    
    