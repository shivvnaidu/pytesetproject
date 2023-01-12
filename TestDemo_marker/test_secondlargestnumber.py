import unittest
def max(l):
    n = len(l)
    for i in l (1,n):
        if l[i]>90:
            second_largest = l[i]
    return second_largest
class my_test(unittest.TestCase):
    def test1(self,l):
        l=[10,20,4,56,80,99]
        r=max(l)
        f(l)
        self.assertEqual(r,99)
        print(" Second largest number is : ",r)
