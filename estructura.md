app/
├── alembic/                  # Migraciones de base de datos
├── api/
│   └── v1/
│       ├── endpoints/
│       │   ├── auth.py       # Endpoints de login y autenticacion
│       │   ├── empleados.py  # Endpoints de empleados
│       │   ├── usuarios.py   # Endpoints de usuarios
│       │   └── menus.py      # Endpoints de menús
│       └── api.py            # Router principal v1
├── core/
│   ├── auth.py              # Autenticación con JWT
│   ├── security.py          # Cifrado y verificacion de contraseñas
│   ├── config.py            # Configuración centralizada
│   ├── exceptions.py        # Manejo de excepciones
│   └── logging_config.py    # Configuración de logging
├── db/
│   ├── connection.py        # Gestión de conexiones
│   └── queries.py           # Queries centralizados
├── models/                  # Modelos
│   ├── empleado.py
│   ├── usuario.py
│   └── menu.py
├── schemas/                # Schemas Pydantic
│   ├── auth.py
│   ├── empleado.py
│   ├── usuario.py
│   └── menu.py
├── services/               # Lógica de negocio
│   ├── empleado_service.py
│   ├── usuario_service.py
│   └── menu_service.py
├── utils/                 # Utilidades
│   └── menu_helper.py
├── .env                   # Variables de entorno
├── .gitignore            # Archivos ignorados por git
├── requirements.txt      # Dependencias del proyecto
└── main.py              # Punto de entrada de la aplicación