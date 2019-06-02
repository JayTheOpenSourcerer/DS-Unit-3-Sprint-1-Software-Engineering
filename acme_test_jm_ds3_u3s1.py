import unittest
from acme_jm_ds3_u3s1 import Product
from acme_report_jm_ds3_u3s1 import generate_products, ADJECTIVES, NOUNS

'''Jason Meil''' 
class AcmeProductTests(unittest.TestCase):
    """
    Making sure Acme products are the tops!
    """

    def test_default_product_price(self):
        """
        Test default product price being 10.
        """

        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """
        Test default product price being 10.
        """

        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_custom(self):
        """
        Test default product price being 10.
        """

        prod = Product('Test Product', 5, 10, 2.5)
        self.assertEqual(prod.price, 5)
        self.assertEqual(prod.weight, 10)
        self.assertEqual(prod.flamibility, 2.5)

    def test_default_product_internal(self):
        """
        Test default product price being 10.
        """

        prod = Product('Test Product', 4, 10, 2.5)
        self.assertEqual(prod.stealability(), 'Not so stealable...')
        self.assertEqual(prod.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    """
    Acme Report Testing
    """
    
    def test_default_num_products(self):
        prod = generate_products()
        self.assertEqual(len(prod), 30)

    def test_legal_names(self):
        for prod in generate_products():
            prodname = prod.name.split(' ')
            self.assertTrue(prodname[0] in ADJECTIVES)
            self.assertTrue(prodname[1] in NOUNS)


if __name__ == '__main__':
    unittest.main()