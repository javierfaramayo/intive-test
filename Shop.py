from constants import INITIAL_STOCK


class Shop:
    def __init__(self):
        """
        When a shop is created it will get the current bikes stock from anywhere, it can be a database, in this case it comes from a constant
        """

        self.__get_initial_stock()

    def __get_initial_stock(self):
        self.__stock = INITIAL_STOCK

    def get_stock(self):
        """ Returns the current stock """
        return self.__stock

    def increment_stock(self, q):
        """ Increments the current stock """
        self.__stock += q

    def decrement_stock(self, q):
        """ Decrement the current stock """
        self.__stock -= q
