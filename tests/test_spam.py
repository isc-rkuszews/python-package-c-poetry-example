from unittest import TestCase

import bobtest as sp


class bobtestTest(TestCase):
    def test_bobtest(self):
        print(dir(sp))
        sp.system("ls -l")
