def get_all_table_names(db, verbose=True):
    table_names_list = []
    for clazz in db.Model._decl_class_registry.values():
        try:
            table_names_list.append(clazz.__tablename__)
        except:
            pass

    if verbose:
        print("\nTable Names:")
        for table_name in table_names_list:
            print("\t{}".format(table_name))

    return table_names_list


def make_db_file(db, db_name):
    import os 

    file_names = os.listdir()
    n_files = len(file_names)
    db_exists = False
    for idx_file in range(n_files):
        if db_name in file_names[idx_file]:
            db_exists = True
            break

    print("\ndb_exists: {}\n".format(db_exists))
    if not db_exists:
        db.create_all()


def set_db_uri(app, db_type: str, db_name: str, set_relative_path=True):
    """
    :param app:
    :param db_type: (str) "sqlite"
    :param db_name:
    :param set_relative_path: (bool)
    :return:
    """

    if set_relative_path:
        path_setting = "///"
    else:   # absolute setting
        path_setting = "////"

    database_uri = "{0}:{1}{2}.db".format(db_type,
                                          path_setting,
                                          db_name)
    print("database_uri:", database_uri)

    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

    return app