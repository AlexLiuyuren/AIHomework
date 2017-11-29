import math
from collections import Counter
from attribute import Attribute
from data import Data
import copy
import queue


class TreeNode:
    def __init__(self, data=[], attribute=None, category=None, next_node=[]):
        # 该节点上数据
        self.data = data
        # weight 处理缺失值
        self.weight = None
        # 划分属性
        self.attribute = attribute
        # 叶结点的类别
        self.category = category
        # 叶结点
        self.next_node = next_node


# 缺失值, 连续值
def tree_generate(data, tmp_attributes, attributes, optimizer):
    c, same = same_class(data)
    node = TreeNode()
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
    # attr 可能是continuous的, 此时attr.value有值
    attr, weight, data_set = optimizer(data, tmp_attributes, attributes)
    # print(attr.name)
    node.attribute = attr
    node.weight = weight
    node.next_node = []
    i = 0
    if attr.discrete is True:
        index = find_attr(attr, attributes)
        # print(index)
        for iset in data_set:
            for d in iset:
                if d.value[index] == "?":
                    d.w *= node.weight[i]
            if len(iset) == 0:
                new_node = TreeNode(data=iset)
                new_node.category = most_class(data)
                node.next_node.append(new_node)
            else:
                Attribute.remove(tmp_attributes, attr)
                new_node = tree_generate(iset, tmp_attributes, attributes, optimizer)
                node.next_node.append(new_node)
            i += 1
    else:
        vindex = find_index(attr.range, attr.value)
        aindex = find_attr(attr, tmp_attributes)
        tmp_attrs1 = copy.deepcopy(tmp_attributes)
        tmp_attrs2 = copy.deepcopy(tmp_attributes)
        tmp_attrs = [tmp_attrs1, tmp_attrs2]
        tmp_attrs1[aindex].range = tmp_attrs1[aindex].range[:vindex]
        tmp_attrs2[aindex].range = tmp_attrs2[aindex].range[vindex + 1:]
        if len(tmp_attrs1[aindex].range) == 0:
            Attribute.remove(tmp_attrs1, attr)
        if len(tmp_attrs2[aindex].range) == 0:
            Attribute.remove(tmp_attrs2, attr)
        for i in range(2):
            for d in data_set[i]:
                if d.value[aindex] == "?":
                    d.w *= node.weight[i]
            if len(data_set[i]) == 0:
                new_node = TreeNode(data=data_set[i])
                new_node.category = most_class(data)
                node.next_node.append(new_node)
            else:
                new_node = tree_generate(data_set[i], tmp_attrs[i], attributes, optimizer)
                node.next_node.append(new_node)
    return node


def find_index(listi, value):
    for i in range(len(listi)):
        if value == listi[i]:
            return i
    return -1


def find_data(data, attr, v, attributes):
    index = find_attr(attr, attributes)
    new_data = []
    for d in data:
        if d.value[index] == v:
            new_data.append(d)
    return new_data


# situation 1: same class
def same_class(data):
    c = data[0].value[-1]
    same = True
    for d in data:
        if d.value[-1] != c:
            same = False
            break
    return c, same


def find_attr(attribute, attributes):
    for i in range(len(attributes)):
        if attribute.name == attributes[i].name:
            return i
    print("attribute not found")
    return -1


def have_same_attributes(data, tmp_attributes, attributes):
    index = []
    res = []
    for attr in tmp_attributes:
        i = find_attr(attr, attributes)
        index.append(i)
    for i in index:
        res.append(data[0].value[i])
    for d in data:
        for i in range(len(index)):
            if d.value[index[i]] != res[i]:
                return False
    # print("have same attributes")
    return True


def most_class(data):
    category = []
    for d in data:
        category.append(d.value[-1])
    c = Counter(category).most_common()[0][0]
    # print(c)
    return c


# test function
def tree_test(root, x, attributes):
    if root.category is not None:
        return [root.category], [x.w]
    index = find_attr(root.attribute, attributes)
    if x.value[index] == "?":
        ret_category = []
        ret_w = []
        if root.attribute.discrete is True:
            for i in range(len(root.attribute.range)):
                new_x = copy.deepcopy(x)
                new_x.w *= root.weight[i]
                new_category, new_w = tree_test(root.next_node[i], new_x, attributes)
                ret_category.extend(new_category)
                ret_w.extend(new_w)
        else:
            for i in range(2):
                new_x = copy.deepcopy(x)
                new_x.w *= root.weight[i]
                new_category, new_w = tree_test(root.next_node[i], new_x, attributes)
                ret_category.extend(new_category)
                ret_w.extend(new_w)
        return ret_category, ret_w
    else:
        if root.attribute.discrete is True:
            childi = 0
            for d in root.attribute.range:
                # print(d)
                # print(x.value[index])
                if x.value[index] == d:
                    return tree_test(root.next_node[childi], x, attributes)
                else:
                    childi += 1
        else:
            if x.value[index] <= root.attribute.value:
                return tree_test(root.next_node[0], x, attributes)
            else:
                return tree_test(root.next_node[1], x, attributes)
    print("error")
    return None

def continuous_divide(data, attr, value, attributes):
    left_data = []
    right_data = []
    index = find_attr(attr, attributes)
    for d in data:
        if d.value[index] == "?":
            continue
        if d.value[index] <= value:
            left_data.append(d)
        else:
            right_data.append(d)
    return [left_data, right_data]


def ent(data):
    res = 0
    category = []
    wsum = 0
    for d in data:
        wsum += d.w
        if d.value[-1] not in category:
            category.append(d.value[-1])
    for k in category:
        wk = 0
        for d in data:
            if d.value[-1] == k:
                wk += d.w
        if wk == 0:
            continue
        pk = wk / wsum
        res -= pk * math.log(pk, 2)
    return res


def divide_data(data, attr, attributes):
    data_set = []
    for value in attr.range:
        new_data = find_data(data, attr, value, attributes)
        data_set.append(new_data)
    return data_set


def no_empty_data(data, attr, attributes):
    index = find_attr(attr, attributes)
    new_data = []
    for d in data:
        if d.value[index] != "?":
            new_data.append(d)
    return new_data


def bfs(root):
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        name = "None"
        weight = "None"
        if node.attribute is not None:
            name = node.attribute.name
        if node.weight is not None:
            weight =node.weight
        print("attributename: %s, weight: %s" % (name, str(weight)))
        for n in node.next_node:
            q.put(n)


def all_zero(lst):
    for i in lst:
        if i != 0:
            return False
    return True
