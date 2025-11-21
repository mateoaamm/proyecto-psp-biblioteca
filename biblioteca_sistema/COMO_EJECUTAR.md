# 🚀 CÓMO EJECUTAR EL CÓDIGO - GUÍA COMPLETA

## Sistema de Gestión de Biblioteca Universitaria
**Desarrollado por:** Mateo Arroyave  
**Proyecto:** PSP 0.1

---

## 📋 PREREQUISITOS

Necesitas tener instalado:
- **Python 3.8 o superior** (recomendado 3.10+)
- **pip** (gestor de paquetes de Python)

### Verificar si tienes Python

```bash
# Windows (CMD o PowerShell)
python --version

# Linux/Mac
python3 --version
```

Si no tienes Python:
- **Windows:** Descarga desde https://www.python.org/downloads/
- **Mac:** `brew install python3`
- **Linux:** `sudo apt install python3 python3-pip`

---

## 🎯 OPCIÓN 1: EJECUCIÓN RÁPIDA (Recomendada)

### Paso 1: Descargar los archivos

Descarga estos 4 archivos y ponlos en una carpeta llamada `biblioteca_sistema`:

```
biblioteca_sistema/
├── app.py
├── models.py
├── config.py
└── requirements.txt
```

### Paso 2: Abrir terminal en la carpeta

**Windows:**
1. Abre la carpeta `biblioteca_sistema`
2. Shift + Click derecho → "Abrir ventana de PowerShell aquí"

**Mac/Linux:**
1. Abre Terminal
2. `cd ruta/a/biblioteca_sistema`

### Paso 3: Instalar dependencias

```bash
# Windows
pip install -r requirements.txt

# Mac/Linux
pip3 install -r requirements.txt
```

### Paso 4: Ejecutar la aplicación

```bash
# Windows
python app.py

# Mac/Linux
python3 app.py
```

### Paso 5: Abrir en el navegador

Abre tu navegador en: **http://localhost:5000**

¡Listo! 🎉

---

## 🎯 OPCIÓN 2: CON ENTORNO VIRTUAL (Más limpio)

### Paso 1: Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

Verás `(venv)` al inicio de tu terminal.

### Paso 2: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar

```bash
python app.py
```

### Paso 4: Abrir navegador

http://localhost:5000

---

## 📦 COMANDOS ADICIONALES

### Crear base de datos (si no se crea automáticamente)

```bash
# Windows
flask --app app init-db

# Mac/Linux
flask --app app init-db
```

### Agregar datos de ejemplo

```bash
flask --app app seed
```

Esto crea:
- 3 libros de ejemplo
- 2 usuarios de ejemplo

---

## 🖥️ CAPTURAS DE PANTALLA

### Pantalla Principal
```
┌─────────────────────────────────────────────┐
│      📚 Sistema de Biblioteca               │
│   Desarrollado por Mateo Arroyave          │
├─────────────────────────────────────────────┤
│  [3]           [2]            [0]           │
│  Libros      Usuarios      Préstamos        │
│                                             │
│  📖 Gestión de Libros                      │
│  👥 Gestión de Usuarios                    │
│  📋 Préstamos                              │
│  📊 API / Datos                            │
└─────────────────────────────────────────────┘
```

### Gestión de Libros
```
┌─────────────────────────────────────────────┐
│  📖 Gestión de Libros         [🏠 Inicio]  │
├─────────────────────────────────────────────┤
│  Agregar Nuevo Libro                       │
│  ISBN: [____________]                       │
│  Título: [____________]                     │
│  Autor: [____________]                      │
│  [➕ Agregar Libro]                         │
├─────────────────────────────────────────────┤
│  📚 Catálogo Actual                        │
│  ┌────────────────────────────────────┐    │
│  │ ISBN    │ Título  │ Autor │ Estado │    │
│  │ 978...  │ Clean.. │ Mart..│   ✓    │    │
│  └────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
```

---

## 🔧 SOLUCIÓN DE PROBLEMAS

### Error: "No module named 'flask'"

**Solución:**
```bash
pip install flask flask-sqlalchemy
```

### Error: "Address already in use"

**Solución:** El puerto 5000 está ocupado. Cambia el puerto en `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

Luego abre: http://localhost:5001

### Error: "Permission denied"

**Solución (Mac/Linux):**
```bash
chmod +x app.py
python3 app.py
```

### No se crea la base de datos

**Solución:**
```bash
flask --app app init-db
```

---

## 📱 ACCEDER DESDE OTRO DISPOSITIVO

Si quieres acceder desde tu celular o tablet en la misma red:

1. Encuentra tu IP:
   ```bash
   # Windows
   ipconfig
   
   # Mac/Linux
   ifconfig
   ```

2. Busca algo como `192.168.1.X`

3. En tu celular, abre: `http://192.168.1.X:5000`

---

## 🎨 PERSONALIZACIÓN

### Cambiar el puerto

En `app.py`, línea final:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Tu puerto
```

### Cambiar configuración de préstamos

En `config.py`:
```python
DIAS_PRESTAMO = 14  # Cambiar a 14 días
MULTA_POR_DIA = 2000  # Cambiar multa a $2000
MAX_PRESTAMOS_SIMULTANEOS = 5  # Permitir 5 préstamos
```

---

## 🧪 PROBAR LA APLICACIÓN

### 1. Agregar un libro

1. Ve a "Gestión de Libros"
2. Llena el formulario:
   - ISBN: `9780134685991`
   - Título: `Effective Java`
   - Autor: `Joshua Bloch`
3. Click "Agregar Libro"

### 2. Ver datos en JSON

Abre en el navegador: http://localhost:5000/api/datos

Verás todos los datos en formato JSON.

---

## 📊 API ENDPOINTS

La aplicación incluye una API REST básica:

```
GET /api/datos
```

**Respuesta:**
```json
{
  "proyecto": "Sistema de Biblioteca",
  "desarrollador": "Mateo Arroyave",
  "metodologia": "PSP 0.1",
  "total_libros": 3,
  "total_usuarios": 2,
  "prestamos_activos": 0,
  "libros": [...]
}
```

---

## 🛑 DETENER LA APLICACIÓN

Para detener el servidor:
- Presiona `Ctrl + C` en la terminal

---

## 📝 ESTRUCTURA DE ARCHIVOS

```
biblioteca_sistema/
│
├── app.py              # Aplicación principal
├── models.py           # Modelos de datos (Libro, Usuario, Prestamo)
├── config.py           # Configuración
├── requirements.txt    # Dependencias
│
└── biblioteca.db       # Base de datos (se crea automáticamente)
```

---

## 🎓 CARACTERÍSTICAS DEL SISTEMA

### Funcionalidades Implementadas:

✅ **Gestión de Libros**
- Agregar libros con validación de ISBN
- Visualizar catálogo completo
- Control de disponibilidad

✅ **API REST**
- Endpoint JSON con datos del sistema
- Información en tiempo real

✅ **Base de Datos**
- SQLite (no requiere instalación adicional)
- Modelos relacionales completos

✅ **Interfaz Web**
- Diseño responsive
- Gradientes modernos
- Fácil de usar

### Funcionalidades Pendientes (para expandir):

⏳ Gestión completa de usuarios
⏳ Registro de préstamos y devoluciones
⏳ Cálculo automático de multas
⏳ Búsqueda avanzada de libros
⏳ Reportes y estadísticas

---

## 💻 TECNOLOGÍAS UTILIZADAS

- **Python 3.10+** - Lenguaje de programación
- **Flask 3.0** - Framework web
- **SQLAlchemy** - ORM para base de datos
- **SQLite** - Base de datos
- **HTML5 + CSS3** - Frontend

---

## 📚 PARA APRENDER MÁS

### Recursos de Flask:
- Documentación oficial: https://flask.palletsprojects.com/
- Tutorial completo: https://flask.palletsprojects.com/tutorial/

### Recursos de SQLAlchemy:
- Documentación: https://www.sqlalchemy.org/

---

## ✅ CHECKLIST DE EJECUCIÓN

Antes de ejecutar, verifica:

- [ ] Python 3.8+ instalado
- [ ] pip funciona correctamente
- [ ] Los 4 archivos están en la misma carpeta
- [ ] Terminal abierta en la carpeta correcta
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] Puerto 5000 libre (o usar otro puerto)

---

## 🎉 ¡LISTO!

Si seguiste todos los pasos, deberías ver:

```
============================================================
🚀 INICIANDO SISTEMA DE BIBLIOTECA
============================================================
📚 Proyecto: Sistema de Gestión de Biblioteca
👨‍💻 Desarrollador: Mateo Arroyave
📊 Metodología: PSP 0.1
============================================================

🌐 Abre tu navegador en: http://localhost:5000
⏹️  Para detener: Presiona Ctrl+C

 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
```

**¡Disfruta tu Sistema de Biblioteca!** 🚀📚

---

**Desarrollado por:** Mateo Arroyave  
**Proyecto:** PSP 0.1 - Sistema de Gestión de Biblioteca  
**Fecha:** Noviembre 2025
