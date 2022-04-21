import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *
import calculatorApp


class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")
        # self.patcher1 = patch('calculatorApp.add', return_value = 5)
        # self.MockClass1 = self.patcher1.start()
        # self.addCleanup(self.patcher1.stop)
    
    # CheckUserInput()
    def test_IfUserInputEmpty(self):
        self.assertRaises(ValueError, check_user_input,"")

    def test_IfUserInputInt(self):
        self.assertEqual(check_user_input("1"), 1)

    def test_IfUserInputFloat(self):
        self.assertEqual(check_user_input("1.1"), 1.1)

    def test_IfUserInputNotNum(self):
        self.assertRaises(ValueError, check_user_input,"NaN")

    # Add()
    def test_IfAdded(self):
        self.assertEqual(add(1,2),3)

    


    def test_AddPass(self):
        self.assertEqual(add(6,3), 9)# will execute the add
        self.assertEqual(calculate('1',6,3), 5) # will call the mock

    def test_AddInvalid(self):
        self.assertNotEqual(calculate('1',9,3), 9)

    def test_DividByZerrorEx1(self):
        with self.assertRaises(ValueError):
             calculate('4','3','w')
    
    ##OR

    def test_DividByZerrorEx2(self):
        self.assertRaises(ValueError, calculate, '4','3','w') 

    def test_DividByZerrorRegex(self):
        with self.assertRaisesRegex(ValueError, "input is not a number!"):
             calculate('4','3','w')

    
    def test_AddPassWithMockEx1(self):
        with mock.patch('calculatorApp.add', return_value = 6):
            result = calculate('1',2,4)
        self.assertEqual(result, 6)

    @mock.patch('calculatorApp.add', return_value = 4)
    def test_AddPassWithMockEx2(self, mock_check):
        result = calculate('1',3,2)
        self.assertEqual(result, 4)


    def test_AddPassWithMocEx3(self):
        assert calculatorApp.add is self.MockClass1
        self.assertEqual(calculate('1',2,6), 5)
        


    def tearDown(self):
        print("tearDown .. ")
        #self.patcher1.stop()#or add this and remove self.addCleanup(self.patcher1.stop) in startup but this is not recommened!


class TestCalculateWithoutMock(unittest.TestCase):
    def test_AddPass(self):
        self.assertEqual(add(6,3), 9)
        self.assertEqual(calculate('1',6,3), 9)

if __name__ == '__main__':
	unittest.main()
