class Bill:
    def __init__(self, amount):
        if amount <= 0:
            raise ValueError

        if not isinstance(amount, int):
            raise TypeError

        self.__amount = amount

    def __int__(self):
        return self.__amount

    def __str__(self):
        return "A {}$ bill.".format(self.__amount)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return int(self) == int(other)

    def __hash__(self):
        return hash(self.__str__())
