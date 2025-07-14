import unittest
from step1_city_functions import city_country

# Step 2 - Unit test for city_country()
class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

if __name__ == '__main__':
    unittest.main()
