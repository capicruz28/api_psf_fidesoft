-- Tabla Menu
CREATE TABLE menu (
    menu_id INT PRIMARY KEY IDENTITY(1,1),
    nombre NVARCHAR(100) NOT NULL,
    icono NVARCHAR(50),
    ruta NVARCHAR(255),
    padre_menu_id INT,
    orden INT,
    es_activo BIT DEFAULT 1,
    fecha_creacion DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (padre_menu_id) REFERENCES menu(menu_id)
);

-- Tabla Rol
CREATE TABLE rol (
    rol_id INT PRIMARY KEY IDENTITY(1,1),
    nombre NVARCHAR(50) NOT NULL,
    descripcion NVARCHAR(255),
    es_activo BIT DEFAULT 1,
    fecha_creacion DATETIME DEFAULT GETDATE()
);

-- Tabla Usuario
CREATE TABLE usuario (
    usuario_id INT PRIMARY KEY IDENTITY(1,1),
    nombre_usuario NVARCHAR(50) NOT NULL UNIQUE,
    correo NVARCHAR(100) NOT NULL UNIQUE,
    contrasena NVARCHAR(255) NOT NULL,
    nombre NVARCHAR(50),
    apellido NVARCHAR(50),
    es_activo BIT DEFAULT 1,
    correo_confirmado BIT DEFAULT 0,
    fecha_creacion DATETIME DEFAULT GETDATE(),
    fecha_ultimo_acceso DATETIME,
    fecha_actualizacion DATETIME,
    es_eliminado BIT DEFAULT 0
);

-- Tabla UsuarioRol
CREATE TABLE usuario_rol (
    usuario_rol_id INT PRIMARY KEY IDENTITY(1,1),
    usuario_id INT NOT NULL,
    rol_id INT NOT NULL,
    fecha_asignacion DATETIME DEFAULT GETDATE(),
    es_activo BIT DEFAULT 1,
    FOREIGN KEY (usuario_id) REFERENCES usuario(usuario_id),
    FOREIGN KEY (rol_id) REFERENCES rol(rol_id)
);

-- Tabla RolMenuPermiso
CREATE TABLE rol_menu_permiso (
    rol_menu_id INT PRIMARY KEY IDENTITY(1,1),
    rol_id INT,
    menu_id INT,
    puede_ver BIT DEFAULT 1,
    puede_editar BIT DEFAULT 0,
    puede_eliminar BIT DEFAULT 0,
    FOREIGN KEY (rol_id) REFERENCES rol(rol_id),
    FOREIGN KEY (menu_id) REFERENCES menu(menu_id)
);