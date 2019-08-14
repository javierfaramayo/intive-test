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

    def test_return_bike_correct_data_returns_price(self):

        # Returns a bike used during 3 hours
        self.assertEqual(self.rental.return_bike(1, RENTAL_TYPES['PER_HOUR'], datetime.now() + timedelta(hours=-3)), 15)
        self.assertEqual(self.rental.get_stock(), 11)

        # Returns 2 bikes used during 7.5 hours
        self.assertEqual(self.rental.return_bike(2, RENTAL_TYPES['PER_HOUR'], datetime.now() + timedelta(hours=-7.5)), 75)
        self.assertEqual(self.rental.get_stock(), 13)

        # Returns 2 bikes used during 2 days
        self.assertEqual(self.rental.return_bike(2, RENTAL_TYPES['PER_DAY'], datetime.now() + timedelta(days=-2)), 80)
        self.assertEqual(self.rental.get_stock(), 15)

        # Returns 1 bike used during 1 day
        self.assertEqual(self.rental.return_bike(1, RENTAL_TYPES['PER_DAY'], datetime.now() + timedelta(days=-1)), 20)
        self.assertEqual(self.rental.get_stock(), 16)

        # Returns 1 bike used during 1 week
        self.assertEqual(self.rental.return_bike(1, RENTAL_TYPES['PER_WEEK'], datetime.now() + timedelta(days=-7)), 60)
        self.assertEqual(self.rental.get_stock(), 17)

        # Returns 2 bikes used during 2 weeks
        self.assertEqual(self.rental.return_bike(2, RENTAL_TYPES['PER_WEEK'], datetime.now() + timedelta(days=-14)), 240)
        self.assertEqual(self.rental.get_stock(), 19)

        # Returns 3 bikes used during 5 hours, applies familiar discount
        self.assertEqual(self.rental.return_bike(3, RENTAL_TYPES['PER_HOUR'], datetime.now() + timedelta(hours=-5)), 52.5)
        self.assertEqual(self.rental.get_stock(), 22)

        # Returns 4 bikes used during 2 weeks, applies familiar discount
        self.assertEqual(self.rental.return_bike(4, RENTAL_TYPES['PER_WEEK'], datetime.now() + timedelta(days=-14)), 336)
        self.assertEqual(self.rental.get_stock(), 26)


if __name__ == '__main__':
    unittest.main()
