import numpy as np

def naive_bayes(data_set,result):
    """Given a matrix find the probability of an event given a list of given a list of vectors
    - Naive because it is assumed events are independent
    - Zero Conditional Probability Problem: if an item in a vector is zero then the probably of given row is zero
    """
    result_index = parse_result_index(data_set,result)
    
    likelyhood_table = create_probability_matrix(data_set)
    
    likelihood = probability_of_events(likelyhood_table,result_index)
    
    prob_of_result = probability_of_result(likelyhood_table,result_index)
    
    denominator = probability_of_denominator(data_set,result_index)
    
    return (likelihood * prob_of_result) / denominator
    

def  probability_of_denominator(data_set,result_index):
    return (data_set[-1][result_index+1]) * (len(data_set[-1]) - 2) * data_set[-1][-1]

def probability_of_result(likelyhood_table,result_index):
    return likelyhood_table[result_index][-1]

def parse_result_index(data_set,result):
    count = 0
    for i in data_set[0]:
        if i == result:
            return count - 1   
        count += 1
    
def probability_of_events(likelyhood_table, result_index):
        likelihood = 1
        for probability in likelyhood_table[result_index][:-1]:
            likelihood = likelihood * probability
        return likelihood
    
    
def create_probability_matrix(data_set):
    """Takes augmented matrix and creates a likelihood table 
    each entry is the probability within the vector - total is at the bottom
    """
    matrix = np.zeros(shape=(len(data_set[0])-1, len(data_set)-1))
    
    i,j = 0,0
    for vector in data_set[1:]:
        last_item = vector.pop(-1)
        for element in vector[1:]:
            matrix[i][j] = np.divide(float(element),float(last_item))
            i += 1
        vector.append(last_item)
        #matrix[i][j] = last_item
        j += 1
        i = 0
    
    
    return matrix
    
    