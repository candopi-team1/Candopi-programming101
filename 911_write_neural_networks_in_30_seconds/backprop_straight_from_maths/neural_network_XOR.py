import numpy as np

def sigmoid(z):
    return 1 / (1+np.exp(-z))

def sigmoid_derivative(z):
    return np.exp(-z)/((1+np.exp(-z))**2)

class Layer(object):
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(input_size, output_size) 
        self.bias = np.zeros((1, output_size))
        
        self.input       = None
        self.weighted_sum= None
        self.output      = None
        
    def forward_prop(self, input_data):
        self.input       = input_data
        self.weighted_sum= np.dot(self.input, self.weights) + self.bias
        self.output      = sigmoid(self.weighted_sum )

        return self.output

    def backprop(self, delta_to_passbk, weight1, learning_rate):        
  
           delta_to_passbk= np.dot(delta_to_passbk, weight1.T) * sigmoid_derivative(self.weighted_sum)
           gradient = np.dot(layer.input.T, delta_to_passbk) 

           self.weights = self.weights -  learning_rate * gradient
    
           return delta_to_passbk
    

def cost_function(y, y_hat):
    J = 0.5*sum((y-y_hat)**2)
    
    return J

def update_last_layer(last_layer, learning_rate):    
    y_hat = last_layer.output
    z2    = last_layer.weighted_sum
    
    delta_to_passbk = np.multiply(-(y-y_hat),sigmoid_derivative(z2))
    
    gradient_y = np.dot(last_layer.input.T, delta_to_passbk)
    last_layer.weights = last_layer.weights - learning_rate * gradient_y

    return delta_to_passbk,y_hat

"""
Shorter
x = np.array([ [0, 1], [1, 0], [14, 10],
               [7,8], [77,8], [12,13],
               [12,3], [22,4], [67,1.90],
               
               [1, 1], [0, 0], [9.01,9.0],
               [8.8888, 8.8888], [1,1], [2,2],
               [45,45], [34,34], [11.08,11.08]

               ])
"""

x = np.array([ [0, 1], [1, 0], [2, 0],
               [0,2], [3,8], [2,3],     [10,12], [13,18], [12,13],
               [1,3], [2,4], [6,1.90],
               
               [1, 1], [0, 0], [9.0,9.0],
               [8.8, 8.8], [1,1], [2,2], [7,7], [54,54], [9,9],
               [45,45], [34,34], [11.08,11.08], 

               ])


y = np.array([ [1], [1], [1],  [1], [1], [1],
               [1], [1], [1],  [1], [1], [1],
               [0], [0], [0],  [0],[0], [0],
               [0],[0], [0],   [0],[0], [0]    ])


layers=[]

num_input = 2

num_hidden = 5
num_output = 1

layer_h= Layer(num_input,num_hidden)
layer_i= Layer(num_hidden,num_hidden)
layer_y= Layer(num_hidden,num_output)

layers.append(layer_h)
layers.append(layer_i)
layers.append(layer_y)
last_layer=layers[-1]

alpha          = 0.01 # learing_rate   
num_iterations = 5000 # epochs

cost = []
for i in range(num_iterations):
    
    #perform forward propagation and predict output
    output=x
    for layer in layers:
        output=layer.forward_prop(output)

    """ 
    for layer in layers:
      print(layer.weights);
      print(layer.bias);
        
      print(layer.input);    
      print(layer.weighted_sum);
      print(layer.output);  
      print("\n-------------------------------------\n")
    """
     
    delta_to_passbk, y_hat= update_last_layer(last_layer, alpha)
    
    for layer in reversed(layers[:-1]):
        idx       =layers.index(layer)
        weight1   = layers[idx+1].weights
        
        delta_to_passbk = layer.backprop(delta_to_passbk, weight1,  alpha)
 
    
    #compute cost
    c = cost_function(y, y_hat)
    
    #store the cost
    cost.append(c)


low_costs=[c for c in cost if c[0] < 0.16]

print(cost[:10])
print("\n---------------------------\n");
print(cost[(num_iterations-10):])
print("\n---------------------------\n");

if len(low_costs) > 0:
 print(cost[(num_iterations-10):])
 print()
 print(low_costs)
else:
    print("Costs higher than 0.16")

    
""" BEST RESULTS 
...([0.12992725]), array([0.12986975]), array([0.12981231]), array([0.1297549]), array([0.12969753]), array([0.1296402]),
array([0.12958292]), array([0.12952567]), array([0.12946847]), array([0.1294113]), array([0.12935418]), array([0.12929709]),
array([0.12924005]), array([0.12918305]), array([0.12912609]), array([0.12906917]), array([0.12901228]), array([0.12895544]),
array([0.12889864]), array([0.12884188]), array([0.12878516]), array([0.12872848]), array([0.12867184]), array([0.12861524]),
array([0.12855868]), array([0.12850216]), array([0.12844568]), array([0.12838924]), array([0.12833284]), array([0.12827648]),
array([0.12822016]), array([0.12816388]), array([0.12810764]), array([0.12805143]), array([0.12799527]), array([0.12793915]),
array([0.12788307]), array([0.12782702]), array([0.12777102]), array([0.12771506]), array([0.12765913]), array([0.12760325]),
array([0.1275474]), array([0.12749159]), array([0.12743583]), array([0.1273801]), array([0.12732441]), array([0.12726876]),
array([0.12721315]), array([0.12715758]), array([0.12710205]), array([0.12704655]), array([0.1269911]), array([0.12693568]),
array([0.12688031]), array([0.12682497]), array([0.12676967]), array([0.12671441]), array([0.12665919]), array([0.12660401]),
array([0.12654886]), array([0.12649376]), array([0.12643869]), array([0.12638366]), array([0.12632867]), array([0.12627372]),
array([0.12621881]), array([0.12616394]), array([0.1261091]), array([0.1260543]), array([0.12599955]), array([0.12594483]),
array([0.12589014]), array([0.1258355]), array([0.12578089]), array([0.12572633]), array([0.1256718]), array([0.12561731]),
array([0.12556285]), array([0.12550844]), array([0.12545406])]

"""
