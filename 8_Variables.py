print("\nHola que tal soy un programa que te pide 8 numeros enteros y te los eleva al cubo\n")

e = input("¿Desea Utilizarme? ")

if e == 'no':
    print("\nEntonces Bye")
    exit()

if e == 'No':
    print("\nEntonces Bye")
    exit()

if e == 'NO':
    print("\nEntonces Bye")
    exit()

print("\n¿",e,"?", "Muy bien, Empezemos\n")

print("\n..:Acontinuacion digite los numeros enteros a utilizar:..\n")

e1 = int(input("Digite el #1 -> "))
e2 = int(input("Digite el #2 -> "))
e3 = int(input("Digite el #3 -> "))
e4 = int(input("Digite el #4 -> "))
e5 = int(input("Digite el #5 -> "))
e6 = int(input("Digite el #6 -> "))
e7 = int(input("Digite el #7 -> "))
e8 = int(input("Digite el #8 -> "))

print("")

if e1:
    r1 = e1 * e1 * e1
    print("#1 =",r1)

if e2:
    r2 = e2 * e2 * e2
    print("#2 =",r2)

if e3:
    r3 = e3 * e3 * e3
    print("#3 =",r3)

if e4:
    r4 = e4 * e4 * e4
    print("#4 =",r4)

if e5:
    r5 = e5 * e5 * e5
    print("#5 =",r5)

if e6:
    r6 = e6 * e6 * e6
    print("#6 =",r6)

if e7:
    r7 = e7 * e7 * e7
    print("#7 =",r7)

if e8:
    r8 = e8 * e8 * e8
    print("#8 =",r8)

print("\nGracias por Utilizarme Bye")