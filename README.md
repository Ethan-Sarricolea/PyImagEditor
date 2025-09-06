# PyImagEditor
Una app con funciones basicas de edición de imagenes

## Arquitectura

Se utiliza la arquitectura MVC

```bash
PyImagEditor/
│
├── models/            # Lógica de negocio y datos
│   ├── __init__.py
│   └── imagen.py      # Ej: funciones para procesar imagenes
│
├── views/             # Presentación (UI, consola, web, etc.)
│   ├── __init__.py
│   └── consola.py     # Ej: imprimir resultados, mostrar mensajes
│
├── controllers/       # Controladores (conectan vista y modelo)
│   ├── __init__.py
│   └── imagen_ctrl.py # Ej: coordina pegar imagen y quitar fondo
│
├── utils/             # (Opcional) funciones auxiliares/reutilizables
│   └── helpers.py
│
├── main.py            # Punto de entrada de la app
└── requirements.txt   # Dependencias (ej. rembg, pillow)
```

## Requerimientos

`pip install -r requirements.txt`

## Operaciones

Modelo
- Eliminar fondo

Controlador
- Copiar imagen
- Pegar imagen
- Guardar imagen

Vista
- Mensajes en consola
- Pantallas (posterior)