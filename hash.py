length = 4
pages = {}
next = 0


def split():
    global pages
    global length
    global next

    values = pages[next]

    for i in range(0, length + 1):
        if i == next:
            pages[i] = []
        if i not in pages.keys():
            pages[i] = []

    length += 1
    for val in values:
        index = val % 8
        pages[index].append(val)

    next += 1

    if len(pages.keys()) == 8:
        next = 0


def insert(val):
    index = val % 4
    index1 = val % 8
    if index != index1:
        if len(pages.keys()) > index1:
            index = index1
    if len(pages[index]) >= 4:
        pages[index].append(val)
        split()
    else:
        pages[index].append(val)


def init_pages():
    for i in range(0, length):
        pages[i] = []


if __name__ == '__main__':
    init_pages()

    data = [32, 44, 36, 9, 25, 5, 14, 18, 10, 30, 31, 35, 7, 11, 43, 37, 29,34,66,22, 50]
    
    for d in data:
        insert(d)

    print(pages, next, length)
