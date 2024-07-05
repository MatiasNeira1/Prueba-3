import globales
import os
import random
import math


def crear_venta_al_azar():
    todas_los_productos=globales.leer_archivo_json('productos.json')
    todas_las_ventas=globales.leer_archivo_json('ventas.json')

    for i in range(10):
        producto=random.choice(todas_los_productos)

        productos=producto['nombre']

        venta=random.randint(2000,10000)

        iva=float(venta*19/100)

        venta_aleatoria={
            "nombre":productos,
            "venta":round(venta),
            "iva": math.trunc(iva)
        }

        todas_las_ventas.append(venta_aleatoria)
    globales.guardar_archivo_json('productos.json', todas_las_ventas)





def producto_valor_mas_alto():
    todas_los_productos=globales.leer_archivo_json('productos.json')
    todas_las_ventas=globales.leer_archivo_json('ventas.json')

    producto_ord=sorted(todas_los_productos, key=lambda x:x ['venta'], reverse=True)

    for producto in producto_ord[:1]:
        nombre_producto=""
        valor_venta=0
        for venta in todas_los_productos:
            if producto['nombre']==venta['nombre']:
                nombre_producto=f"{producto['nombre']}"
                valor_venta=f"{venta['venta']}"
    print(F"El producto mas caro es {nombre_producto} y su precio es de ${valor_venta}")

def producto_iva_mas_alto():
        todas_los_productos=globales.leer_archivo_json('productos.json')
        todas_las_ventas=globales.leer_archivo_json('ventas.json')

        producto_ord=sorted(todas_los_productos, key=lambda x:x ['iva'], reverse=True)

        for producto in producto_ord[:1]:
            nombre_producto=""
            valor_venta=0
            for venta in todas_los_productos:
                if producto['nombre']==venta['nombre']:
                    nombre_producto=f"{producto['nombre']}"
                    valor_venta=f"{venta['iva']}"
        print(F"El producto que tiene mayor iva es {nombre_producto} y su iva es de ${valor_venta}")

def promedio_ventas():
    todas_los_productos=globales.leer_archivo_json('productos.json')

    suma_ventas=0
    cantidad_ventas=0

    for venta in todas_los_productos:

        suma_ventas+=venta['venta']
        cantidad_ventas+=1

        promedio_ventas= suma_ventas / cantidad_ventas
    print(f"El promedio de las ventas es ${int(promedio_ventas)}")

def media_geometrica():
    todas_los_productos=globales.leer_archivo_json('productos.json')

    suma_ventas=0
    cantidad_ventas=0

    for venta in todas_los_productos:

        suma_ventas+=math.log(venta['venta'])
        cantidad_ventas+=1

        promedio_ventas=math.exp (suma_ventas / cantidad_ventas)
    print(f"El promedio de las ventas es ${int(promedio_ventas)}")


def menu_estadistica():
    while True:
        os.system("cls")
        print("1. Producto con valor mas alto")
        print("2. Producto IVA mas alto")
        print("3. Promedio Ventas")
        print("4. Media Geometrica")
        

        opcion=globales.seleccionar_opcion(4)

        if opcion==1:
            producto_valor_mas_alto()
        elif opcion==2:
            producto_iva_mas_alto()
        elif opcion==3:
            promedio_ventas() 
        elif opcion==4:
            media_geometrica()           
            return
            
        input("Presione ENTER para continuar")
        










def menu_principal():
    while True:
        os.system("cls")
        print("1. Asignar montos aleatorios")
        print("2. Ver estadísticas")
        print("3. Salir del programa")

        opcion=globales.seleccionar_opcion(3)

        if opcion==1:
            crear_venta_al_azar()
        elif opcion==2:
            menu_estadistica()
        elif opcion==3:
            print("SALIo DEL PROGRAMA")
            return
            
        input("Presione ENTER para continuar")

menu_principal()

    