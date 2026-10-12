import sqlite3
import pytest

# Configurar una base de datos en memoria o local para la prueba
@pytest.fixture
def db_connection():
    # Conectar a una base de datos SQLite (se crea localmente para la prueba)
    conn = sqlite3.connect("test_users.db")
    cursor = conn.cursor()
    
    # Crear una tabla de ejemplo para usuarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            job TEXT NOT NULL
        )
    """)
    conn.commit()
    
    yield conn # Entregar la conexión a la prueba
    
    # Limpieza después de la prueba
    cursor.execute("DROP TABLE IF EXISTS users")
    conn.commit()
    conn.close()

def test_user_persistence_in_database(db_connection):
    cursor = db_connection.cursor()
    
    # 1. Simular la inserción de un registro (como si viniera de una API POST exitosa)
    cursor.execute("INSERT INTO users (name, job) VALUES (?, ?)", ("Ivan Suarez Alva", "Lead QA Automation Engineer"))
    db_connection.commit()
    
    # 2. Ejecutar un SELECT para verificar la integridad de los datos guardados
    cursor.execute("SELECT name, job FROM users WHERE name = ?", ("Ivan Suarez Alva",))
    user_record = cursor.fetchone()
    
    # 3. Aserciones para validar que el registro existe y coincide exactamente
    assert user_record is not None, "User record was not found in the database!"
    assert user_record[0] == "Ivan Suarez Alva", "Stored name does not match"
    assert user_record[1] == "Lead QA Automation Engineer", "Stored job title does not match"

def test_user_update_persistence_in_database(db_connection):
    cursor = db_connection.cursor()
    
    # 1. Insertar un usuario inicial
    cursor.execute("INSERT INTO users (name, job) VALUES (?, ?)", ("Ivan Suarez Alva", "Junior QA"))
    db_connection.commit()
    
    # 2. Simular una actualización de datos (como una petición PUT)
    cursor.execute("UPDATE users SET job = ? WHERE name = ?", ("Lead QA Automation Engineer", "Ivan Suarez Alva"))
    db_connection.commit()
    
    # 3. Consultar la base de datos para verificar el cambio
    cursor.execute("SELECT job FROM users WHERE name = ?", ("Ivan Suarez Alva",))
    updated_record = cursor.fetchone()
    
    # 4. Aserción para verificar que el puesto se actualizó correctamente en la DB
    assert updated_record[0] == "Lead QA Automation Engineer", "Database update persistence failed!"