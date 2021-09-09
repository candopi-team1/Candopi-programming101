# python notebook for Make Your Own Neural Network
# code for a 3-layer neural network, and code for learning the MNIST dataset
# (c) Tariq Rashid, 2016
# license is GPLv2

import numpy
# scipy.special for the sigmoid function expit()
import scipy.special


class NeuralNetwork:    
    
    # initialise the neural network
    def __init__(self, no_of_inputnodes, no_of_hiddennodes, no_of_outputnodes, learningrate):
        # set number of nodes in each input, hidden, output layer
        self.no_of_inodes = no_of_inputnodes
        self.no_of_hnodes = no_of_hiddennodes
        self.no_of_onodes = no_of_outputnodes
        
        # link weight matrices, wih and who
        # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
        # w11 w21
        # w12 w22 etc 
        self.wih = numpy.random.normal(0.0, pow(self.no_of_inodes, -0.5), (self.no_of_hnodes, self.no_of_inodes))
        self.who = numpy.random.normal(0.0, pow(self.no_of_hnodes, -0.5), (self.no_of_onodes, self.no_of_hnodes))

        # learning rate
        self.lnn_rate = learningrate
        
        # activation function is the sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)

        
        
    def feed_forward(self, inputs, targets):                
        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        return final_outputs, hidden_outputs



    def update_weight(self, weights_of_layer, errors_of_nx_layer, outputs_of_nx_layer, outputs_of_layer):
        derivative_of_sigmoid    = outputs_of_nx_layer * (1.0 - outputs_of_nx_layer)
        what_do_you_call_it      = (errors_of_nx_layer * derivative_of_sigmoid)
        T_of_outputs_of_layer    =  numpy.transpose(outputs_of_layer)
        
        weights_of_layer += self.lnn_rate * numpy.dot(what_do_you_call_it, T_of_outputs_of_layer )

        

    def backprop(self, targets, final_outputs, hidden_outputs, inputs):        
        # output layer error is the (target - actual)
        output_errors = targets - final_outputs
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors) 

        self.update_weight(weights_of_layer=self.who, errors_of_nx_layer=output_errors, outputs_of_nx_layer=final_outputs,  outputs_of_layer=hidden_outputs )        
        self.update_weight(weights_of_layer=self.wih, errors_of_nx_layer=hidden_errors, outputs_of_nx_layer=hidden_outputs, outputs_of_layer=inputs )

        
    # train the neural network
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        final_outputs, hidden_outputs= self.feed_forward(inputs, targets)
        
        self.backprop(targets, final_outputs, hidden_outputs, inputs)

       
    
    # query the neural network
    def query(self, inputs_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        
        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        
        return final_outputs


