import datetime
import airflow
from airflow.operators import bash_operator
from airflow.providers.sqlite.operators.sqlite import SqliteOperator

default_args = {
    'start_date': datetime.datetime.now(),
}

with airflow.DAG('procesar_usuario', schedule_interval='@daily',
        dafault_args = default_args,
        catchup=False) as dag:

# Definir tareas/operadores

    crear_tabla = SqliteOperator.SqliteOperator(
            task_id = 'crear_tabla', 
            sqlite_conn_id = 'db_sqlite',
            sql = '''
                CREATE TABLE usuarios(
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                pais TEXT NOT NULL,
                usuario TEXT NOT NULL,
                contraseña TEXT NOT NULL,
                email TEXT NOT NULL PRIMARY KEY
            );
            '''
    )