
import os
import mysql.connector
from mysql.connector import Error
from flask import Flask

app = Flask(__name__)

@app.route('/')
def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        if connection.is_connected():
            return "✅ Conexión exitosa a MySQL desde App Service!"
    except Error as e:
        return f"❌ Error de conexión: {e}"
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
