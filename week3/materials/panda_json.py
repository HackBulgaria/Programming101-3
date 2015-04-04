import json


class Panda:
    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.email, self.gender)

    def __repr__(self):
        return "Panda('{}', '{}', '{}')".format(self.name,
                                                self.email, self.gender)


def serialize_to(path, data):
    json_string = json.dumps(data, indent=4)

    with open(path, "w") as f:
        f.write(json_string)


def unserialize_from(path):
    with open(path, "r") as f:
        contents = f.read()

    return json.loads(contents)

p = Panda("Ivo", "ivo@pandamail.com", "male")
serialize_to("panda.json", repr(p))
print(unserialize_from("panda.json"))
