import numpy as np

np.random.seed(1)

def relu(x):
    return (x > 0) * x # returns x if x > 0
                       # return 0 otherwise

def relu2deriv(output):
    return output>0 # returns 1 for input > 0
                    # return 0 otherwise

streetlights = np.array( [[ 1, 0, 1 ],
                          [ 0, 1, 1 ],
                          [ 0, 0, 1 ],
                          [ 1, 1, 1 ] ] )

goal_pred = np.array([[ 1, 1, 0, 0]]).T  # walk_vs_stop
    
alpha = 0.2
hidden_size = 4

weights_0_1 = 2*np.random.random((3,hidden_size)) - 1
weights_1_2 = 2*np.random.random((hidden_size,1)) - 1

layer_0, layer_1, layer_2 = None, None, None

for iteration in range(60):
   layer_2_error = 0
   for i in range(len(streetlights)):

      if iteration == 0 and i==0:
          print(streetlights);          print(streetlights.shape);print('\n');
          print(goal_pred);          print(goal_pred.shape);print('\n');
          weights_0_1_old=weights_0_1        
          weights_1_2_old= weights_1_2

          
      layer_0 = streetlights[i:i+1]
      layer_1_pre_relu=np.dot(layer_0, weights_0_1)
      layer_1 = relu(np.dot(layer_0, weights_0_1))
      
      layer_2 =      np.dot(layer_1, weights_1_2)

      layer_2_error += np.sum((layer_2 - goal_pred[i:i+1]) ** 2)

      layer_2_delta = (layer_2 - goal_pred[i:i+1])
      layer_1_delta=  layer_2_delta.dot(weights_1_2.T)*relu2deriv(layer_1)

      weights_1_2 -= alpha * layer_1.T.dot(layer_2_delta)
      weights_0_1 -= alpha * layer_0.T.dot(layer_1_delta)
      
      if iteration == 0 and i==0:
         print("LAYERS") 
         print(layer_0); print(layer_0.shape); print('\n');
         print("layer_1_pre_relu= ",layer_1_pre_relu); print(layer_1_pre_relu.shape); print('\n');
         print("layer_1         =",layer_1); print(layer_1.shape); print('\n');
         
         print(layer_2); print(layer_2.shape); print('\n');
         
         print("LAYER DELTAS")
         print("layer_2_delta= ",layer_2_delta); print(layer_2_delta.shape);
         print("layer_1_delta= ",layer_1_delta); print(layer_1_delta.shape);print('\n');

         print("WEIGHTS")
                   
         print("weights_0_1_OLD= ", weights_0_1_old);          print(weights_0_1_old.shape); 
         print("weights_0_1    = ", weights_0_1);             print(weights_0_1.shape);

         print("weights_1_2_OLD=",  weights_1_2_old);          print(weights_1_2_old.shape);print('\n');
         print("weights_1_2    = ", weights_1_2);              print(weights_1_2.shape);print('\n');
         
         
         print("WEIGHT DELTAS");
         print("layer2_weight_delta");print(layer_1.T.dot(layer_2_delta));print(layer_1.T.dot(layer_2_delta).shape);
         print("layer1_weight_delta");print(layer_0.T.dot(layer_1_delta));print(layer_0.T.dot(layer_1_delta).shape); print('\n');

   if(iteration % 10 == 9):
      print("Error:layer_2_error: " + str(layer_2_error))

      

