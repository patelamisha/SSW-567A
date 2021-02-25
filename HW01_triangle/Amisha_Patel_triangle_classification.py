""" Author  :: Amisha Patel 
     Created :: 02/06/2021
     Assigment :: Testing triangle classification """
import unittest    
def classifyTriangle(a,b,c):
    """This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.""" 
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if (a > (b + c)) or (b > (a + c)) or (c > (a + b)):
        return 'NotATriangle'
    elif a == b == c:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        return 'Right'
    elif (a != b) and  (b != c):
        return 'Scalene'
    else:
        return 'Isoceles'        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(', a, ',', b, ',', c, ')=', classifyTriangle(a, b, c),sep="")
class TestTriangles(unittest.TestCase):
    def testSet1(self): 
        self.assertEqual(classifyTriangle(3, 4 ,5),'Right','3,4,5 is a Right triangle')    
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5, 3, 4 is a Right triangle')
        self.assertEqual(classifyTriangle(3, 5, 4), 'Right', '3, 5, 4 is a Right triangle')    

    def testMyTestSet2(self): 
        self.assertEqual(classifyTriangle(1,1,3),'NotATriangle','should be a notatrianle')
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(2, 3,5),'Scalene','Should be Isoceles')
        self.assertEqual(classifyTriangle(10,10,20),'Isoceles','Should be Equilateral')
    def testInvalidInput(self):
    	self.assertEqual(classifyTriangle(-1,"three",-5),'InvalidInput')
        
if __name__ == '__main__':
    runClassifyTriangle(1, 2, 3)
    runClassifyTriangle(1, 1, 1)
    runClassifyTriangle(20, 20, 40)
    runClassifyTriangle(3, 4, 5)
    runClassifyTriangle(1, 1, 5)
    runClassifyTriangle(-1,0, 0)

    unittest.main(exit=False)         
