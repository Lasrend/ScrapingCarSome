from orator import DatabaseManager, Schema
from main import PARAMS
database = PARAMS.DATABASE

config = {
    'postgresql': {
        'driver': 'postgres',
        'host': database.host,
        'database': database.db,
        'user': database.username,
        'password': database.password,
        'prefix': ''
    }
}

db = DatabaseManager(config)
schema = Schema(db)
from orator import Model
Model.set_connection_resolver(db)
