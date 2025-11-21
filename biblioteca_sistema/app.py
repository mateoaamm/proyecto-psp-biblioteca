"""
Aplicación Flask - Sistema de Gestión de Biblioteca
Desarrollado por: Mateo Arroyave
Proyecto PSP - Sistema de Biblioteca Universitaria
"""
from flask import Flask, render_template_string, request, redirect, url_for, flash, jsonify
from models import db, Libro, Usuario, Prestamo
from config import Config
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


# ==================== PLANTILLAS HTML ====================

HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Biblioteca - Mateo Arroyave</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        h1 {
            color: #667eea;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 40px;
            font-size: 1.1em;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        .stat-number {
            font-size: 3em;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .stat-label {
            font-size: 1.1em;
            opacity: 0.9;
        }
        .menu {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .menu-item {
            background: #f8f9fa;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            text-decoration: none;
            color: #333;
            transition: all 0.3s;
            border: 2px solid transparent;
        }
        .menu-item:hover {
            transform: translateY(-5px);
            border-color: #667eea;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        .menu-item h3 {
            color: #667eea;
            margin-bottom: 10px;
        }
        .alert {
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 5px;
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #eee;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📚 Sistema de Biblioteca</h1>
        <p class="subtitle">Desarrollado con PSP por Mateo Arroyave</p>
        
        {% with messages = get_flashed_messages() %}
        {% if messages %}
            {% for message in messages %}
            <div class="alert">{{ message }}</div>
            {% endfor %}
        {% endif %}
        {% endwith %}
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">{{ total_libros }}</div>
                <div class="stat-label">Libros en Catálogo</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{{ total_usuarios }}</div>
                <div class="stat-label">Usuarios Activos</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{{ prestamos_activos }}</div>
                <div class="stat-label">Préstamos Activos</div>
            </div>
        </div>
        
        <div class="menu">
            <a href="/libros" class="menu-item">
                <h3>📖 Gestión de Libros</h3>
                <p>Agregar, editar y consultar libros del catálogo</p>
            </a>
            <a href="/usuarios" class="menu-item">
                <h3>👥 Gestión de Usuarios</h3>
                <p>Registrar y administrar usuarios</p>
            </a>
            <a href="/prestamos" class="menu-item">
                <h3>📋 Préstamos</h3>
                <p>Registrar préstamos y devoluciones</p>
            </a>
            <a href="/api/datos" class="menu-item">
                <h3>📊 API / Datos</h3>
                <p>Acceso a datos en formato JSON</p>
            </a>
        </div>
        
        <div class="footer">
            <p><strong>Sistema de Gestión de Biblioteca Universitaria</strong></p>
            <p>Proyecto PSP 0.1 | Mateo Arroyave | 2025</p>
            <p>💻 Tecnologías: Python 3 + Flask + SQLite</p>
        </div>
    </div>
</body>
</html>
"""

LIBROS_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Gestión de Libros</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            padding: 20px;
        }
        .container { max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
        h1 { color: #333; margin-bottom: 20px; }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            margin: 10px 5px;
        }
        .btn:hover { background: #5568d3; }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th { background: #667eea; color: white; }
        .disponible { color: green; font-weight: bold; }
        .no-disponible { color: red; }
        form { background: #f8f9fa; padding: 20px; border-radius: 5px; margin-top: 20px; }
        input { padding: 8px; margin: 5px 0; width: 100%; max-width: 300px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📖 Gestión de Libros</h1>
        <a href="/" class="btn">🏠 Inicio</a>
        
        <form method="POST" action="/libros/agregar">
            <h3>Agregar Nuevo Libro</h3>
            <input type="text" name="isbn" placeholder="ISBN (OPCIONAL - puedes dejarlo vacío)" >
            <small style="display:block; margin: -5px 0 10px 0; color: #666;">
                💡 Puedes dejar este campo vacío o usar cualquier código
            </small>
            <input type="text" name="titulo" placeholder="Título" required>
            <input type="text" name="autor" placeholder="Autor" required>
            <input type="text" name="editorial" placeholder="Editorial">
            <input type="number" name="anio" placeholder="Año">
            <input type="number" name="total" placeholder="Cantidad" value="1" min="1">
            <button type="submit" class="btn">➕ Agregar Libro</button>
        </form>
        
        <h2>📚 Catálogo Actual</h2>
        <table>
            <tr>
                <th>ISBN</th>
                <th>Título</th>
                <th>Autor</th>
                <th>Editorial</th>
                <th>Año</th>
                <th>Disponibles/Total</th>
                <th>Estado</th>
            </tr>
            {% for libro in libros %}
            <tr>
                <td>{{ libro.isbn }}</td>
                <td><strong>{{ libro.titulo }}</strong></td>
                <td>{{ libro.autor }}</td>
                <td>{{ libro.editorial or '-' }}</td>
                <td>{{ libro.anio or '-' }}</td>
                <td>{{ libro.disponibles }}/{{ libro.total }}</td>
                <td>
                    {% if libro.disponibles > 0 %}
                    <span class="disponible">✓ Disponible</span>
                    {% else %}
                    <span class="no-disponible">✗ Prestado</span>
                    {% endif %}
                </td>
            </tr>
            {% else %}
            <tr><td colspan="7" style="text-align:center;">No hay libros registrados</td></tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>
"""


# ==================== RUTAS ====================

@app.route('/')
def index():
    """Página principal"""
    total_libros = Libro.query.count()
    total_usuarios = Usuario.query.filter_by(activo=True).count()
    prestamos_activos = Prestamo.query.filter_by(estado='activo').count()
    
    return render_template_string(
        HOME_TEMPLATE,
        total_libros=total_libros,
        total_usuarios=total_usuarios,
        prestamos_activos=prestamos_activos
    )


@app.route('/libros')
def libros():
    """Listar libros"""
    todos_libros = Libro.query.order_by(Libro.titulo).all()
    return render_template_string(LIBROS_TEMPLATE, libros=todos_libros)


@app.route('/libros/agregar', methods=['POST'])
def agregar_libro():
    """Agregar nuevo libro"""
    try:
        isbn = request.form.get('isbn', '').strip()
        
        # Si no tiene ISBN, generar uno automático
        if not isbn:
            isbn = f"AUTO-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        else:
            # Limpiar el ISBN (quitar espacios y guiones)
            isbn = isbn.replace('-', '').replace(' ', '')
        
        # Verificar si ya existe
        if Libro.query.filter_by(isbn=isbn).first():
            flash('❌ Ya existe un libro con ese ISBN.')
            return redirect(url_for('libros'))
        
        nuevo_libro = Libro(
            isbn=isbn,
            titulo=request.form.get('titulo'),
            autor=request.form.get('autor'),
            editorial=request.form.get('editorial'),
            anio=request.form.get('anio', type=int),
            total=request.form.get('total', type=int, default=1),
            disponibles=request.form.get('total', type=int, default=1)
        )
        
        db.session.add(nuevo_libro)
        db.session.commit()
        
        flash(f'✅ Libro "{nuevo_libro.titulo}" agregado exitosamente.')
    except Exception as e:
        db.session.rollback()
        flash(f'❌ Error: {str(e)}')
    
    return redirect(url_for('libros'))


@app.route('/usuarios')
def usuarios():
    """Listar usuarios"""
    return "<h1>Usuarios</h1><p>En desarrollo...</p><a href='/'>Volver</a>"


@app.route('/prestamos')
def prestamos():
    """Listar préstamos"""
    return "<h1>Préstamos</h1><p>En desarrollo...</p><a href='/'>Volver</a>"


@app.route('/api/datos')
def api_datos():
    """API con datos del sistema"""
    libros_list = [
        {
            'isbn': l.isbn,
            'titulo': l.titulo,
            'autor': l.autor,
            'disponibles': l.disponibles
        } for l in Libro.query.all()
    ]
    
    return jsonify({
        'proyecto': 'Sistema de Biblioteca',
        'desarrollador': 'Mateo Arroyave',
        'metodologia': 'PSP 0.1',
        'total_libros': len(libros_list),
        'total_usuarios': Usuario.query.count(),
        'prestamos_activos': Prestamo.query.filter_by(estado='activo').count(),
        'libros': libros_list
    })


@app.cli.command()
def init_db():
    """Inicializar la base de datos"""
    db.create_all()
    print("✅ Base de datos creada exitosamente")


@app.cli.command()
def seed():
    """Poblar con datos de ejemplo"""
    db.create_all()
    
    # Libros de ejemplo
    libros_ejemplo = [
        Libro(isbn='9780134685991', titulo='Effective Java', autor='Joshua Bloch', 
              editorial='Addison-Wesley', anio=2018, total=3, disponibles=3),
        Libro(isbn='9780132350884', titulo='Clean Code', autor='Robert C. Martin', 
              editorial='Prentice Hall', anio=2008, total=2, disponibles=2),
        Libro(isbn='9781449355739', titulo='Learning Python', autor='Mark Lutz', 
              editorial="O'Reilly", anio=2013, total=2, disponibles=2),
    ]
    
    for libro in libros_ejemplo:
        if not Libro.query.filter_by(isbn=libro.isbn).first():
            db.session.add(libro)
    
    # Usuarios de ejemplo
    usuarios_ejemplo = [
        Usuario(codigo='EST001', nombre='Mateo', apellido='Arroyave', 
                email='mateo@universidad.edu', tipo='estudiante'),
        Usuario(codigo='EST002', nombre='Ana', apellido='García', 
                email='ana@universidad.edu', tipo='estudiante'),
    ]
    
    for usuario in usuarios_ejemplo:
        if not Usuario.query.filter_by(codigo=usuario.codigo).first():
            db.session.add(usuario)
    
    db.session.commit()
    print("✅ Datos de ejemplo agregados")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    print("\n" + "="*60)
    print("🚀 INICIANDO SISTEMA DE BIBLIOTECA")
    print("="*60)
    print("📚 Proyecto: Sistema de Gestión de Biblioteca")
    print("👨‍💻 Desarrollador: Mateo Arroyave")
    print("📊 Metodología: PSP 0.1")
    print("="*60)
    print("\n🌐 Abre tu navegador en: http://localhost:5000")
    print("⏹️  Para detener: Presiona Ctrl+C\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
