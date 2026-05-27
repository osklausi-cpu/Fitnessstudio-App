import threading

class Database:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        return Database()

    def query(self, sql):
        print(f"Executing: {sql}")