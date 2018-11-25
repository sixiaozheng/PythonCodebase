import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import time
#multilayer perception
mnist=input_data.read_data_sets('/data/mnist',one_hot=True)

##########
X = tf.placeholder(tf.float32,[None,784],name='X_placeholder')
Y = tf.placeholder(tf.int32,[None,10],name='Y_placeholder')
#########
n_hidden_1=256
n_hidden_2=256
n_input=784
n_classes=10

weight={
    'h1':tf.Variable(tf.random_normal([n_input,n_hidden_1]),name='W1'),
    'h2':tf.Variable(tf.random_normal([n_hidden_1,n_hidden_2]),name='W2'),
    'out':tf.Variable(tf.random_normal([n_hidden_2,n_classes]),name='W')
}

biases={
    'b1':tf.Variable(tf.random_normal([n_hidden_1]),name='b1'),
    'b2':tf.Variable(tf.random_normal([n_hidden_2]),name='b2'),
    'out':tf.Variable(tf.random_normal([n_classes]),name='bias')
}
#########
def multilayer_perceptron(x,weight,biases):
    layer_1=tf.add(tf.matmul(x,weight['h1']),biases['b1'],name='fc_1')
    layer_1=tf.nn.relu(layer_1,name='relu_1')
    layer_2=tf.add( tf.matmul(layer_1,weight['h2']),biases['b2'],name='fc_2')
    layer_2=tf.nn.relu(layer_2,name='relu_2')
    out_layer=tf.add(tf.matmul(layer_2,weight['out']),biases['out'],name='fc_3')
    return out_layer
##########
pred=multilayer_perceptron(X,weight,biases)
##########
learning_rate=0.001
loss_all=tf.nn.softmax_cross_entropy_with_logits(logits=pred,labels=Y,name='cross_entropy_loss')
loss=tf.reduce_mean(loss_all,name='avg_loss')
optimizer=tf.train.AdamOptimizer(learning_rate).minimize(loss)
##########
init=tf.global_variables_initializer()
##########
training_epochs=15
batch_size=128
display_step=1

with tf.Session() as sess:
    sess.run(init)
    writer=tf.summary.FileWriter('./graphs/MLP_DNN',sess.graph)

    for epoch in range(training_epochs):
        avg_loss=0
        total_batch=int(mnist.train.num_examples/batch_size)
        for i in range(total_batch):
            batch_x,batch_y=mnist.train.next_batch(batch_size)
            _,los=sess.run([optimizer,loss],feed_dict={X:batch_x,Y:batch_y})
            avg_loss+=los/total_batch

        if epoch%display_step==0:
            print('Epoch:','%04d'%(epoch+1),'cost=', '{:.9f}'.format(avg_loss))

    print('Optimization Finished!')

    correct_prediction=tf.equal(tf.argmax(pred,1),tf.argmax(Y,1))
    accuracy=tf.reduce_mean(tf.cast(correct_prediction,'float'))
    print('Accuracy:',accuracy.eval({X:mnist.test.images,Y:mnist.test.labels}))
    writer.close()


