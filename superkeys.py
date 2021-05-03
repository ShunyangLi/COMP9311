
cand = ['ABJ', 'BCJ', 'BDJ', 'BEGJ', 'BGHJ']
keys = ['A', 'B', 'C', 'D', 'E', 'G', 'H', 'I', 'J']


def combine(index, supkerkeys, path):
    supkerkeys.add("".join(sorted(path)))

    for i in range(index, len(keys)):
        if keys[i] in path:
            continue

        path.append(keys[i])
        combine(i + 1, supkerkeys, path)
        path.pop()
    
    return supkerkeys


def all_superkeys():
    """
    calculate all the possible supker keys
    """
    supkerkeys = set()

    for k in cand:
        combine(0, supkerkeys, list(k))
    
    print(supkerkeys)
    print(len(supkerkeys) - len(cand))


if __name__ == '__main__':
    all_superkeys()
