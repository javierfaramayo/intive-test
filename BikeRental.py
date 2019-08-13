from constants import RENTAL_TYPES, RENTAL_PRICES
from Shop import Shop
from datetime import datetime


class BikeRental(Shop):

    def __validate_bikes_request(self, bikes, rental_type):
        if bikes <= 0:
            print("The amount of bikes must be greater than 0")
            return False

        if self.get_stock() < bikes:
            print("There is no available stock")
            return False

        if rental_type not in RENTAL_TYPES.values():
            print("The rental type is not available")
            return False

        return True

    def rent_bike(self, bikes, rental_type):

        if self.__validate_bikes_request(bikes, rental_type):

            rent_time = datetime.now()

            print(f'Success! {bikes} bikes rented at {rent_time}.')
            self.decrement_stock(bikes)
            return rent_time

        return False

    def return_bike(self, bikes, rental_type, rented_at):

        """ First verifies if three fields are not null """
        if bikes and rental_type and rented_at:

            if rental_type not in RENTAL_TYPES.values():

                """ Verifies if the rental type sent exists """
                print("The rental type is not available")
                return False

            if bikes <= 0:

                """  """
                print("The amount of bikes must be greater than 0")
                return False

            self.increment_stock(bikes)
            self.__calculate_price()

            return True

        else:
            print("Incorrect data")
            return False
