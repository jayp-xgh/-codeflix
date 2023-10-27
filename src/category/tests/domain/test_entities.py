from datetime import datetime
import unittest
from category.domain.entities import Category

class TestCategory(unittest.TestCase):

    def test_constructor(self):
        category = Category('Movie', 'test', True, datetime.now())
        self.assertEqual(category.name, 'movie')
        self.assertEqual(category.description, 'test')
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.create_at, datetime)
