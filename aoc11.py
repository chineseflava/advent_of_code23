import math
import os
import numpy as np
import operator

try:
   from itertools import izip_longest
except ImportError:  # Python 3
    from itertools import zip_longest as izip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

class Monkey():
    def __init__(self, name, items, operation, test, pass_test, no_pass_test):
        
        self.name = name
        self.items = [int(x) for x in items.split(", ")]
        self.operation = operation.split(" ")
        self.test = int(test)
        self.pass_test = [int(pass_test), int(no_pass_test)]
        self.n_spect = 0

    def operate(self, item):
        ops = { "+": operator.add, "*": operator.mul}
        if self.operation[4] == "old":
            new_level = ops[self.operation[3]](item, item)
        else:
            new_level = ops[self.operation[3]](item, int(self.operation[-1]))
        return new_level


def do_shenanigans(monkey, monkeys):

    for item in monkey.items:
        lcm = 11*19*7*17*3*5*13*2
        item = monkey.operate(int(item))
        monkey.n_spect += 1
        item = item % lcm # // 3 part
        #print(item)
        if item % monkey.test == 0:
            throw(monkey.pass_test[0], item, monkeys)
        else:
            throw(monkey.pass_test[1], item, monkeys)
    monkey.items = []


def throw(monkey_no, item, monkeys):
    monkeys[monkey_no].items.append(item)


def process_data():
    # read data
    filename = 'inputs/aoc11.txt'
    monkeys = []
    N = 7
    with open(filename) as f:
        for lines in grouper(f, N, ''):
            assert len(lines) == N
            #print(lines)
            name = lines[0][7]
            items = lines[1][18:-1]
            operation = lines[2][13:-1]
            test = lines[3][21:-1]
            pass_test = lines[4][29:-1]
            no_pass_test = lines[5][30:-1]
            print(f"Monkey {name}; items {items}; operation {operation}; test {test} - {pass_test}:{no_pass_test}")
            monkey = Monkey(name, items, operation, test, pass_test, no_pass_test)
            monkeys.append(monkey)
            #print(monkey.items)
            #print(monkey.operation)
    
    #print(monkeys)
    for i in range(10000):
        for monkey in monkeys:
            do_shenanigans(monkey, monkeys)
    monkey_spections = []
    for monkey in monkeys:
        monkey_spections.append(monkey.n_spect)
    monkey_spections.sort()
    print(monkey_spections[-1] * monkey_spections[-2])


if __name__ == '__main__':
    process_data()