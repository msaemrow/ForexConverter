from unittest import TestCase
from app import app
from converter import Converter

class ConverterTests(TestCase):
    def setUp(self):
        """Sets up client before every test."""
        app.config['TESTING'] = True
        app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

    def test_home_page(self):
        """Check to make sure correct HTML is displayed"""

        with app.test_client() as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>ForEx Converter</h1>', html)
            self.assertIn('<h3>Available Conversions</h3>', html)
            
    def test_converter(self):
        "Tests if 1 USD is converted to 1 USD"
        self.assertEqual(Converter.convert_currency(self, 'USD', 'USD', 1), 1)
    
    def test_load_coverter_page(self):
        "Tests to see if request is successful and loads correctly on paged"
        with app.test_client() as client:
            response = client.get('/converted?convert-from=USD&convert-to=USD&amount=100')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>ForEx Converter</h1>', html)
            self.assertIn('<h3>Available Conversions</h3>', html)
            self.assertIn('Converted Amount: 100 USD = 100', html)    