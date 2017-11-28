from ID3 import id3_tree_generate, id3_tree_test
from attribute import Attribute
import copy
import pandas as pd

def read_data(filename):
    f = open(filename)
    data = []
    all_lines = f.readlines()
    for line in all_lines:
        tmp = line.split(",")
        data.append(tmp)
    data[-1][-1] = data[-1][-1][:-1]
    f.close()
    return data

if __name__ == "__main__":
    data = read_data("audiology.standardized.train.txt")
    attributes = Attribute.read_attribute("audiology_attribute.txt")
    tmp_attributes = copy.deepcopy(attributes)
    root = id3_tree_generate(data, tmp_attributes, attributes)
    right = 0
    for d in data:
        if id3_tree_test(root, d, attributes) == d[-1]:
            right += 1
    print("correct percentage: %f" % (right / len(data)))
    # print(root.attribute.name)
    # print(data[-1])
    # print(attributes[-1].range)
