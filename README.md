

## 📋 LO QUE NECESITAS

- [ ] Cuenta de GitHub (crear en https://github.com/signup si no tienes)
- [ ] Navegador web
- [ ] Tus archivos listos en tu computadora

---

## 🎯 PASO 1: CREAR REPOSITORIO EN GITHUB

### 1.1 Ir a GitHub

1. Abre tu navegador
2. Ve a: **https://github.com**
3. **Inicia sesión** con tu cuenta

### 1.2 Crear Nuevo Repositorio

1. Click en el **botón verde "New"** (arriba a la izquierda)
   - O ve a: https://github.com/new

2. **Llena el formulario:**
   ```
   Repository name: proyecto-psp-biblioteca
   
   Description: Sistema de Gestión de Biblioteca - Proyecto PSP
   
   Visibilidad:
   ○ Public  ← Selecciona esta (recomendado)
   ○ Private
   
   Initialize this repository with:
   ☑ Add a README file  ← MARCA ESTA
   ☐ Add .gitignore     ← Déjala sin marcar
   ☐ Choose a license   ← Déjala sin marcar
   ```

3. Click **"Create repository"** (botón verde abajo)

### ✅ Resultado:
Verás tu repositorio creado con un archivo README.md básico.

---

## 📁 PASO 2: CREAR ESTRUCTURA DE CARPETAS

Ahora vamos a crear las carpetas para organizar tus archivos.

### 2.1 Crear carpeta "excel"

1. En tu repositorio, click en **"Add file"** (arriba a la derecha)
2. Selecciona **"Create new file"**
3. En el campo de nombre escribe: `excel/README.md`
   - ⚠️ IMPORTANTE: El `/` crea la carpeta automáticamente
4. En el contenido escribe:
   ```
   # Excel PSP
   
   Contiene el archivo Excel con todas las métricas del proyecto PSP.
   ```
5. Scroll abajo y click **"Commit new file"** (botón verde)

### 2.2 Crear carpeta "informes"

1. Click en **"Add file"** → **"Create new file"**
2. Nombre: `informes/README.md`
3. Contenido:
   ```
   # Informes PSP
   
   Documentación y análisis del proyecto.
   ```
4. Click **"Commit new file"**

### 2.3 Crear carpeta "sistema-biblioteca"

1. Click en **"Add file"** → **"Create new file"**
2. Nombre: `sistema-biblioteca/README.md`
3. Contenido:
   ```
   # Sistema de Biblioteca
   
   Código fuente del sistema web.
   ```
4. Click **"Commit new file"**

---

## 📤 PASO 3: SUBIR ARCHIVOS

Ahora vamos a subir tus archivos a cada carpeta.

### 3.1 Subir Excel

1. Click en la carpeta **"excel"**
2. Click en **"Add file"** → **"Upload files"**
3. **Arrastra** o click "choose your files"
4. Selecciona: `PSP_CORREGIDO_SIN_ERRORES.xlsx`
5. Scroll abajo
6. En "Commit changes" escribe: `Agregar Excel con métricas PSP`
7. Click **"Commit changes"** (verde)

### 3.2 Subir Informes

1. Click en el nombre del repo (arriba) para volver a la raíz
2. Click en la carpeta **"informes"**
3. Click en **"Add file"** → **"Upload files"**
4. **Arrastra** los 3 archivos:
   - `INFORME_FINAL_SIMPLE.md`
   - `INFORME_EXPLICATIVO_METRICAS.md`
   - `GLOSARIO_PSP_COMPLETO.md`
5. Mensaje: `Agregar informes PSP`
6. Click **"Commit changes"**

### 3.3 Subir Código del Sistema

1. Volver a la raíz (click en nombre del repo)
2. Click en carpeta **"sistema-biblioteca"**
3. Click en **"Add file"** → **"Upload files"**
4. **Arrastra** todos los archivos del sistema:
   - `app.py`
   - `models.py`
   - `config.py`
   - `requirements.txt`
   - `COMO_EJECUTAR.md`
5. Mensaje: `Agregar código fuente del sistema`
6. Click **"Commit changes"**

---

## 📝 PASO 4: EDITAR EL README PRINCIPAL

Ahora vamos a mejorar el README principal del proyecto.

### 4.1 Ir al README

1. Volver a la raíz del repositorio (click en el nombre)
2. Verás el archivo **README.md** listado
3. Click en el archivo `README.md`

### 4.2 Editar README

1. Click en el **ícono de lápiz** (✏️) arriba a la derecha que dice "Edit this file"
2. **Borra** todo el contenido actual
3. **Copia y pega** este contenido:

```markdown
# 📊 Proyecto PSP - Sistema de Gestión de Biblioteca

## Desarrollado por Mateo Arroyave
**Universidad Libre Seccional Pereira**  
**Fecha:** Noviembre 2025  
**Metodología:** Personal Software Process (PSP 0.1)

---

## 📋 Descripción

Sistema de gestión de biblioteca universitaria desarrollado siguiendo la metodología PSP (Personal Software Process). Este proyecto incluye:

- Sistema web completo con Flask y SQLite
- Registro detallado de tiempo y defectos
- Análisis de métricas de calidad y productividad
- Documentación completa del proceso PSP

---

## 📊 Resultados del Proyecto

### Métricas Principales:
- **Tiempo Total:** 1,375 minutos (22.9 horas)
- **LOC Producidas:** 1,000 líneas
- **Productividad:** 43.6 LOC/hora ✅
- **Defectos:** 12 encontrados y corregidos
- **Yield:** 58.3%
- **Calificación:** 7.5/10

---

## 📁 Estructura del Repositorio

```
proyecto-psp-biblioteca/
│
├── excel/                          # Datos PSP en Excel
│   └── PSP_CORREGIDO_SIN_ERRORES.xlsx
│
├── informes/                       # Documentación y análisis
│   ├── INFORME_FINAL_SIMPLE.md
│   ├── INFORME_EXPLICATIVO_METRICAS.md
│   └── GLOSARIO_PSP_COMPLETO.md
│
├── sistema-biblioteca/             # Código fuente
│   ├── app.py
│   ├── models.py
│   ├── config.py
│   ├── requirements.txt
│   └── COMO_EJECUTAR.md
│
└── README.md
```

---

## 🚀 Cómo Ejecutar el Sistema

### Prerequisitos:
- Python 3.8+
- pip

### Instalación:

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/proyecto-psp-biblioteca.git

# 2. Entrar al directorio
cd proyecto-psp-biblioteca/sistema-biblioteca

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar
python app.py

# 5. Abrir navegador
http://localhost:5000
```

---

## 📊 Documentación PSP

### Excel con Datos Completos:
- **Time Recording:** Registro de 11 sesiones de trabajo
- **Defect Recording:** 12 defectos documentados
- **Quality Metrics:** Todas las métricas calculadas
- **Dashboard:** Evaluación de cumplimiento de objetivos

### Informes Incluidos:

1. **[INFORME_FINAL_SIMPLE.md](./informes/INFORME_FINAL_SIMPLE.md)**
   - Análisis de todas las tablas del Excel
   - 12 secciones con interpretaciones
   - Conclusiones y recomendaciones

2. **[INFORME_EXPLICATIVO_METRICAS.md](./informes/INFORME_EXPLICATIVO_METRICAS.md)**
   - Explicación detallada de cada métrica
   - Fórmulas y cálculos
   - Ejemplos prácticos

3. **[GLOSARIO_PSP_COMPLETO.md](./informes/GLOSARIO_PSP_COMPLETO.md)**
   - Definición de todos los términos
   - LOC, Yield, Defectos/KLOC, etc.
   - Ejemplos aplicados al proyecto

---

## 🎯 Métricas Destacadas

### Productividad:
- **LOC/Hora:** 43.6 (Nivel Senior) ✅
- **Eficiencia:** 73.5% (Error estimación: +36%)

### Calidad:
- **Defectos/KLOC:** 12.0 (Meta: <10) ⚠️
- **Yield:** 58.3% (Meta: >70%) ⚠️

### Distribución del Tiempo:
- Codificación: 48.0%
- Pruebas: 26.2%
- Diseño: 15.3%
- Planificación: 6.5%
- Postmortem: 2.2%
- Compilación: 1.8%

---

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3 + Flask
- **Base de Datos:** SQLite
- **Frontend:** HTML/CSS (templates embebidos)
- **Metodología:** PSP 0.1
- **Control de versiones:** Git/GitHub

---

## 📈 Lecciones Aprendidas

### Fortalezas:
✅ Alta productividad (43.6 LOC/h)  
✅ Buena distribución de tiempo  
✅ Proyecto completado exitosamente

### Áreas de Mejora:
⚠️ Yield bajo (58.3% vs meta 70%)  
⚠️ Defectos/KLOC alto (12 vs meta <10)  
⚠️ Subestimación de tiempo (+36%)

### Recomendaciones para Próximos Proyectos:
1. Compilar cada 50 LOC
2. Revisar código antes de cada commit
3. Estimar +40% en Codificación y Pruebas
4. Usar checklists de diseño

---

## 👨‍💻 Autor

**Mateo Arroyave Martínez**  
Estudiante de Ingeniería de Sistemas  
Universidad Libre Seccional Pereira

---

## 📄 Licencia

Este proyecto fue desarrollado con fines educativos como parte del curso de Ingeniería de Software.

---

**Proyecto desarrollado:** Noviembre 2025  
**Metodología:** PSP 0.1 (Personal Software Process)  
**Resultado:** Proyecto exitoso con áreas de mejora identificadas
```

4. Scroll abajo
5. Mensaje del commit: `Actualizar README principal`
6. Click **"Commit changes"** (verde)

---

## 🎨 PASO 5: AGREGAR DESCRIPCIÓN Y TOPICS

### 5.1 Agregar Descripción

1. Estando en la página principal de tu repositorio
2. Busca el cuadro "About" en la columna derecha
3. Click en el **ícono de engranaje** ⚙️
4. En **Description** escribe:
   ```
   Sistema de Gestión de Biblioteca desarrollado con PSP - Proyecto Universitario
   ```
5. En **Website** (opcional): deja vacío o pon tu página
6. Click **"Save changes"**

### 5.2 Agregar Topics (Etiquetas)

1. En el mismo cuadro "About"
2. En **Topics**, agrega estas etiquetas (una por una):
   ```
   psp
   personal-software-process
   python
   flask
   sqlite
   software-engineering
   metrics
   biblioteca
   universidad-libre
   ```
3. Presiona Enter después de cada una
4. Click **"Save changes"**

---

## 🎯 PASO 6: CREAR .gitignore (Opcional pero recomendado)

### 6.1 Crear archivo

1. En la raíz del repositorio
2. Click **"Add file"** → **"Create new file"**
3. Nombre: `.gitignore`
4. Contenido:

```
# Python
__pycache__/
*.py[cod]
*.so
.Python
venv/
*.egg-info/

# Base de datos
*.db
*.sqlite
*.sqlite3
biblioteca.db

# IDEs
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Temporales
*.tmp
*.bak
```

5. Mensaje: `Agregar .gitignore`
6. Click **"Commit new file"**

---

## ✅ PASO 7: VERIFICAR TODO

### Checklist Final:

1. **Ir a la página principal del repo**
2. Verificar que veas:
   - [ ] 📁 Carpeta `excel` con el archivo .xlsx
   - [ ] 📁 Carpeta `informes` con 3 archivos .md
   - [ ] 📁 Carpeta `sistema-biblioteca` con archivos .py
   - [ ] 📄 README.md bien formateado
   - [ ] 📄 .gitignore
   - [ ] Description en el cuadro About
   - [ ] Topics agregados

### Navegar por el Repositorio:

- Click en cada carpeta para ver los archivos
- Click en los archivos .md para ver cómo se ven
- Verifica que el README principal se vea bien

---

## 🔗 COMPARTIR TU REPOSITORIO

### Tu URL será:
```
https://github.com/TU_USUARIO/proyecto-psp-biblioteca
```

### Puedes:
- Copiar el link y enviarlo por correo
- Agregarlo a tu CV
- Compartirlo en LinkedIn
- Usarlo como portafolio

---

## 📤 PASO 8: ACTUALIZAR ARCHIVOS EN EL FUTURO

### Agregar nuevos archivos:

1. Ir a la carpeta donde quieres agregarlo
2. **"Add file"** → **"Upload files"**
3. Arrastrar archivos
4. Commit

### Editar un archivo existente:

1. Click en el archivo
2. Click en el **ícono de lápiz** ✏️
3. Hacer cambios
4. Scroll abajo
5. Mensaje del commit
6. **"Commit changes"**

### Eliminar un archivo:

1. Click en el archivo
2. Click en los **tres puntos** (...)
3. **"Delete file"**
4. Confirmar commit

---

## 📸 CAPTURAS RECOMENDADAS

Para documentar tu proceso, toma screenshots de:

1. ✅ Repositorio creado
2. ✅ Carpetas organizadas
3. ✅ README principal
4. ✅ Topics agregados
5. ✅ Archivos subidos

---

## 🎉 RESULTADO FINAL

Tu repositorio debería verse así:

```
📦 proyecto-psp-biblioteca
│
├── 📄 README.md (con todo formateado bonito)
├── 📄 .gitignore
│
├── 📁 excel/
│   ├── 📄 README.md
│   └── 📊 PSP_CORREGIDO_SIN_ERRORES.xlsx
│
├── 📁 informes/
│   ├── 📄 README.md
│   ├── 📄 INFORME_FINAL_SIMPLE.md
│   ├── 📄 INFORME_EXPLICATIVO_METRICAS.md
│   └── 📄 GLOSARIO_PSP_COMPLETO.md
│
└── 📁 sistema-biblioteca/
    ├── 📄 README.md
    ├── 🐍 app.py
    ├── 🐍 models.py
    ├── 🐍 config.py
    ├── 📄 requirements.txt
    └── 📄 COMO_EJECUTAR.md
```

---

## 💡 TIPS IMPORTANTES

### ✅ Buenas Prácticas:

1. **Mensajes de commit claros:**
   - ✅ "Agregar Excel con métricas PSP"
   - ❌ "asdf"

2. **Nombres de archivo descriptivos:**
   - ✅ `INFORME_FINAL_SIMPLE.md`
   - ❌ `documento1.md`

3. **Organización:**
   - Usa carpetas lógicas
   - Un README por carpeta explicando su contenido

### ⚠️ Evitar:

- No subir archivos muy grandes (>100MB)
- No subir contraseñas o tokens
- No subir bases de datos con datos sensibles

---

## 🔄 CLONAR TU REPOSITORIO

Si quieres descargarlo en otra computadora:

### Opción 1: Descargar ZIP

1. En tu repo, click **"Code"** (botón verde)
2. Click **"Download ZIP"**
3. Descomprimir

### Opción 2: Con Git (si lo tienes instalado)

```bash
git clone https://github.com/TU_USUARIO/proyecto-psp-biblioteca.git
```

-
---

---

**Guía creada para:** Mateo Arroyave  
**Método:** Todo desde la web, sin comandos  
**Tiempo estimado:** 15-20 minutos  
**Dificultad:** Fácil ⭐
