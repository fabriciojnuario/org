import spike80.dao.DaoRoom as dr

class Room:

    def __int__(self, nroom, floor, troom, status):
        self.nroom = nroom
        self.floor = floor
        self.troom = troom
        self.status = status

    def getNroom(self):
        return self.nroom

    def getFloor(self):
        return self.floor

    def getTroom(self):
        return self.troom

    def getStatus(self):
        return self.status

    def get_all_rooms(self):
        connection = dr.DaoRoom()
        registers = connection.listaQuartos()
        rooms = []
        for i in range(len(registers)):
            room = Room()
            room.nroom = registers[i][0]
            room.floor = registers[i][1]
            room.troom = registers[i][2]
            room.status = registers[i][3]
            rooms.append(room)

        return rooms

    def get_room(self, num_quarto):
        connection = dr.DaoRoom()
        registry = connection.selecionaQuarto(num_quarto)
        room = Room()
        room.nroom = registry[0]
        room.floor = registry[1]
        room.troom = registry[2]
        room.status = registry[3]

        return room

    def insert_room(self, num_quarto, andar, tipo_quarto, status):
        connection = dr.DaoRoom()
        room = Room()
        room.nroom = num_quarto
        room.floor = andar
        room.troom = tipo_quarto
        room.status = status
        connection.inserirQuarto(room.nroom, room.floor, room.troom, room.status)

    def update_room(self, num_quarto, andar, tipo_quarto, status):
        connection = dr.DaoRoom()
        room = Room()
        room.nroom = num_quarto
        room.floor = andar
        room.troom = tipo_quarto
        room.status = status
        connection.atualizaQuarto(room.floor, room.troom, room.status, room.nroom)

    def delete_room(self, num_quarto):
        connection = dr.DaoRoom()
        room = Room()
        room.nroom = num_quarto
        connection.excluirQuarto(room.nroom)
