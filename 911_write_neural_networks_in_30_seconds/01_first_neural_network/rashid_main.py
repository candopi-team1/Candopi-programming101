# python notebook for Make Your Own Neural Network
# code for a 3-layer neural network, and code for learning the MNIST dataset
# (c) Tariq Rashid, 2016
# license is GPLv2


import numpy
import scipy.special
import matplotlib.pyplot

from nn2 import  NeuralNetwork


PIXEL_LENGTH_OF_IMG_SIDE = 28


no_of_input_nodes =  PIXEL_LENGTH_OF_IMG_SIDE * PIXEL_LENGTH_OF_IMG_SIDE
no_of_hidden_nodes = 200 # changeable e.g 234, 867 
no_of_output_nodes = 10

learning_rate = 0.1

neunet1 = NeuralNetwork(no_of_input_nodes, no_of_hidden_nodes, no_of_output_nodes, learning_rate)


# load the mnist training data CSV file into a list
# training_data_file = open("mnist_dataset/mnist_train.csv", 'r') # 20 mins

training_data_file = open("mnist_dataset/mnist_train_100.csv", 'r')


training_data_list = training_data_file.readlines()
training_data_file.close()
# print(type(training_data_list[0] )) # <class 'str'>

# train the neural network

# epochs is the number of times the training data set is used for training
epochs = 5


for e in range(epochs):
    # go through all records in the training data set
    for record in training_data_list:
        # split the record by the ',' commas
        all_values = record.split(',')
        # scale and shift the inputs
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        
        # create the target output values (all 0.01, except the desired label which is 0.99)
        targets = numpy.zeros(no_of_output_nodes) + 0.01
        
        # all_values[0] is the target label for this record
        targets[int(all_values[0])] = 0.99  
        neunet1.train(inputs, targets) # both <class 'numpy.ndarray'>





# load the mnist test data CSV file into a list
# test_data_file = open("mnist_dataset/mnist_test.csv", 'r')
test_data_file = open("mnist_dataset/mnist_test_10.csv", 'r')

test_data_list = test_data_file.readlines()
test_data_file.close()



# test the neural network

# scorecard for how well the network performs, initially empty
scorecard = []

# go through all the records in the test data set
for record in test_data_list:
    # split the record by the ',' commas
    all_values = record.split(',')
    # correct answer is first value
    correct_label = int(all_values[0])
    # scale and shift the inputs
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    
    # query the network
    outputs = neunet1.query(inputs)

    # the index of the highest value corresponds to the label
    label = numpy.argmax(outputs)
    
    # append correct or incorrect to list
    if (label == correct_label):
        # network's answer matches correct answer, add 1 to scorecard
        scorecard.append(1)
    else:
        # network's answer doesn't match correct answer, add 0 to scorecard
        scorecard.append(0)

    



# calculate the performance score, the fraction of correct answers
scorecard_array = numpy.asarray(scorecard)
print ("performance = ", scorecard_array.sum() / scorecard_array.size)



