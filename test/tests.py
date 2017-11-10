import unittest


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        print('Setting up...')

    def tearDown(self):
        print('Tearing down...')

    def test_sample(self):
        assert 1 == 1

if __name__ == '__main__':
    unittest.main()
