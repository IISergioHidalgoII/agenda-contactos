import json
import os

ARCHIVO = "contactos.json"

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

def mostrar_menu():
    print("\n===== Agenda de Contactos =====")
    print("1. Agregar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    print("================================")

def main():
    contactos = cargar_contactos()
    acciones = {
        "1": agregar_contacto,
        "2": listar_contactos,
        "3": buscar_contacto,
        "4": eliminar_contacto,
    }

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "5":
            print("¡Hasta luego!")
            break
        elif opcion in acciones:
            if opcion in ("1", "4"):
                acciones[opcion](contactos)
            else:
                acciones[opcion](contactos)
        else:
            print("Opcion no valida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
