"""
Modelos de datos para el sistema de biblioteca
"""
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Libro(db.Model):
    """Modelo para gestión de libros"""
    __tablename__ = 'libros'
    
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), unique=True, nullable=False, index=True)
    titulo = db.Column(db.String(200), nullable=False, index=True)
    autor = db.Column(db.String(100), nullable=False)
    editorial = db.Column(db.String(100))
    anio = db.Column(db.Integer)
    disponibles = db.Column(db.Integer, default=1)
    total = db.Column(db.Integer, default=1)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Libro {self.titulo}>'
    
    def esta_disponible(self):
        """Verificar si hay ejemplares disponibles"""
        return self.disponibles > 0
    
    @staticmethod
    def validar_isbn(isbn):
        """Validar formato ISBN-13"""
        isbn = isbn.replace('-', '').replace(' ', '')
        if len(isbn) != 13 or not isbn.isdigit():
            return False
        
        try:
            suma = 0
            for i, digito in enumerate(isbn[:-1]):
                suma += int(digito) * (1 if i % 2 == 0 else 3)
            check_digit = (10 - (suma % 10)) % 10
            return check_digit == int(isbn[-1])
        except:
            return False


class Usuario(db.Model):
    """Modelo para gestión de usuarios"""
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    activo = db.Column(db.Boolean, default=True)
    
    prestamos = db.relationship('Prestamo', backref='usuario', lazy='dynamic')
    
    def __repr__(self):
        return f'<Usuario {self.codigo}>'
    
    def puede_prestar(self, max_prestamos=3):
        """Verificar si puede realizar más préstamos"""
        if not self.activo:
            return False
        activos = self.prestamos.filter_by(estado='activo').count()
        return activos < max_prestamos


class Prestamo(db.Model):
    """Modelo para gestión de préstamos"""
    __tablename__ = 'prestamos'
    
    id = db.Column(db.Integer, primary_key=True)
    libro_id = db.Column(db.Integer, db.ForeignKey('libros.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    fecha_prestamo = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_devolucion_estimada = db.Column(db.DateTime, nullable=False)
    fecha_devolucion_real = db.Column(db.DateTime)
    multa = db.Column(db.Float, default=0.0)
    estado = db.Column(db.String(20), default='activo')
    
    libro = db.relationship('Libro', backref='prestamos_libro')
    
    def __repr__(self):
        return f'<Prestamo {self.id}>'
    
    def calcular_multa(self, multa_por_dia=1000):
        """Calcular multa por retraso"""
        if self.estado == 'devuelto' and self.fecha_devolucion_real:
            if self.fecha_devolucion_real > self.fecha_devolucion_estimada:
                dias = (self.fecha_devolucion_real - self.fecha_devolucion_estimada).days
                self.multa = dias * multa_por_dia
        return self.multa
