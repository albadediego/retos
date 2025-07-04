estudiantes = {} #Creamos diccionario vacio
continuar = True #Inicializamos el continuar a True

#Funcion para agregar estudiantes
def agregar_estudiantes():
    #Se pide al usuario el nombre del estudiante
    nombre = input("Ingrese nombre de estudiante: ")
    #Se crea una lista de notas vacia
    notas = []
    #Se inicializa el contador a 0
    contador = 0

    #Se pide las notas al usuario 3 veces, un numero entre 0 y 10 y lo añadimos a notas
    while contador < 3:
        nota = float(input("Ingrese una nota (entre 0 y 10): "))
        
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            contador += 1
        else:
            print("La nota debe de estar entre 0 y 10")
    #Se añaden las notas al diccionario
    estudiantes[nombre] = notas
    print("Se ha creado un nuevo estudiante")

#Funcion para quitar estudiantes
def quitar_estudiantes():
    #Se pide al usuario el nombre del estudiante a eliminar
    nombre = input("Ingrese nombre de estudiante a eliminar: ")
    #Se comprueba que el nombre esta en la lista y en caso positivo, se elimina
    if nombre in estudiantes:
        del estudiantes[nombre]
        print("Estudiante eliminado")
    else: 
        print("Estudiante no encontrado")

#Funcion para mostrar los estudiantes aprobados con media de 6 o mas
def mostrar_estudiantes_aprobados():
    #Se recorre el diccionario para coger las notas de los estudiantes y hacer la media
    for nombre, notas in estudiantes.items():
        media = sum(notas) / 3
        #Si la nota es 6 o mas se muestra por pantalla
        if media >= 6:
            print(f"La nota media de {nombre} es: {media:.2f}")

#Funcion para buscar estudiantes
def buscar_estudiante():
    #Se pide al usuario el nombre del estudiante que quiere buscar
    nombre = input("Escriba el nombre del estudiante que quiere buscar: ")
    #Se comprueba que el nombre esta en el diccionario y se muestran el nombre y la media
    if nombre in estudiantes:
        notas = estudiantes[nombre]
        media = sum(notas) / 3
        print(f"La media de {nombre} es: {media:.2f}")
    else:
        print("Estudiante no encontrado")

#Funcion para mostrar todos los estudiantes
def mostrar_todos():
    #Se recorre el diccionario y se imprime por pantalla todos los datos (nombre, notas y media)
    for nombre, notas in estudiantes.items():
        media = sum(notas) / 3
        print(f"{nombre}: \n Las notas son: {notas} \n La media es: {media:.2f}")

#Se usa un mientras para que el programa continue hasta que se elige la opcion numero 6
while continuar:
    programa = int(input("Pulsa: \n" \
    "1: Agregar estudiantes \n" \
    "2: Quitar estudiantes \n" \
    "3: Mostrar estudiantes aprobados \n" \
    "4: Buscar estudiante \n" \
    "5: Mostrar todos los estudiantes \n" \
    "6: Salir: "))

    if programa == 1:
        agregar_estudiantes()

    elif programa == 2:
        quitar_estudiantes()

    elif programa == 3:
        mostrar_estudiantes_aprobados()

    elif programa == 4:
        buscar_estudiante

    elif programa == 5:
        mostrar_todos()

    elif programa == 6:
        print("Fin del programa")
        break

    else:
        print("Opcion no valida")