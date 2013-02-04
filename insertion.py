"""
insertion sort

script demonstrates implementation of insertion sort.
"""


import random

def insertion(l):
    """
    implements insertion sort

    pass it a list, list will be modified in place
    """

    for i in range(1, len(l)):
        for j in range(0, i):
            if l[i] < l[j]:

                # below is same as
                # l[j], l[i] = l[i], l[j]

                tmp = l[j]
                l[j] = l[i]
                l[i] = tmp

    return l


def main():
    # l = [6,7,24,1,18,23,4]

    l = range(100)

    random.shuffle(l)
    print( "Before Sort: {0}".format(l) )
    print

    l = insertion(l)
    print( "After Sort: {0}".format(l) )


if __name__ == "__main__":
    main()
