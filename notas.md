# CLONACION EN NUEVO EQUIPO
# Clona tu repositorio
git clone https://github.com/tu-usuario/tu-repositorio.git
# Abrir ruta del repositorio
cd tu-repositorio
# crear espacio virtual 
python -m venv venv     
# acceder al espacio virtual 
venv\Scripts\activate
# Instala las dependencias
pip install -r requirements.txt
# ejecutar apis
uvicorn app.main:app --reload

# crear (.env) para conexion db
# Database
DB_SERVER=perufashions9
DB_USER=sa
DB_PASSWORD=HebsMaq
DB_DATABASE=bdtex
DB_PORT=1433

# Security
SECRET_KEY=8c8b3c6a0b178437c99799e426cd5f6ee992e496d8ca0e25444eb2a3914690c3
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM=HS256

# Logging
LOG_LEVEL=INFO

# DESPLIEGUE EN SERVIDOR
# Instala Python
Descarga Python desde: python.org. (Durante la instalación, selecciona "Add Python to PATH".)
# Instala Git
Instala Git si no lo tienes: Git for Windows.
# Clona tu repositorio
git clone https://github.com/tu-usuario/tu-repositorio.git
# Abrir ruta del repositorio
cd tu-repositorio
# Crea un entorno virtual
python -m venv venv
# Activa el entorno virtual
venv\Scripts\activate
# Instala las dependencias
pip install -r requirements.txt
# Prueba que tu API funciona localmente
uvicorn app.main:app --host 0.0.0.0 --port 8000
# Para ejecutar FastAPI en segundo plano como un servicio
# Crea un archivo batch (start_api.bat) en la carpeta del proyecto
start_api.bat creado en la aplicación
# Descarga e instala NSSM
descarga y dirigite a la carpeta para ejecutar comandos.
# Creacion de un servicio
./nssm.exe install FastAPI_Service
# Direccionar al archivo .bat
Path: Ruta del archivo start_api.bat.
Startup Directory: Carpeta del proyecto.
Guarda y cierra.
# Iniciar el Servicio de FastAPI
net start FastAPI_Service
# Detener el Servicio de FastAPI
net stop FastAPI_Service
# Automatización con un Script si realizas actualizaciones frecuentes (Opcional)
update_api.bat creado en la aplicación

# GITHUB
# Comandos Básicos de Git
# git init 
Inicializa un nuevo repositorio Git en el directorio actual.
# git clone <url>
Clona un repositorio remoto en tu máquina local.
# git status
Muestra el estado actual del repositorio, incluyendo archivos modificados y no rastreados.
# git add <archivo>
Agrega archivos al área de preparación (staging area).
# git commit -m "mensaje"
Crea un commit con los cambios en el área de preparación.
# git push
Sube los commits al repositorio remoto.
# git pull
Descarga y fusiona los cambios del repositorio remoto.
# git fetch
Descarga cambios del repositorio remoto sin fusionarlos.
# git merge <rama>
Fusiona la rama especificada con la rama actual.
# git branch
Lista las ramas existentes.
# git checkout <rama>
Cambia a la rama especificada.
# git log
Muestra el historial de commits.
# git diff
Muestra las diferencias entre el área de trabajo y el área de preparación o entre commits.

# Comandos Avanzados
# git branch <nombre-rama>
Crea una nueva rama.
# git checkout -b <nombre-rama>
Crea y cambia a una nueva rama.
# git rebase <rama>
Reaplica commits de la rama actual sobre otra rama.
# git stash
Guarda temporalmente los cambios no confirmados.
# git stash pop
Restaura los cambios guardados con stash y los elimina de la pila de stash.
# git reset <archivo>
Quita un archivo del área de preparación.
# git reset --hard <commit>
Restablece el repositorio a un estado anterior (¡usa con cuidado!).
# git tag <nombre-tag>
Crea una etiqueta en el commit actual.
# git remote add <nombre> <url>
Agrega un nuevo repositorio remoto.
# git remote -v
Muestra los repositorios remotos configurados.

# Comandos relacionados con GitHub
# git push origin <rama>
Sube los commits de una rama específica al repositorio remoto.
# git pull origin <rama>
Descarga cambios de una rama específica y los fusiona.
# git clone <url>
Clona un repositorio GitHub en tu máquina local.
# git remote set-url origin <url>
Cambia la URL del repositorio remoto.
# gh repo create
(usando la CLI de GitHub) Crea un nuevo repositorio en GitHub.
# gh pr create
(usando la CLI de GitHub) Crea un nuevo pull request en GitHub.