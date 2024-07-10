import funciones_edu as fn 

trabajadores = [
    "Juan perez", "maria garcia", "carlos lopez", "ana martinez", "pedro rodriguez",
    "laura hernandez", "miguel sanchez", "isable gomez", "francisco diaz", "elena fernandez"
]

sueldos_trabajadores = {}

while True:
    print("*-- Menu --*")
    print("0. Inizializar sueldos en 0")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

    opc = int(input("Seleccione una opcion: "))
    if opc == 0:
        for trabajador in trabajadores:
            sueldos_trabajadores = {trabajador : 0 for trabajador in trabajadores}

        print("--------------------------------------------")
        print("Sueldos inizializados correctamente")
        print("--------------------------------------------")
    elif opc == 1:
        if not sueldos_trabajadores:
            print("----------------------------")
            print("primero inizialice su sueldo")
            print("----------------------------")
        else:
            sueldos_trabajadores = fn.asignar_sueldos(trabajadores)
    elif opc ==2:
        if sueldos_trabajadores:
            fn.clasificar_sueldos(sueldos_trabajadores)
        else:
            print("----------------------------")
            print("primero asigne sueldos")
            print("----------------------------")
    elif opc == 3:
        if sueldos_trabajadores:
            max_sueldo, min_sueldo, prom_sueldo, media_geometrica = fn.estadísticas_sueldos(sueldos_trabajadores)
            if max_sueldo is not None:
                print("--------------------------------------------")
                print("El sueldo mas alto es:", max_sueldo)
                print("El sueldo mas bajo es:", min_sueldo)
                print("El promedio de los sueldos es:", prom_sueldo)
                print("La media geometrica es:", media_geometrica)
                print("--------------------------------------------")
        else:
            print("----------------------------")
            print("primero asigne sueldos")
            print("----------------------------")
    elif opc == 4:
        if sueldos_trabajadores:
            fn.generar_reporte(sueldos_trabajadores)
        else:
            print("----------------------------")
            print("primero asigne sueldos")
            print("----------------------------")
    elif opc == 5:
        print("----------------------------")
        print("Saliendo del programa...")
        print("Desarrollado por Eduardo silva vergara")
        print("Mi rut es: 20.708.149-3")
        print("----------------------------")
        break
    else:
        print("------------------------------------------------")
        print("por favor seleccione un opcion valida del 0 al 5")
        print("------------------------------------------------")
