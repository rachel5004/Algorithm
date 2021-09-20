import unittest

def solution(N):
    return N

class Test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(1, solution(1))
        self.assertEqual(1, solution(2))

if __name__=='___main__':
    unittest.main()