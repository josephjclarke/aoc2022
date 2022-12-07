import itertools


class FileType:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getSize(self):
        return self.size

    def __repr__(self):
        return f"{self.name} {self.size}"


class File(FileType):
    pass


class Directory(FileType):
    def __init__(self, name):
        super().__init__(name, 0)
        self.contains = []
        self.knowsSize = False

    def addFile(self, f):
        if isinstance(f, Directory):
            f.parent = self
        self.contains.append(f)
        self.knowsSize = False

    def calcSize(self):
        if self.knowsSize == True:
            return
        if self.contains == []:
            self.size = 0
            self.knowsSize = True
        else:
            self.size = sum(map(lambda x: x.getSize(), self.contains))
            self.knowsSize = True

    def getSize(self):
        if self.knowsSize == True:
            return self.size
        else:
            self.calcSize()
            return self.size


def get_all_directories_helper(start):
    ds = list(filter(lambda d: isinstance(d, Directory), start.contains))
    if len(ds) == 0:
        return start
    return [start, *map(get_all_directories_helper, ds)]


def flatten(ds):
    for d in ds:
        if isinstance(d, list):
            yield from flatten(d)
        else:
            yield d


def get_all_directories(start):
    return flatten(get_all_directories_helper(start))


class Parsed:
    def __init__(self, com, args):
        self.com = com
        self.args = args

    def __repr__(self):
        return f"{self.com} {self.args}"


def parse(data):
    i = 0
    while i < len(data):
        line = data[i]
        if line[0] == "$":
            com = line[2:4]
            if com == "cd":
                i += 1
                yield Parsed("cd", line[5:])
            elif com == "ls":
                j = i + 1
                args = []
                while j < len(data):
                    nextline = data[j]
                    if nextline[0] == "$":
                        break
                    else:
                        args.append(nextline)
                        j += 1
                i = j
                yield Parsed("ls", args)


data = [line.rstrip() for line in open("input07.txt").readlines()]

root = Directory("/")
root.parent = root
current_dir = root
for command in parse(data):
    if command.com == "cd":
        if command.args == "/":
            current_dir = root
        elif command.args == "..":
            current_dir = current_dir.parent
        for d in current_dir.contains:
            if d.name == command.args:
                current_dir = d
    elif command.com == "ls":
        for f in command.args:
            a, b = f.split()
            if a == "dir":
                current_dir.addFile(Directory(b))
            else:
                current_dir.addFile(File(b, int(a)))

total_size = root.getSize()
dirs = get_all_directories(root)
dir_sizes = list(map(lambda d: d.size, dirs))
small_enough = filter(lambda x: x < 100000, dir_sizes)
print(sum(small_enough))
current_unused_space = 70000000 - total_size
print(min(filter(lambda x: x + current_unused_space >= 30000000, dir_sizes)))
