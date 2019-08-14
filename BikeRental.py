from constants import RENTAL_TYPES, RENTAL_PRICES, FAMILIAR_DISCOUNT
from Shop import Shop
from datetime import datetime


class BikeRental(Shop):
    """
    BikeRental inherits from Shop to get the initial stock when an instance is created and increment and decrement
    the stock
    """

    def __init__(self):
        super().__init__()
        self.bikes = 0
        self.rental_type = 0
        self.rented_at = None

    def __validate_bikes_request(self):
        if self.bikes <= 0:
            print("The amount of bikes must be greater than 0")
            return False

        if self.get_stock() < self.bikes:
            print("There is no available stock")
            return False

        if self.rental_type not in RENTAL_TYPES.values():
            print("The rental type is not available")
            return False

        return True

    def rent_bike(self, bikes, rental_type):

        self.bikes = bikes
        self.rental_type = rental_type

        if self.__validate_bikes_request():

            self.rented_at = datetime.now()

            print(f'Success! {self.bikes} bikes rented at {self.rented_at}.')
            self.decrement_stock(self.bikes)
            return self.rented_at

        return False

    def return_bike(self, bikes, rental_type, rented_at):

        """ First verifies if three fields are not null """
        if bikes and rental_type and rented_at:

            self.bikes = bikes
            self.rental_type = rental_type
            self.rented_at = rented_at

            if self.rental_type not in RENTAL_TYPES.values():

                """ Verifies if the rental type sent exists """
                print("The rental type is not available")
                return False

            if self.bikes <= 0:

                """ Verifies if the amount of bikes is correct """
                print("The amount of bikes must be greater than 0")
                return False

            """ Returns the bikes to stock """
            self.increment_stock(self.bikes)

            """ Calculates the price based on the time used """
            price = self.__calculate_price()

            if 3 <= self.bikes <= 5:
                print("Applies familiar discount")
                price = price - (price * FAMILIAR_DISCOUNT / 100)

            return price

        else:
            print("Incorrect data")
            return False

    def __calculate_price(self):

        price = 0
        time_used = datetime.now() - self.rented_at

        if self.rental_type == RENTAL_TYPES['PER_HOUR']:

            price = round((time_used.seconds / 3600) * RENTAL_PRICES['PER_HOUR'] * self.bikes, 2)

        elif self.rental_type == RENTAL_TYPES['PER_DAY']:

            price = round(time_used.days * RENTAL_PRICES['PER_DAY'] * self.bikes, 2)

        elif self.rental_type == RENTAL_TYPES['PER_WEEK']:

            price = round((time_used.days / 7) * RENTAL_PRICES['PER_WEEK'] * self.bikes, 2)

        return price


