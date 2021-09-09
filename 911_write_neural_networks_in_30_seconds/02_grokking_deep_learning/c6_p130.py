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
      layer_0 = streetlights[i:i+1]
      layer_1 = relu(np.dot(layer_0, weights_0_1))
      layer_2 =      np.dot(layer_1, weights_1_2)

      layer_2_error += np.sum((layer_2 - goal_pred[i:i+1]) ** 2)

      layer_2_delta = (layer_2 - goal_pred[i:i+1])
      layer_1_delta=  layer_2_delta.dot(weights_1_2.T)*relu2deriv(layer_1)

      weights_1_2 -= alpha * layer_1.T.dot(layer_2_delta)
      weights_0_1 -= alpha * layer_0.T.dot(layer_1_delta)

   if(iteration % 10 == 9):
      print("Error:" + str(layer_2_error))
      #OK print(layer_0); print(layer_1); print(layer_2)
      #OK print(weights_0_1); print(weights_1_2)
      #OK print(layer_2_delta); print(layer_1_delta);
      #OK print("layer2_weight_delta");print(layer_1.T.dot(layer_2_delta));
      #OK print("layer1_weight_delta");print(layer_0.T.dot(layer_1_delta));

      

"""
layer2_weight_delta
[[0.        ]
 [0.        ]
 [0.        ]
 [0.00376362]]
 
layer1_weight_delta
[[0.         0.         0.         0.05686159]
 [0.         0.         0.         0.05686159]
 [0.         0.         0.         0.05686159]]
"""
      
"""
print();
[  [0.27511184]  ] ==> 
[  [0.20835876]  ] ==> 
[  [0.05981475]  ] ==> 
[  [0.00433851]  ]



print(layer_1_delta);

[  [-0.          0.         -0.          0.15093618]  ] ==> 
[  [-0.          0.         -0.          0.146626]    ] ==> 
[  [-0.          0.         -0.          0.05686159]  ] ==> 
[  [-0.          0.         -0.          0.00465724]  ]

"""

"""
print(layer_0); 
[[1 1 1]]


print(layer_1); 
[[-0.         -0.         -0.          0.00404159]]


print(layer_2)
[[0.00433851]]

"""


"""
print(streetlights)
[[1 0 1]
 [0 1 1]
 [0 0 1]
 [1 1 1]]


print(goal_pred)
[[1]
 [1]
 [0]
 [0]]



print(weights_0_1)
[[-0.16595599    0.91056768   -0.99977125   -0.90023925]
 [-0.70648822   -0.92794391   -0.62747958    0.89703458]
 [-0.20646505   -0.03308324   -0.16161097    0.00237016]  ]
 
==>
[[-0.16595599    0.91056768   -0.99977125   -0.90023925]
 [-0.70648822   -0.92794391   -0.62747958    0.88874965]
 [-0.20646505   -0.03308324   -0.16161097    0.01118313]  ]


 
print(weights_1_2)
[ [-0.5910955 ]
  [ 1.13962134]
  [-0.94522481]
  [ 1.11023793]  ]
  
==>

[ [-0.5910955 ]
  [ 1.13962134]
  [-0.94522481]
  [ 1.10362956]  ]

 
"""
