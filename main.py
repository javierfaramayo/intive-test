import unittest
from Shop import Shop
from BikeRental import BikeRental
from constants import RENTAL_TYPES
from datetime import datetime, timedelta


class ShopTest(unittest.TestCase):

    def setUp(self):

        self.shop = Shop()

    def test_get_initial_stock(self):

        self.assertEqual(self.shop.get_stock(), 10)

    def test_increment_stock(self):

        self.shop.increment_stock(5)
        self.assertEqual(self.shop.get_stock(), 15)

    def test_decrement_stock(self):

        self.shop.decrement_stock(5)
        self.assertEqual(self.shop.get_stock(), 5)


class BikeRentalTest(unittest.TestCase):

    def setUp(self):

        self.rental = BikeRental()

    def test_rent_bike_invalid_amount_valid_rental_type(self):

        self.assertFalse(self.rental.rent_bike(0, 1))
        self.assertEqual(self.rental.get_stock(), 10)

        self.assertFalse(self.rental.rent_bike(-3, 2))
        self.assertEqual(self.rental.get_stock(), 10)

        self.assertFalse(self.rental.rent_bike(15, 3))
        self.assertEqual(self.rental.get_stock(), 10)

    def test_rent_bike_valid_amount_and_rental_type(self):
        self.assertIsInstance(self.rental.rent_bike(2, 1), datetime)
        self.assertEqual(self.rental.get_stock(), 8)

    def test_rent_bike_valid_amount_invalid_rental_type(self):
        self.assertFalse(self.rental.rent_bike(5, 4))

    def test_return_bike_incorrect_data(self):

        # Incorrect amount of bikes, negative number
        self.assertFalse(self.rental.return_bike(-3, RENTAL_TYPES['PER_HOUR'], datetime.now() + timedelta(hours=-1)))
        self.assertEqual(self.rental.get_stock(), 10)

        # Incorrect amount of bikes, zero number
        self.assertFalse(self.rental.return_bike(0, RENTAL_TYPES['PER_DAY'], datetime.now() + timedelta(hours=-1)))
        self.assertEqual(self.rental.get_stock(), 10)

        # Incorrect rental type
        self.assertFalse(self.rental.return_bike(5, 4, datetime.now() + timedelta(hours=-1)))
        self.assertEqual(self.rental.get_stock(), 10)

        # Incorrect datetime
        self.assertFalse(self.rental.return_bike(5, RENTAL_TYPES['PER_HOUR'], None))
        self.assertEqual(self.rental.get_stock(), 10)



if __name__ == '__main__':
    unittest.main()
