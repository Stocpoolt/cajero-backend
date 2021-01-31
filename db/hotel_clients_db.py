from typing import Dict
from pydantic import BaseModel

class ClientsInDB(BaseModel):
    nombre: str
    apellido: str
    email: str
    telefono: int

database_clients = Dict[str,ClientsInDB]

database_clients = {
    "hugotamayo@gmail.com":ClientsInDB(**{"nombre":"Hugo", "apellido":"Tamayo",
    "email": "Hugotamayo@gmail.com", "telefono":555}),
    "pacotamayo@gmail.com":ClientsInDB(**{"nombre":"Paco", "apellido":"Tamayo",
    "email": "pacotamayo@gmail.com", "telefono":666}),
    "luistamayo@gmail.com":ClientsInDB(**{"nombre":"Luis", "apellido":"Tamayo",
    "email": "luistamayo@gmail.com", "telefono":777})
}

def add_clients(clients_in_db:ClientsInDB):
    database_clients[clients_in_db.email] = ClientsInDB(**{"nombre":clients_in_db.nombre, "apellido":clients_in_db.apellido,
    "email":clients_in_db.email,"telefono":clients_in_db.telefono})
    return database_clients

def get_clients(email: str):
    if email in database_clients.keys():
        return database_clients[email]
    else:
        return None
