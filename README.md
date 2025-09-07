# PyImagEditor

This is my app to remove background of the images on my files or images from clipboard, also you can copy the output image.

I will update the app to add more functions and make the interface.

For now, the app works only for console.

## architecture

I use the MVC architecture

```bash
PyImagEditor/
│
├── model/            # Logic
│   ├── __init__.py
│   └── background_rm.py   # remove background functions
│   └── image_ctrl.py      # copy, paste on clipboard functions
│
├── view/             # UI (console, web, desktop)
│   ├── __init__.py
│   └── console.py     # console messages
│
├── controller/       # Controller (view and controller connection)
│   ├── __init__.py
│   └── console_ctrl.py # Console options
│
├── utils/             # auxiliary functions
│   └── helpers.py     # optional
│
├── main.py            # App execution
└── requirements.txt   # Dependencies
```

## Requirements

`pip install -r requirements.txt`

## Operations

Modelo
- remove background
- Copy background
- Paste image
- Save image

Controlador
- I/O

Vista
- Interface messages
- Desktop (posterior)

