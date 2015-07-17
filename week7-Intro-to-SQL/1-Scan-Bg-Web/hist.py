class Histogram:
    
    def __init__(self):
        self.__hist = {}

    def add(self, value):
        if value not in self.__hist:
            self.__hist[value] = 0

        self.__hist[value] += 1
    
    def count(self, value):
        if value in self.__hist:
            return self.__hist[value]

    def items(self):
        return self.__hist.items()

    def __str__(self):
        return str(self.__hist)
    
    def __repr__(self):
        return self.__str__()
    
    def get_dict(self):
        return self.__hist

def main():
    h = Histogram()

    h.add(1)
    h.add(1)
    h.add(2)
    h.add(2)
    h.add(3)
    
    for key, count in h.items():
        print("{}: {}".format(key, count))

if __name__ == "__main__":
    main()
