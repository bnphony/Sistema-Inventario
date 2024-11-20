import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/sqlite/db.sqlite3'),
    }
}

# Se requiere instalar la libreria psycopg2
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'inventario_victoria',
        'USER': 'postgres',
        'PASSWORD': '123456789',
        'HOST': 'localhost',
        'PORT': '5433'
    }
}

# Se requiere instalar la liberia mysqlclient

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'certificado',
        'USER': 'hola',
        'PASSWORD': 'Touhou33',
        'HOST': '127.0.0.1',
        'PORT': '3308',
        # 'OPTIONS': {
        #     'sql_mode': 'traditional',
        # }
    }
}