import math


class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": amount, "description": desc})

    def withdraw(self, amount, desc=""):
        if self.check_funds(amount):
            amount *= -1
            self.ledger.append({"amount": amount, "description": desc})
            return True
        return False

    def transfer(self, amount, category):
        if self.withdraw(amount, "Transfer to {}".format(category.name)):
            category.deposit(amount, "Transfer from {}".format(self.name))
            return True
        return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        return False

    def get_balance(self):
        amount = 0
        for element in self.ledger:
            amount += element["amount"]
        return amount

    def __str__(self):
        s = self.name.center(30, '*')
        for x in self.ledger:
            s += "\n" + "{:<23}".format(x["description"])[0:23] + "{:>7.2f}".format(x["amount"])
        s += "\n" + "Total: " + "{:.2f}".format(self.get_balance())
        return s


def create_spend_chart(categories):
    s = "Percentage spent by category"
    total = list()
    max_length = 0
    t = 0
    for category in categories:
        for x in category.ledger:
            if x["amount"] < 0:
                t += x["amount"]
    t *= -1
    for category in categories:
        amt = 0
        for x in category.ledger:
            if x["amount"] < 0:
                amt += x["amount"]
        amt *= -1
        amt /= t
        amt *= 100
        total.append(math.floor(amt / 10) * 10)
        if len(category.name) > max_length:
            max_length = len(category.name)
    y_axis = 100
    while y_axis >= 0:
        s += "\n{:>3}|".format(y_axis)
        for i in range(0, len(total)):
            if total[i] == y_axis:
                total[i] -= 10
                if i == 0:
                    s += " o"
                else:
                    s += "  o"
            else:
                if i == 0:
                    s += "  "
                else:
                    s += "   "
        y_axis -= 10
        s += "  "
    s += "\n    "
    for i in range(0, len(total)):
        s += "---"
    s += "-"
    for i in range(0, max_length):
        first = True
        s += "\n    "
        for category in categories:
            if first:
                try:
                    s += " " + category.name[i]
                except:
                    s += "  "
                first = False
            else:
                try:
                    s += "  " + category.name[i]
                except:
                    s += "   "
        s += "  "
    return s
