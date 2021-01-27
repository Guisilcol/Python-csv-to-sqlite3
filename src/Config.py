
config = {
    "diretorios": [
        "./inputFolder",
        "./outputFolder"
    ],
    "sqliteDbName": "database.db",
    "logFilepath": "./log.log",
    "isInDevelopment": False
}


def get_config_dict() -> dict:
    return config