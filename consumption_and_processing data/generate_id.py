import hashlib
from logger import Logger
logger = Logger.get_logger()



class IDGenerator:
    def __init__(self,hash_base: list):
        self.hash_base = hash_base

    def generate_unique_id(self,file_data):
        result = hashlib.sha256(f"{file_data[self.hash_base[0]]}{file_data[self.hash_base[1]]}{file_data[self.hash_base[2]]}".encode()).hexdigest()
        logger.info("id generated successfully")
        return result






