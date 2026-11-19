import unittest
from app import saludar

class TestApp(unittest.TestCase):

    def test_saludar(self):
        self.assertEqual(
            saludar(),
            "Hello World desde DevSecOps!"
        )

if __name__ == "__main__":
    unittest.main()
