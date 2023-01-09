class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = {}
        


    def add_child(self, name):
        return self.children.setdefault(name, Node(name, parent=self))


    def add_file(self, name, size):
        self.files[name] = int(size)

    #Properties
    @property
    def root(self):
        return self if self.parent is None else self.parent.root
    @property
    def size(self):
        dir_value = 0
        for item in self.files:
            self.files
        return sum(self.files.values()) + sum(node.size for node in self.children.values())


    def __iter__(self):
        for child in self.children.values():
            yield child
            yield from child


    def rec_dir_sizes2(self, dir_sizes):
        for child in self.children.values():
            child.rec_dir_sizes2(dir_sizes)
        dir_sizes[self.name] = self.size
        return

    def rec_dir_sizes(self):
        dir_sizes = {}

        for child in self.children.values():
            child.rec_dir_sizes2(dir_sizes)
        dir_sizes[self.name] = self.size
        return dir_sizes

def process_data():
    data = open("inputs/aoc7.txt", "r")
    lines = data.readlines()
    current_dir = Node("/")
    for line in lines[1:]:
        #print(line)
        line = line.strip("\n").split(" ")
        if line[0] == "dir":
            continue
        elif line[0] == "$":
            command = line[1]
            if command == "cd":
                dir = line[2]
                if dir == "..":
                    current_dir = current_dir.parent
                else:
                    current_dir.add_child(dir)
                    current_dir = current_dir.children[dir]
                    
        else:
            #print(line)
            current_dir.add_file(line[1], line[0])
            #print(current_dir.files)
            
    return current_dir.root


if __name__ == '__main__':
    root = process_data()
    dir_dict = root.rec_dir_sizes()
    print(dir_dict)
    score = 0
    for item in dir_dict.values():
        if item <= 100000:
            score += item
            
    print(f"the answer is: {score}")

    print(f"or {sum(dir.size for dir in root if dir.size < 100000)}")
    
    total_size = root.size
    max_size = 70000000
    req_size = 30000000
    space_left = max_size-total_size
    min_remove = req_size-space_left
    result = max_size
    for item in dir_dict.values():
        value = item - min_remove
        old_value = result - min_remove
        if value <= old_value and value >= 0:
            result = item
    print(f"the second answer is: {result}")
    