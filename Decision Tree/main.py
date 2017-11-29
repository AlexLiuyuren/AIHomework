from tree import *
from ID3 import id3_optimizer
from C45 import c45_optimizer
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


def test(train_data_file_name, attribute_file_name, test_data_file_name, optimizer):
    data = read_data(train_data_file_name)
    attributes = Attribute.read_attribute(attribute_file_name, data)
    tmp_attributes = copy.deepcopy(attributes)
    root = tree_generate(data, tmp_attributes, attributes, optimizer)
    right = 0
    # bfs(root)
    test_data = read_data(test_data_file_name)
    Attribute.change_types(attributes, test_data)
    for d in test_data:
        category, probability = tree_test(root, d, attributes)
        pmax = -1
        index = -1
        for i in range(len(probability)):
            # print(probability[i])
            if probability[i] > pmax:
                pmax = probability[i]
                index = i
        # print(category[index], d.value[-1])
        if category[index] == d.value[-1]:
            right += 1
    print("correct percentage: %f" % (right / len(test_data)))

if __name__ == "__main__":
    # test("audiology.standardized.train.txt", "audiology_attribute.txt", "audiology.standardized.test.txt", id3_optimizer)
    # test("credit_train.txt", "credit_attribute.txt", "credit_test.txt", id3_optimizer)
    test("audiology.standardized.train.txt", "audiology_attribute.txt", "audiology.standardized.test.txt", c45_optimizer)
    # test("credit_train.txt", "credit_attribute.txt", "credit_test.txt", c45_optimizer)



