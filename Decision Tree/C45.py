from tree import *
import math


def c45_optimizer(data, tmp_attributes, attributes):
    best_attr = None
    best_gain_ratio = -1
    best_weight = []
    best_data_set = []
    for attr in tmp_attributes:
        if attr.range[0] == "#unique":
            # print("pass unique")
            continue
        if attr.discrete is True:
            not_empty = no_empty_data(data, attr, attributes)
            e1 = ent(not_empty)
            wdsum = Data.wsum(data)
            wdnesum = Data.wsum(not_empty)
            ro = 0
            if wdnesum != 0:
                ro = wdnesum / wdsum
            data_set = divide_data(not_empty, attr, attributes)
            new_e = 0
            weight = []
            for iset in data_set:
                rv = 0
                if wdnesum != 0:
                    rv = Data.wsum(iset) / wdnesum
                weight.append(rv)
                new_e += rv * ent(iset)
            gain = ro * (e1 - new_e)
            IV = 1
            if wdnesum != 0:
                IV = 0
                for iset in data_set:
                    rv = Data.wsum(iset) / wdnesum
                    if rv == 0:
                        continue
                    IV -= rv * math.log(rv, 2)
            if IV == 0:
                IV = 1
            gain_ratio = gain / IV
            if gain_ratio > best_gain_ratio:
                best_gain_ratio = gain_ratio
                best_attr = attr
                best_weight = weight
                index = find_attr(best_attr, attributes)
                for d in data:
                    if d.value[index] == "?":
                        new_d = copy.deepcopy(d)
                        for i in range(len(data_set)):
                            if weight[i] > 0:
                                data_set[i].append(new_d)
                best_data_set = data_set
        else:
            not_empty = no_empty_data(data, attr, attributes)
            e1 = ent(not_empty)
            wdsum = Data.wsum(data)
            wdnesum = Data.wsum(not_empty)
            ro = 0
            if wdnesum != 0:
                ro = wdnesum / wdsum
            best_continuous_gain_ratio = -1
            best_continuous_value = 0
            best_continuous_dataset = []
            best_continuous_weight = []
            for value in attr.range:
                data_set = continuous_divide(not_empty, attr, value, attributes)
                new_e = 0
                weight = []
                for iset in data_set:
                    rv = 0
                    if wdnesum != 0:
                        rv = Data.wsum(iset) / wdnesum
                    weight.append(rv)
                    new_e += rv * ent(iset)
                continuous_gain = ro * (e1 - new_e)
                IV = 1
                if wdnesum != 0:
                    IV = 0
                    for iset in data_set:
                        rv = Data.wsum(iset) / wdnesum
                        if rv == 0:
                            continue
                        IV -= rv * math.log(rv, 2)
                if IV == 0:
                    IV = 1
                continuous_gain_ratio = continuous_gain / IV
                if continuous_gain_ratio > best_continuous_gain_ratio:
                    best_continuous_gain_ratio = continuous_gain_ratio
                    best_continuous_value = value
                    best_continuous_weight = weight
                    best_continuous_dataset = data_set
            if best_continuous_gain_ratio > best_gain_ratio:
                best_gain_ratio = best_continuous_gain_ratio
                best_attr = attr
                best_attr.value = best_continuous_value
                best_weight = best_continuous_weight
                index = find_attr(best_attr, attributes)
                for d in data:
                    if d.value[index] == "?":
                        new_d = copy.deepcopy(d)
                        for i in range(len(best_continuous_dataset)):
                            if best_weight[i] > 0:
                                best_continuous_dataset[i].append(new_d)
                best_data_set = best_continuous_dataset
    return best_attr, best_weight, best_data_set
