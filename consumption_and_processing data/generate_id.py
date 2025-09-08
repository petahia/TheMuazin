import hashlib

class IDGenerator:
    def __init__(self,hash_base):
        self.hash_base = hash_base

    def generate_unique_id(self,file_data):
        return hashlib.sha256(self.hash_base.encode()).hexdigest()







hash_base = f"{file_data['name']}_{file_data['size']}_{file_data['creation_date']}"