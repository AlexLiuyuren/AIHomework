import math
from collections import Counter
from attribute import Attribute


class ID3TreeNode:
    def __init__(self, data=[], attribute=None, category=None, next_node=None):
        # 该节点上数据
        self.data = data
        # 划分属性
        self.attribute = attribute
        # 叶结点的类别
        self.category = category
        # 叶结点
        self.next_node = next_node


# 缺失值, 连续值
def id3_tree_generate(data, tmp_attributes, attributes):
    c, same = same_class(data)
    node = ID3TreeNode()
    # situation 1
    if same is True:
        node.data = data
        node.category = c
        return node
    if Attribute.empty(tmp_attributes) is True or have_same_attributes(data, tmp_attributes, attributes):
        c = most_class(data)
        node.data = data
        node.category = c
        return node
    # 要考虑#unique情况
    attr = id3_optimizer(data, tmp_attributes, attributes)
    print(attr.name)
    node.attribute = attr
    node.next_node = []
    for v in attr.range:
        new_data = find_data(data, attr, v, attributes)
        if len(new_data) == 0:
            new_node = ID3TreeNode(data=new_data)
            new_node.category = most_class(data)
            node.next_node.append(new_node)
        else:
            Attribute.remove(tmp_attributes, attr)
            new_node = id3_tree_generate(new_data, tmp_attributes, attributes)
            node.next_node.append(new_node)
    return node


def find_data(data, attr, v, attributes):
    index = find_attr(attr, attributes)
    new_data = []
    for d in data:
        if d[index] == v:
            new_data.append(d)
    return new_data


# situation 1: same class
def same_class(data):
    c = data[0][-1]
    same = True
    for d in data:
        if d[-1] != c:
            same = False
            break
    return c, same


def find_attr(attribute, attributes):
    for i in range(len(attributes)):
        if attribute.name == attributes[i].name:
            return i
    return -1


def have_same_attributes(data, tmp_attributes, attributes):
    index = []
    res = []
    for attr in tmp_attributes:
        i = find_attr(attr, attributes)
        index.append(i)
    for i in index:
        res.append(data[0][i])
    for d in data:
        for i in range(len(index)):
            if d[index[i]] != res[i]:
                return False
    return True


def most_class(data):
    category = []
    for d in data:
        category.append(d[-1])
    c = Counter(category).most_common()[0][0]
    # print(c)
    return c


# test function
def id3_tree_test(root, x, attributes):
    if root.category is not None:
        return root.category
    index = find_attr(root.attribute, attributes)
    childi = 0
    for d in root.attribute.range:
        print(d)
        print(x[index])
        if x[index] == d:
            return id3_tree_test(root.next_node[childi], x, attributes)
        else:
            childi += 1
    print("error")
    return None


def id3_optimizer(data, tmp_attributes, attributes):
    best_attr = None
    best_gain = -1
    e1 = ent(data)
    for attr in tmp_attributes:
        if attr.range[0] == "#unique":
            continue
        data_set = divide_data(data, attr, attributes)
        new_e = 0
        for set in data_set:
            new_e += len(set) / len(data) * ent(set)
        gain = e1 - new_e
        if gain > best_gain:
            best_gain = gain
            best_attr = attr
    return best_attr


def ent(data):
    res = 0
    category = []
    for d in data:
        category.append(d[-1])
    length = len(category)
    statistic = Counter(category).most_common()
    for ins in statistic:
        pk = ins[1] / length
        res -= pk * math.log(pk, 2)
    return res


def divide_data(data, attr, attributes):
    data_set = []
    for value in attr.range:
        new_data = find_data(data, attr, value, attributes)
        data_set.append(new_data)
    return data_set
