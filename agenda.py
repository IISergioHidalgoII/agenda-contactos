import json
import os

ARCHIVO = "contactos.json"

#==================== Funciones ====================

def cargar_contactos(): 
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_contactos(contactos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(contactos, f, ensure_ascii=False, indent=2)

def agregar_contacto(contactos):
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacio.")
        return
    telefono = input("Telefono: ").strip()
    correo = input("Correo: ").strip()
    contactos.append({"nombre": nombre, "telefono": telefono, "correo": correo})
    guardar_contactos(contactos)
    print(f"Contacto '{nombre}' agregado.")

def listar_contactos(contactos):
    if not contactos:
        print("No hay contactos guardados.")
        return
    print(f"\n{'#':<4} {'Nombre':<20} {'Telefono':<15} {'Correo'}")
    print("-" * 60)
    for i, c in enumerate(contactos, 1):
        print(f"{i:<4} {c['nombre']:<20} {c['telefono']:<15} {c['correo']}")

def buscar_contacto(contactos):
    termino = input("Buscar por nombre: ").strip().lower()
    resultados = [c for c in contactos if termino in c["nombre"].lower()]
    if not resultados:
        print("No se encontraron contactos.")
    else:
        for c in resultados:
            print(f"\nNombre:   {c['nombre']}")
            print(f"Telefono: {c['telefono']}")
            print(f"Correo:   {c['correo']}")

def actualizar_contacto(contactos):
    listar_contactos(contactos)
    if not contactos:
        return
    try:
        indice = int(input("\nNumero de contacto a editar: ")) - 1
        if 0 <= indice < len(contactos):
            c = contactos[indice]
            print(f"Editando '{c['nombre']}' (Enter para mantener el valor actual)")
            nuevo_nombre = input(f"Nombre [{c['nombre']}]: ").strip()
            nuevo_telefono = input(f"Telefono [{c['telefono']}]: ").strip()
            nuevo_correo = input(f"Correo [{c['correo']}]: ").strip()
            if nuevo_nombre:
                c['nombre'] = nuevo_nombre
            if nuevo_telefono:
                c['telefono'] = nuevo_telefono
            if nuevo_correo:
                c['correo'] = nuevo_correo
            guardar_contactos(contactos)
            print(f"Contacto actualizado.")
        else:
            print("Numero fuera de rango.")
    except ValueError:
        print("Entrada invalida.")

def eliminar_contacto(contactos):
    listar_contactos(contactos)
    if not contactos:
        return
    try:
        indice = int(input("\nNumero de contacto a eliminar: ")) - 1
        if 0 <= indice < len(contactos):
            eliminado = contactos.pop(indice)
            guardar_contactos(contactos)
            print(f"Contacto '{eliminado['nombre']}' eliminado.")
        else:
            print("Numero fuera de rango.")
    except ValueError:
        print("Entrada invalida.")

#==================== Menu principal ====================

def mostrar_menu():
    print("\n===== Agenda de Contactos =====")
    print("1. Agregar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")
    print("================================")

def main():
    contactos = cargar_contactos()
    acciones = {
        "1": agregar_contacto,
        "2": listar_contactos,
        "3": buscar_contacto,
        "4": actualizar_contacto,
        "5": eliminar_contacto,
    }

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "6":
            print("Bye Bye!")
            break
        elif opcion in acciones:
            acciones[opcion](contactos)
        else:
            print("Opcion no valida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
