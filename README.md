# Teraki ML Test 

**Q.4 -** _**In k-fold cross-validation, what is the role of parameter k? What happens when it is too big? When it is too small?**_

_Ans:_ 

The parameter _k_ decides how in how many parts do we split the data or in other words we make k subsets of the data in order to split the dataset into Training set and Testing set. We make k runs. So, we use _(k-1)/k_ fraction of data for training and _1/k_ fraction for testing. When the value of _k_ is too big, at every run we get larger training set, which reduces the bias of the model while estimating generalization error rate. The extreme case (leave-one-out) would be _k_=_N_, where _N_ is number of instances in a dataset. That means it utilizes the whole dataset except one point and that point is used as testing. It is computationally exhaustive approach when considering large dataset as cross-validation procedure has to be repeated _N_ times. If the value of _k_ is too small, it can be seen that the dataset is not exhaustively used in order to train & test there can be bias in estimation of generalization error rate small _k_ and high variance can be observed in testing error as it is computed over small number of test instances.



**Q.2 -** _**Suppose you have a neural network for binary classification. The input layer contains 20 nodes, and there are two hidden layers of sizes 10 and 5. All layers are fully connected. What are the shapes of the weights of this network? How many parameters are there in the network in total? Which activation function would you use 1.) in the intermediate layers 2.) in the final layer?**_

_Ans:_ 

The weights would be in form of matrix, so the weights to the first hidden layer would 20x10 and to the second layer it would be 10x5 to out it would be 5x1. So total of 255 weights. I would use ReLu for intermediate layers and Sigmoid function in the final layer. So total of 272 parameter in network would be present.
