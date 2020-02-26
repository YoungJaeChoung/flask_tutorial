def make_db_file(db, db_name):
    import os 

    file_names = os.listdir()
    n_files = len(file_names)
    db_exists = False
    for idx_file in range(n_files):
        if db_name in file_names[idx_file]:
            db_exists = True
            break

    print("db_exists: {}".format(db_exists))
    if not db_exists:
        db.create_all()
