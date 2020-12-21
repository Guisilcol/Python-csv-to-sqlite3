import controller.MainProcess as MainProcess

if __name__ == "__main__":
    welcome_message = "********** CSV to SQLITE3 **********"
    print(welcome_message)
    MainProcess.read_csv_and_load_sqlite3()