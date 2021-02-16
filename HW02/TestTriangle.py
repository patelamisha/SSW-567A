""" Author :Amisha Patel
    Date : 02/16/2021
    Assignment : Test Classify Triagnle"""
import unittest
from Triangle import classifyTriangle
class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testRightTriangleA(self): 
        self.assertNotEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,4,3),'Right')

    def testEquilateralTrianglesA(self):         
        self.assertEqual(classifyTriangle(1,0,1),'Equilateral','1,1,1 should be equilateral')
    
    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(4, 14, 2),'Isosceles')

    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 11, 11),'Scalene')
        
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 6, 0),'NotATriangle')
 
    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(-5, 9, 1),'NotATriangle')

    def testInvalidInputA(self):
    	self.assertEqual(classifyTriangle(a,0,0),'InvalidInput')
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()