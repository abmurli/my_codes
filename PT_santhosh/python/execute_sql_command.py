import sqlite3
import sys

try:
    db_name = sys.argv[1]
    sql_file = sys.argv[2]
    if not str(sql_file).endswith('.sql'):
        print("Kindly input the sql file name with .sql extension")
        sys.exit(1)
except IndexError as err:
    print("Expected 2 arguements \n1.db_name\n2.sql_file_name\nUsage: "
          "python3 execute_sql_command <db_name> <sql_file_name>")
    sys.exit(1)
except Exception as err:
    print("ERROR: Unexpected\n{}".format(err))
    sys.exit(1)

try:
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    sql_file = open(sql_file)
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)
except FileNotFoundError as err:
    print("ERROR: Sql file not found\ncheck if the sql file \'{}\' exist".format(sql_file))
    sys.exit(1)
except Exception as err:
    print("ERROR: Unexpected\n{}".format(err))
    sys.exit(1)
