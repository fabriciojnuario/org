import spike80.dao.DaoService as ds


class Job:
    def __int__(self):
        print("")

    def getId_job(self):
        return self.id_job

    def getPrice(self):
        return self.price

    def getDescription(self):
        return self.description

    def get_all_jobs(self):
        connection = ds.DaoService()
        registers = connection.listaServico()
        jobs = []
        for i in range(len(registers)):
            job = Job()
            job.id_job = registers[i][0]
            job.description = registers[i][1]
            job.price = registers[i][2]
            jobs.append(job)

        return jobs

    def get_job(self, id_job):
        registry = ds.DaoService().selecionaServico(id_job,)
        job = Job()
        job.id_job = registry[0]
        job.description = registry[1]
        job.price = registry[2]

        return job

    def update_job(self, id_job, description, price):
        registry_to_insert = id_job, description, price
        connection = ds.DaoService()
        job = Job()
        job.id_job = registry_to_insert[0]
        job.description = registry_to_insert[1]
        job.price = registry_to_insert[2]
        connection.atualizaServico(job.id_job, job.description, job.price)

    def insert_job(self, id_job, description, price):
        record_to_insert = (id_job, description, price)
        job = Job()
        job.id_job = record_to_insert[0]
        job.description = record_to_insert[1]
        job.price = record_to_insert[2]
        ds.DaoService().inserirServico(job.id_job, job.description, job.price)

    def delete_job(self, id_job):
        job = Job()
        job.id_job = id_job
        ds.DaoService().excluiServico(id_job,)

    def __str__(self):
        return f"{self.id_job}+{self.description}"

