import json


class Panda:
    def __init__(self, name, email, gender):
        self.__name = name
        self.__gender = gender
        self.__email = email

    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def __str__(self):
        return "{} - {} - {}".format(self.name(), self.email(), self.gender())

    def __repr__(self):
        return "Panda('{}', '{}', '{}')".format(self.name(), self.email(), self.gender())

    def to_json(self):
        return self.__repr__()

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return self.name() == other.name() and self.email() == other.email() \
            and self.gender() == other.gender()


class PandaSocialNetwork:
        def __init__(self):
            self.network = {}

        def has_panda(self, panda):
            return panda in self.network

        def add_panda(self, panda):
            if self.has_panda(panda):
                raise Exception("Panda already there")

            self.network[panda] = []

        def are_friends(self, panda1, panda2):
            if panda1 not in self.network or panda2 not in self.network:
                return False

            return panda1 in self.network[panda2] and \
                panda2 in self.network[panda1]

        def make_friends(self, panda1, panda2):
            if not self.has_panda(panda1):
                self.add_panda(panda1)

            if not self.has_panda(panda2):
                self.add_panda(panda2)

            if self.are_friends(panda1, panda2):
                raise Exception("Pandas are already friends")

            self.network[panda1].append(panda2)
            self.network[panda2].append(panda1)

        def panda_connections(self, panda):
            print(self.network)
            connections = {}
            q = []
            visited = set()

            q.append((0, panda))
            visited.add(panda)

            while len(q) != 0:
                panda_data = q.pop(0)
                current_level = panda_data[0]
                current_node = panda_data[1]
                print(current_node)
                connections[current_node] = current_level

                for neighbour in self.network[current_node]:
                    # print(neighbour)
                    if neighbour not in visited:
                        visited.add(neighbour)
                        q.append((current_level + 1, neighbour))

            return connections

            def connection_level(self, panda1, panda2):
                panda_table = self.panda_connections(panda1)

                if panda2 not in panda_table:
                    return -1

                return panda_table[panda2]

            def genders_in_network(self, level, gender, panda):
                panda_table = self.panda_connections(panda)
                counter = 0

                for panda in panda_table:
                    p_level = panda_table[panda]
                    if p_level != 0 and p_level <= level and panda.gender() == gender:
                        counter += 1

                return counter

        def __repr__(self):
            for_save = {}

            for panda in self.network:
                friends = [repr(panda_friend) for panda_friend in self.network[panda]]
                for_save[repr(panda)] = friends

            return json.dumps(for_save, indent=True)

        def save(self, filename):
            with open(filename, "w") as f:
                f.write(self.__repr__())

        @staticmethod
        def load(filename):
            network = PandaSocialNetwork()
            with open(filename, "r") as f:
                contents = f.read()
                json_network = json.loads(contents)

                for panda in json_network:
                    for friends in json_network[panda]:
                        # ВИЕ ТРЯБВА САМИ ДА ГО НАПРАВИТЕ ПО НЯКАКЪВ НАЧИН
                        p1 = eval(panda)
                        p2 = eval(friends)
                        if not network.are_friends(p1, p2):
                            network.make_friends(p1, p2)

            return network


# A -> B -> C -> D -> A
p1 = Panda("A", "asda", "male")
p2 = Panda("B", "asdasd", "female")
p3 = Panda("C", "asdads", "male")
p4 = Panda("D", "asdada", "female")

network = PandaSocialNetwork()
network.make_friends(p1, p2)
network.make_friends(p2, p3)
network.make_friends(p3, p4)
network.make_friends(p4, p1)

network.save("network.json")
network2 = PandaSocialNetwork.load("network.json")

# print(repr(network2))
result = network2.panda_connections(p1)
print(json.dumps({repr(panda): result[panda] for panda in result}, indent=True))
