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

    # Used for sorting
    def __lt__(self, other):
        return int(self) < int(other)


class BillBatch:
    def __init__(self, bills):
        self.__bills = bills

    def __len__(self):
        return len(self.__bills)

    def __getitem__(self, index):
        return self.__bills[index]

    def total(self):
        return sum([int(bill) for bill in self.__bills])


class CashDesk:
    def __init__(self):
        self.money_holder = {}

    def __store_money(self, bill):
        if bill not in self.money_holder:
            self.money_holder[bill] = 1
        else:
            self.money_holder[bill] += 1

    def take_money(self, money):
        if isinstance(money, Bill):
            self.__store_money(money)
        elif isinstance(money, BillBatch):
            for bill in money:
                self.__store_money(bill)

    def total(self):
        m = self.money_holder
        return sum([int(bill) * m[bill] for bill in m])

    def inspect(self):
        lines = []
        total = self.total()

        lines.append("We have {}$ in the desk.".format(total))

        if total > 0:
            lines.append("Bills are:")

            bills = list(self.money_holder.keys())
            bills.sort()

            for bill in bills:
                line = "${} - {}".format(int(bill), self.money_holder[bill])
                lines.append(line)
        return "\n".join(lines)
