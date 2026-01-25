import sys
import os
import unittest

# 添加 scripts 目录到 path
sys.path.append(os.path.join(os.path.dirname(__file__), '../scripts'))

from calc import add

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
