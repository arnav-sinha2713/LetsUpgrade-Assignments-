
import unittest
import check_prime

class testPrime(unittest.TestCase):
    def isprime(self):
        a=15
        result=check_prime.checkprime(a)
        self.assertEquals(result, True)
        
if __name__=="__main__":
    unittest.main()
