"""
Simple class to count from zero to N
"""
class count_to(object):
    def __init__(self, nber):
        if nber < 0:
            raise ValueError('count_to argument must be a positive integer')

        self.nber = nber

    def __iter__(self):
        return count_to_iter(self.nber)


class count_to_iter(object):
    def __init__(self, nber):
        self.stopat = nber
        self.current_nber = 0

    def __next__(self):
        if self.current_nber > self.stopat:
            raise StopIteration

        self.current_nber += 1

        return self.current_nber - 1


if __name__ == '__main__':
    for x in count_to(-1):
        print(x)