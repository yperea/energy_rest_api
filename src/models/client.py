"""
    client.py
    -------------
    Este modulo contiene la clase ClientModel la cual aloja y maneja 
    las operaciones contra la entidad 'Clientes' en la base de datos
"""

class ClientModel():
    """
    La clase ClientModel almacena y maneja las operaciones 
    contra la entidad 'Clientes' en la base de datos
    """
    def __init__(self, _id: int, name: str, description: str):
        """
        Inicializa la clase Client con la informacion basica del cliente.
        """
        self.id = _id
        self.name = name
        self.description = description

    def json(self):
        """
        Serializa el objeto ClientModel en formato json.
        """
        return {'id': self.id, 'name': self.name, 'description': self.description}
