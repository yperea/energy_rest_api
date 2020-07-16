"""
    client.py
    -------------
    Este modulo contiene la clase CustomerModel la cual aloja y maneja 
    las operaciones contra la entidad 'Clientes' en la base de datos
"""
from db import db


class CustomerModel(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(500))

    """
    La clase CustomerModel almacena y maneja las operaciones 
    contra la entidad 'Clientes' en la base de datos
    """
    def __init__(self, name: str, description: str):
        """
        Inicializa la clase Client con la informacion basica del cliente.
        """
        self.name = name
        self.description = description

    def json(self):
        """
        Serializa el objeto CustomerModel en formato json.
        """
        return {'id': self.id, 'name': self.name, 'description': self.description}

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()