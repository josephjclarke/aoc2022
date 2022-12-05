def half(lines):
    return [[line[:len(line) // 2], line[len(line) // 2:]] for line in lines]


def both(hl):
    return [set(left).intersection(set(right)) for left, right in hl]


def priority(ch):
    return (ord(ch) - 96) % 58


def triples(lines):
    tr = []
    for i in range(0, len(lines) - 3, 3):
        tr.append(
            list(
                set(lines[i]).intersection(set(lines[i + 1])).intersection(
                    set(lines[i + 2])))[0])
    return tr


with open("input03.txt") as file:
    lines = [line.rstrip() for line in file]
    halfed_lines = half(lines)
    common = [list(b) for b in both(halfed_lines)]
    ps = [list(map(priority, c)) for c in common]
    total_p = [sum(p) for p in ps]
    overall = sum(total_p)
    print(overall)
    tr = triples(lines)
    print(sum(map(priority, tr)))
