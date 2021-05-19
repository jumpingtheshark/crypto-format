import unittest
from crypto4 import CryptoFormatter


class CryptoFormatterTest(unittest.TestCase):
    def testFormat1(self):
        c = CryptoFormatter()
        self.assertEqual(c.cformat("James Bond 7", 3), "James Bond 007")

    def testFormat2(self):
        c = CryptoFormatter()
        self.assertEqual(c.cformat("PI=3.14", 2), "PI=03.14")


    def testFormat3(self):
        c = CryptoFormatter()
        self.assertEqual(c.cformat("It's 3:13pm", 2), "It's 3:13pm")


    def testFormat4(self):
        c = CryptoFormatter()
        self.assertEqual(c.cformat("It's 12:13pm", 2), "It's 12:13pm")

    def testFormat5(self):
        c = CryptoFormatter()
        self.assertEqual(c.cformat("99UR1337", 6), "000099UR001337")


if __name__ == '__main__':
    unittest.main()

'''
Examples:
Inputs (I): "James Bond 7", 3
Output (O): "James Bond 007"

I: "PI=3.14", 2
O: "PI=03.14"

I: "It's 3:13pm", 2
O: "It's 03:13pm"

I: "It's 12:13pm", 2
O: "It's 12:13pm"

I: "99UR1337", 6
O: return "000099UR001337"



echo "# crypto-format" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/jumpingtheshark/crypto-format.git
git push -u origin main
'''
