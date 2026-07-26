import os
import shutil

# Rename the database file to backup
if os.path.exists('db.sqlite3'):
    shutil.move('db.sqlite3', 'db.sqlite3.backup')
    print('Database renamed to db.sqlite3.backup')
else:
    print('Database file not found')
