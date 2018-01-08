import unittest


import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import naive_bayes


class TestNaiveBayes(unittest.TestCase):
    
    def test_create_probability_matrix(self):
        data_set = [["type","Mango","Peach","Total"],["yellow",1,2,3,6],["sweet",4,5,6,15],["total",7,8,9,24]]
        #hold = data_set
        matrix = naive_bayes.create_probability_matrix(data_set)
        
        #self.assertEqual(hold, data_set)
        
        print data_set
        print matrix
    
    def test_probability_of_events(self):
        data_set = [["type","Mango","Peach","Total"],["yellow",1,2,3,6],["sweet",4,5,6,15],["total",7,8,9,24]]
    
        matrix = naive_bayes.create_probability_matrix(data_set)
        likelihood = naive_bayes.probability_of_events(matrix,0)
        
        self.assertEquals(likelihood, 0.044444444444444439)
    
        likelihood = naive_bayes.probability_of_events(matrix,1)
        self.assertEquals(likelihood,0.1111111111111111)
        
    def test_parse_result_index(self):
        
        data_set = [["type","Mango","Peach","Total"],["yellow",1,2,3,6],["sweet",4,5,6,15],["total",7,8,9,24]]
        
        self.assertEquals(naive_bayes.parse_result_index(data_set,"Mango"),0)
        self.assertEquals(naive_bayes.parse_result_index(data_set,"Peach"),1)
    
    
    
    def test_probability_of_result(self):
    
        data_set = [["type","Mango","Peach","Total"],["yellow",1,2,3,6],["sweet",4,5,6,15],["total",7,8,9,24]]
    
        matrix = naive_bayes.create_probability_matrix(data_set)
        
        self.assertEquals(naive_bayes.probability_of_result(matrix,0),0.29166666666666669)

    def test_probability_of_denominator(self):
        
        data_set = [["type","Mango","Peach","Total"],["yellow",1,2,3,6],["sweet",4,5,6,15],["total",7,8,9,24]]
        
        self.assertEquals(naive_bayes.probability_of_denominator(data_set,0),504)
        self.assertEquals(naive_bayes.probability_of_denominator(data_set,1),576)
        
    def test_naive_bayes(self):
        
        data_set = [["type","Mango","Peach","Total"],["yellow",1,2,3,6],["sweet",4,5,6,15],["total",7,8,9,24]]
        
        self.assertEquals(naive_bayes.naive_bayes(data_set,"Mango"),1)


        
if __name__ == "__main__":
    unittest.main()