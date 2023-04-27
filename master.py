import hashlib, os.path


class MasterPassword:
    def __init__(self):
        self.key = None

    def load(self, password= "", path="key"):
        if os.path.exists(path) != True:
            return None
        else:
            with open(path, 'r') as file:
                self.key = file.read()
            h = hashlib.new('sha256')
            h.update(password.encode())
            self.check = h.hexdigest()
            if self.check != self.key:
                return False
            else:
                return True

    def create_master_psswd(self, password="", path="key"):
        if password == "" or len(password) > 25:
            print("This can not be empty or longer than 25 characters")
        #elif len(password) > 25:
        #    print("This can not be empty or longer than 25 characters")
        else:
            h = hashlib.new('sha256')
            h.update(password.encode())
            self.key = h.hexdigest()
            with open(path, "w") as file:
                file.write(self.key)
            return path