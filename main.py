from managers.manager_a import PreProccess
from managers.manager_b import ManagerSendToMongoElastic
from managers.manager_c import STTSaveToElastic
from managers.manager_d import SendClassifiedToElastic

class Main:
    def __init__(self):
        self.path = '/Users/petahiam/podcasts'
        self.a = PreProccess(self.path)
        self.b = ManagerSendToMongoElastic()
        self.c = STTSaveToElastic()
        self.d = SendClassifiedToElastic('unra')



    def run_all(self):
        self.a.run()
        self.b.run()
        self.c.run()
        self.d.run()


if __name__ == '__main__':
    boom = Main()
    boom.run_all()


