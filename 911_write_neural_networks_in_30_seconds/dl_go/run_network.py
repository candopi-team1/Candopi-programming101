# tag::test_setup[]
from load_mnist import load_data
from network import SequentialNetwork
from layers import DenseLayer, ActivationLayer

training_data, test_data = load_data()  # <1>


"""
print(type(training_data)) # list
print(len(training_data))  # 60 000
print(len(test_data))      # 10 000
"""


len_train_dat= len(training_data)
len_test_dat= len(test_data)
kilo= 1000
new_len1=int(0.5*kilo); # to speed up on slow PC's ;-)
new_len2=int(0.2*kilo);

training_data, test_data = training_data[:new_len1], test_data[:new_len2] 

net = SequentialNetwork()  # <2>

net.add(DenseLayer(784, 392))  # <3>
net.add(ActivationLayer(392))
net.add(DenseLayer(392, 196))
net.add(ActivationLayer(196))
net.add(DenseLayer(196, 10))
net.add(ActivationLayer(10))  # <4>


# <1> First, load training and test data.
# <2> Next, initialize a sequential neural network.
# <3> You can then add dense and activation layers one by one.
# <4> The final layer has size 10, the number of classes to predict.
# end::test_setup[]

# tag::test_run[]
net.train(training_data, epochs=10, mini_batch_size=10,
          learning_rate=3.0, test_data=test_data)  # <1>

# <1> You can now easily train the model by specifying train and test data, the number of epochs, the mini-batch size
# and the learning rate.
# end::test_run[]

# https://github.com/maxpumperla/deep_learning_and_the_game_of_go/tree/master/code/dlgo/nn

