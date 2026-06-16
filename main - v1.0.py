import csv
import os

archivo_csv = "inventario_mercadocaro.csv"

archivo_existe = os.path.exists(archivo_csv)

with open(archivo_csv, "a", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)

    if not archivo_existe:
        escritor.writerow([
            "Marca",
            "Modelo",
            "Categoria",
            "Pieza",
            "Precio",
            "Cantidad"
        ])

    while True:
        print("\n=== INVENTARIO MERCADOCARO ===")
        print("1. Agregar producto individual")
        print("2. Agregar telefono completo")
        print("3. Buscar producto")
        print("4. Ver todo el inventario")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            print("\n--- Nuevo Producto ---")

            marca = input("marca: ")
            modelo = input("modelo: ")
            categoria = input("categoria: ")
            pieza = input("pieza: ")
            precio = input("precio: ")
            cantidad = input("cantidad: ")

            print("\n--- Verificar datos ---")
            print(f"Marca: {marca}")
            print(f"Modelo: {modelo}")
            print(f"Categoria: {categoria}")
            print(f"Pieza: {pieza}")
            print(f"Precio: {precio}")
            print(f"Cantidad: {cantidad}")

            confirmar = input("\n¿Los datos son correctos? (s/n): ")

            if confirmar.lower() == "s":
                escritor.writerow([
                    marca,
                    modelo,
                    categoria,
                    pieza,
                    precio,
                    cantidad
                ])
                archivo.flush()

                print("\nproducto guardado correctamente.")
            else:
                print("\nProducto no guardado.")

        elif opcion == "2":
            piezas_base = [
                ("Tarjetas Logicas", "Tarjeta Logica"),
                ("Bocinas", "Bocina Altavoz"),
                ("Bocinas", "Bocina Llamadas"),
                ("Camaras", "Camara Trasera"),
                ("Camaras", "Camara Frontal"),
                ("Centros de Carga", "Centro de Carga"),
                ("Flex", "Flex Interconexion"),
                ("Flex", "Flex Volumen"),
                ("Flex", "Flex Encendido"),
                ("Antenas", "Antena Señal"),
                ("Tapas Internas", "Tapa Interna NFC"),
                ("Flex", "Flex Sensor Huella"),
                ("Baterias", "Bateria"),
                ("Tapas Traseras", "Tapa Trasera"),
                ("Bandejas SIM", "Bandeja SIM")
             ]

            print("\n--- Agregar telefono completo ---")

            marca = input("Marca del telefono: ")
            modelo = input("Modelo del telefono: ")

            productos_guardados = 0

            for categoria, pieza in piezas_base:
                 existe = input(f"¿Existe {pieza}? (s/n): ")

                 if existe.lower() == "s":
                     precio = input(f"Precio de {pieza}: ")
                     cantidad = input(f"Cantidad de {pieza}: ")

                     escritor.writerow([
                         marca,
                         modelo,
                         categoria,
                         pieza,
                         precio,
                         cantidad
                     ])
                      
                     archivo.flush()

                     productos_guardados += 1
                     print(f"{pieza} guardado correctamente.")

            print(f"\nTelefono procesado. Productos guardados: {productos_guardados}" )   
        elif opcion == "3":
            termino = input("\nbuscar marca, modelo o pieza: ").lower()
            
            print("\n=== RESULTADOS ===")
       
            encontrados = 0

            with open(archivo_csv, "r", encoding="utf-8") as archivo_busqueda:

                lector = csv.reader(archivo_busqueda)

                next(lector)

                for fila in lector:

                    texto = " ".join(fila).lower()
                    
                    palabras = termino.split()

                    if all(palabra in texto for palabra in palabras):

                       print(
                           f"{fila[0]} | {fila[1]} | {fila[2]} | "
                           f"{fila[3]} | {fila[4]} | stock: {fila[5]}"
                       )  

                       encontrados += 1

            if encontrados == 0:
               print("no se encontraron resultados")     

        elif opcion == "4":
            print("\n=== INVENTARIO COMPLETO ===")

            with open(archivo_csv, "r", encoding="utf-8") as archivo_busqueda:
                lector = csv.reader(archivo_busqueda)
                next(lector)

                for fila in lector:
                    print(
                        f"{fila[0]} | {fila[1]} | {fila[2]} | "
                        f"{fila[3]} | ${fila[4]} | stock: {fila[5]}"
                     )

        elif opcion == "5":
           break

        else:
            print("\nOpcion no valida. Intenta de nuevo.")

print("\nprograma finalizado.")
print(f"archivo actualizado: {archivo_csv}")