class Attribute:
    def __init__(self, name, range, discrete):
        self.name = name
        self.range = range
        self.discrete = discrete
        return

    @staticmethod
    def read_attribute(filename):
        f = open(filename)
        attributes = []
        all_lines = f.readlines()
        for line in all_lines:
            tmp = line.split()
            name = tmp[0]
            range = tmp[1:]
            discrete = True
            if tmp[1] == "continuous":
                range = []
                discrete = False
            attributes.append(Attribute(name, range, discrete))
        return attributes

    @staticmethod
    def empty(attributes):
        if len(attributes) == 0:
            return True
        for attr in attributes:
            if attr.range[0] != "#unique":
                return False
        return True

    @staticmethod
    def remove(attributes, attribute):
        for i in range(len(attributes)):
            if attribute.name == attributes[i].name:
                del attributes[i]
                break
        return

