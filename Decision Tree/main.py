from ID3 import id3_tree_generate, id3_tree_test, bfs
from data import Data
from attribute import Attribute
import copy
import pandas as pd


def read_data(filename):
    f = open(filename)
    data = []
    all_lines = f.readlines()
    for line in all_lines:
        tmp = line.split(",")
        tmp[-1] = tmp[-1][:-1]
        # print(tmp)
        data.append(Data(tmp))
    f.close()
    return data

if __name__ == "__main__":
    data = read_data("audiology.standardized.train.txt")
    attributes = Attribute.read_attribute("audiology_attribute.txt", data)
    tmp_attributes = copy.deepcopy(attributes)
    root = id3_tree_generate(data, tmp_attributes, attributes)
    right = 0
    # bfs(root)
    test_data = read_data("audiology.standardized.test.txt")
    # print(test_data)
    for d in test_data:
        category, probability = id3_tree_test(root, d, attributes)
        # print(category)
        # print(probability)
        pmax = -1
        index = -1
        for i in range(len(probability)):
            # print(probability[i])
            if probability[i] > pmax:
                pmax = probability[i]
                index = i
        print(category[index], d.value[-1])
        if category[index] == d.value[-1]:
            right += 1
    print("correct percentage: %f" % (right / len(test_data)))

