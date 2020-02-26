def check_database_uri_str(database_uri):
    is_correct = database_uri == "SQLALCHEMY_DATABASE_URI"
    return is_correct