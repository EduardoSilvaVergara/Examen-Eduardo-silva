import random as rd 
import csv
import statistics as st 

def asignar_sueldos(trabajadores):
    sueldos_trabajadores = {}

    for trabajador in trabajadores:
        sueldo = rd.randint(300000, 2500000)

        sueldos_trabajadores[trabajador] = sueldo

    print("Saldo asignado correctamente")
    print("------------------------------------------------------------------------------")
    print(sueldos_trabajadores)
    print("------------------------------------------------------------------------------\n") 

    return sueldos_trabajadores

def clasificar_sueldos(sueldos_trabajadores):
    menores_800k = {}
    entre_800k_2millones = {}  
    mayor_2millones = {}

    for trabajador, sueldo in sueldos_trabajadores.items():
        if sueldo < 800000:
            menores_800k[trabajador] = sueldo
        elif sueldo <=2000000:
            entre_800k_2millones[trabajador] = sueldo
        else:
            mayor_2millones[trabajador] = sueldo

    sueldo = list(sueldos_trabajadores.values())
    total = sum(sueldo)

    print("------------------------------------------------------------------------------")
    print("Los sueldos menores a 800.000 son  Total:", len(menores_800k))
    print("Nombre","         Sueldo")
    for trabajador, sueldo in menores_800k.items():
        print(trabajador, ":  $",sueldo)

    print("")
    print("Los sueldos entre 800.000 y 2.000.000 son  Total:", len(entre_800k_2millones))
    print("Nombre","         Sueldo")
    for trabajador, sueldo in entre_800k_2millones.items():
        
        print(trabajador, ":  $",sueldo)

    print("")
    print("Los sueldos mayores a 2.000.000 son  Total:", len(mayor_2millones))
    print("Nombre","         Sueldo")
    for trabajador, sueldo in mayor_2millones.items():
        print(trabajador, ":  $",sueldo)
    print("")
    print("El total de los sueldos es: ", total)
    print("------------------------------------------------------------------------------\n")
    

def estadísticas_sueldos(sueldos_trabajadores):
    
    sueldo = list(sueldos_trabajadores.values())

    if not sueldos_trabajadores:
        print("Primero asigne sueldos a los trabajadores")
        return None, None, None
    
    max_sueldo = max(sueldo)
    min_sueldo = min(sueldo)
    prom_sueldo = sum(sueldo) / len(sueldo)
    media_geometrica =st.geometric_mean(sueldo)

    return max_sueldo, min_sueldo, prom_sueldo, media_geometrica

def generar_reporte(sueldos_trabajadores):

    descsalud = {}
    descafp = {}
    sueldoliquido = {}

    with open("Reporte_seldos.csv", "w",newline="") as archivo:
        escritor = csv.writer(archivo,delimiter=",")

        escritor.writerow(["Trabajadores", "|   |$","Sueldo base", "|   |$","Descuento salud", "|   |$","Descuneto de afp", "|   |$","Sueldo liquido"])
        escritor.writerow("                                                 ")
        for trabajador, sueldo in sueldos_trabajadores.items():
            descsalud = sueldo * 0.07
            descafp= sueldo * 0.12
            sueldoliquido = sueldo - descafp - descsalud
            escritor.writerow([trabajador, "|   |$",sueldo, "|   |$",descsalud, "|   |$",descafp, "|   |$",sueldoliquido])
            escritor.writerow(["Los sueldos no estan truncados, por favor leer el valor antes del ."])

    print("-------------------------------------")
    print("Reporte generado correctamente en csv")
    print("-------------------------------------\n")