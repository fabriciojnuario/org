class Job:
    def __int__(self, id_job, price, description):
        self.id_job = id_job
        self.price = price
        self.description = description

    def getId_job(self):
        return self.id_job

    def getPrice(self):
        return self.price

    def getDescription(self):
        return self.description


