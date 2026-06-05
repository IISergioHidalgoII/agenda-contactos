# Agenda de Contactos

Aplicación de consola para gestionar contactos con nombre, teléfono y correo. Los datos se guardan en un archivo `contactos.json` de forma persistente.

## Cómo ejecutar

```bash
python agenda.py
```

## Funciones

| Función | Qué hace |
|---|---|
| `cargar_contactos()` | Lee el archivo `contactos.json` y retorna la lista de contactos. Si no existe, retorna lista vacía |
| `guardar_contactos(contactos)` | Escribe la lista de contactos en `contactos.json` |
| `agregar_contacto(contactos)` | Pide nombre, teléfono y correo al usuario y agrega el contacto a la lista |
| `listar_contactos(contactos)` | Muestra todos los contactos en formato de tabla |
| `buscar_contacto(contactos)` | Filtra contactos cuyo nombre contenga el término buscado |
| `eliminar_contacto(contactos)` | Muestra la lista y elimina el contacto por número seleccionado |
| `mostrar_menu()` | Imprime el menú de opciones en consola |
| `main()` | Carga los contactos y controla el flujo principal en un bucle |

## Diagrama de flujo

```
Inicio
  │
  ▼
cargar_contactos() ──► lee contactos.json (o lista vacía)
  │
  ▼
mostrar_menu()
  │
  ▼
¿Opción ingresada?
  ├─ "1" ──► agregar_contacto() ──► guardar_contactos() ──► volver al menú
  │
  ├─ "2" ──► listar_contactos() ──────────────────────────► volver al menú
  │
  ├─ "3" ──► buscar_contacto() ───────────────────────────► volver al menú
  │
  ├─ "4" ──► listar_contactos()
  │               │
  │               ▼
  │          eliminar_contacto() ──► guardar_contactos() ──► volver al menú
  │
  ├─ "5" ──► Salir
  │
  └─ otra ──► "Opción no válida" ──────────────────────────► volver al menú
```

## Almacenamiento

Los contactos se guardan en `contactos.json` (excluido del repo vía `.gitignore`):

```json
[
  {
    "nombre": "Juan Pérez",
    "telefono": "1234-5678",
    "correo": "juan@correo.com"
  }
]
```

## Tecnologías

- Python 3
- Módulo `json` (estándar)
- Módulo `os` (estándar)
