# encapsulation: making instance variables 'private'
class Transaction:
    def __init__(self, date, category, description, amount, type):
        self.__date = date
        self.__category = category
        self.__description = description
        self.__amount = amount
        self.__type = type

    # I want to change string representation of Transaction object
    def __str__(self):
        return f"{self.__date}: {self.__category}, {self.__description}, {self.__amount}, {self.__type}"

    # getter
    def get_category(self):
        return self.__category

    def get_date(self):
        return self.__date

    def get_amount(self):
        return self.__amount

    def get_description(self):
        return self.__description

    def get_type(self):
        return self.__type

    # setter
    def set_category(self, category):
        if category == "Food" or category == "Rent" or category == "Utilities":
            self.__category = category
        else:
            print("Wrong Category")

    def set_description(self, description):
        if len(description) < 30:
            self.__description = description
        else:
            print("Too many characters")

    def set_type(self, type):
        if type == "Expense" or type == "Income":
            self.__type = type
        else:
            print("Wrong type")


