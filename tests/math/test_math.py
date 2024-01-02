from unittest import TestCase

import bobtest.math as math


class bobtestTest(TestCase):
    def test_bobtest(self):
        print(dir(math))
        assert math.add(1, 2) == 3

        assert math.add(3, 4) == 7
