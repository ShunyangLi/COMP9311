"""
implement the buffer replace
"""
from random import randint


def LRU(pages, buffer_size):
    buffer = []
    replacement = 0

    for page in pages:
        if len(buffer) < buffer_size:
            buffer.insert(0, page)
        else:
            if page in buffer:
                temp = buffer.pop(buffer.index(page))
                buffer.insert(0, temp)
            else:
                replacement += 1
                buffer.pop()
                buffer.insert(0, page)
        print("Query: {: <4} Buffer: [{: <4}]".format(page, ", ".join([str(i) for i in buffer])))

    return replacement


def MRU(pages, buffer_size):
    """
    pop the max accessd
    """
    buffer = []
    replacement = 0

    for page in pages:
        if len(buffer) < buffer_size:
            buffer.insert(0, page)
        else:
            if page in buffer:
                del buffer[buffer.index(page)]
                buffer.append(page)
            else:
                replacement += 1
                buffer.pop()
                buffer.insert(0, page)

        print("Query: {: <4} Buffer: [{: <4}]".format(page, ", ".join([str(i) for i in buffer])))

    return replacement

# def MRU(pages, buffer_size):
#     """
#     pop the max accessd
#     """
#     buffer = {}
#     replacement = 0
#
#     for page in pages:
#         if len(buffer) < buffer_size:
#             buffer[page] = 1
#         else:
#             if page in buffer:
#                 # put it at the end
#                 val = buffer[page] + 1
#                 del buffer[page]
#                 buffer[page] = val
#             else:
#                 # delete the mostly access
#                 replacement += 1
#                 key = list(buffer.keys())[-1:].pop()
#                 del buffer[key]
#                 buffer[page] = 1
#
#         print("Query: {} Buffer: {}".format(page, buffer))
#
#     return replacement


def FIFO(pages, buffer_size):
    buffer = []
    replacement = 0

    for page in pages:
        if len(buffer) < buffer_size:
            buffer.insert(0, page)
        else:
            if page not in buffer:
                replacement += 1
                buffer.pop()
                buffer.insert(0, page)
        print("Query: {: <4} Buffer: [{: <4}]".format(page, ", ".join([str(i) for i in buffer])))

    return replacement


if __name__ == '__main__':
    pages = []
    buffer_size = 3

    for i in range(0, 10):
        pages.append(randint(1, 10))

    while True:
        lru = LRU(pages, buffer_size)
        print("LRU: ", lru)

        mru = MRU(pages, buffer_size)
        print("MRU: ", mru)

        fifo = FIFO(pages, buffer_size)
        print("FIFO: ", fifo)

        if lru < fifo < mru:
            print(pages)
            break

        pages.clear()
        for i in range(0, 10):
            pages.append(randint(1, 9))
