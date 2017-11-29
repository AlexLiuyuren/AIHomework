class Attribute:
    def __init__(self, name, range, discrete):
        self.name = name
        self.range = range
        self.discrete = discrete
        # for continuous
        self.value = 0
        return

    @staticmethod
    def read_attribute(filename, data):
        f = open(filename)
        attributes = []
        all_lines = f.readlines()
        i = 0
        for line in all_lines:
            tmp = line.split()
            name = tmp[0]
            irange = tmp[1:]
            discrete = True
            if tmp[1] == "continuous":
                discrete = False
                irange = []
                for d in data:
                    if d.value[i] != '?':
                        d.value[i] = float(d.value[i])
                        if d.value[i] not in irange:
                            irange.append(d.value[i])
                sorted(irange)
            attributes.append(Attribute(name, irange, discrete))
            i += 1
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

    @staticmethod
    def change_types(attributes, data):
        for i in range(len(attributes)):
            if attributes[i].discrete is False:
                for d in data:
                    if d.value[i] != "?":
                        d.value[i] = float(d.value[i])


