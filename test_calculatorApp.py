from ast import Num
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
    
    # CheckUserInput
    def test_InputEmpty(self):
        self.assertRaises(ValueError, check_user_input,"")

    def test_InputInt(self):
        self.assertEqual(check_user_input("1"), 1)

    def test_InputFloat(self):
        self.assertEqual(check_user_input("1.1"), 1.1)

    def test_InputNotNum(self):
        self.assertRaises(ValueError, check_user_input,"x")


    # Add
    def test_Added(self):
        self.assertEqual(add(1,2),3)
        

    # Subtract 
    def test_Subtracted(self):
        self.assertEqual(subtract(3,2),1)


    # Multiply
    def test_Multiplied(self):
        self.assertEqual(multiply(3,2),6)


    # Divide
    def test_DenominatorZero(self):
        self.assertRaises(ZeroDivisionError, divide, 1, 0)
    
    def test_NumeratorZero(self):
        self.assertEqual(divide(0,2),0)

    def test_Divided(self):
        self.assertEqual(divide(6,2),3)
    

    # Calculate
    def test_InputNotNone(self):
        self.assertRaises(ValueError, calculate, '1',None,1) 
        self.assertRaises(ValueError, calculate, '1',1,None)
        
    def test_InvalidInputChoice(self):
        self.assertRaises(Exception, calculate, '5',1,1)

    def test_AddChoice(self):
        with mock.patch('calculatorApp.add', return_value = 3):
            result = calculate('1',1,2)
        self.assertEqual(result, 3)

    def test_SubtractChoice(self):
        with mock.patch('calculatorApp.subtract', return_value = 1):
            result = calculate('2',3,2)
        self.assertEqual(result, 1)
    
    def test_MultiplyChoice(self):
        with mock.patch('calculatorApp.multiply', return_value = 6):
            result = calculate('3',2,3)
        self.assertEqual(result, (2, '*', 3, '=', 6))
    
    def test_DivideChoice(self):
        with mock.patch('calculatorApp.divide', return_value = 3):
            result = calculate('4',6,2)
        self.assertEqual(result, (6, '/', 2, '=', 3))

    def test_DenominatorZeroInDivideChoice(self):
        self.assertRaises(ZeroDivisionError, calculate, '4','1','0')
        self.assertRaises(ZeroDivisionError, calculate, '4',1,0)


    #isExit 
    def test_ExitChoiceNo(self):
        self.assertEqual(isExit("no"),True)

    def test_ExitChoiceYes(self):
        self.assertEqual(isExit("yes"),False)

    def test_InvalidInputChoiceInExit(self):
        self.assertRaises(ValueError, isExit,'Yes')

        
    def tearDown(self):
        print("tearDown .. ")
        #self.patcher1.stop()#or add this and remove self.addCleanup(self.patcher1.stop) in startup but this is not recommened!

if __name__ == '__main__':
	unittest.main()
