import spike80.dao.DaoJob as dj

class Service:
    def __int__(self, id_service, id_job, id_hostage):
        self.id_service = id_service
        self.id_job = id_job
        self.id_hostage = id_hostage

    def  get_all_services(self):
        connection = dj.DaoJob()
        registers = connection.listaAtendimento()
        services = []
        for i in range(len(registers)):
            service = Service()
            service.id_service = registers[i][0]
            service.id_job = registers[i][1]
            service.id_hostage = registers[i][2]
            services.append(service)

        return services

    def get_service(self):
        connection = dj.DaoJob()
        registry = connection.selecionaAtendimento()
        service = Service()
        service.id_service = registry[0]
        service.id_job = registry[1]
        service.id_hostage = registry[2]

        return service

    def update_service(self, id_service, id_job, id_hostage):
        record_to_insert = (id_service, id_job, id_hostage)
        service = Service()
        service.id_service = record_to_insert[0]
        service.id_job = record_to_insert[1]
        service.id_hostage = record_to_insert[2]

        dj.DaoJob().atualizaAtendimento(service.id_service, service.id_service,
                                        service.id_hostage)

    def insert_service(self, id_service, id_job, id_hostage):
        record_to_insert = (id_service, id_job, id_hostage)
        service = Service()
        service.id_service = record_to_insert[0]
        service.id_job = record_to_insert[1]
        service.id_hostage = record_to_insert[2]

        dj.DaoJob().atualizaAtendimento(service.id_service, service.id_service,
                                        service.id_hostage)

    def getId_service(self):
        return self.id_service

    def getId_job(self):
        return self.id_job

    def getId_hostage(self):
        return self.id_hostage


