import numpy as np
import tensorflow as tf
matrix_1=np.zeros((3,4))
print(matrix_1)
matrix_1_2=np.reshape(matrix_1,(2,6))
print(matrix_1_2)

matrix_2=tf.zeros((3,4))
print(matrix_2)
matrix_2_2=tf.reshape(matrix_2,(2,6))
print(matrix_2_2)

#tensorboard --logdir=I:\ProjectFiles\pycharm_conda\graphs\const_add
a=tf.constant([[2,2]],name='a')
b=tf.constant([[0,1],[2,3]],name='b')
c=tf.multiply(a,b,name='dot_product')
d=tf.matmul(a,b,name='mat_mul')
with tf.Session() as sess:
    writer=tf.summary.FileWriter('./graphs/const_mul_2',sess.graph)
    print(sess.run(c))
    print(sess.run(d))
writer.close()

with tf.variable_scope('meh') as scope:
	a = tf.get_variable('a', [10])
	b = tf.get_variable('b', [100])

writer = tf.summary.FileWriter('./graphs/test', tf.get_default_graph())

x=tf.Variable(2.0)
y=2.0*(x**3)
z=3.0+y**2
grad_z=tf.gradients(z,[x,y])
with tf.Session() as sess:
    sess.run(x.initializer)
    print(sess.run(grad_z))

W=tf.Variable(10)
assign_op=W.assign(100)
with tf.Session() as sess:
    sess.run(W.initializer)
    print(W.eval())
    print(sess.run(assign_op))

my_var=tf.Variable(2,name='my_var')
my_var_times_two=my_var.assign(2*my_var)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(my_var_times_two))
    print(sess.run(my_var_times_two))
    print(sess.run(my_var_times_two))

a=tf.placeholder(tf.float32,shape=[3])
b=tf.constant([5,5,5],tf.float32)

c=a+b
with tf.Session() as sess:
    print(sess.run(c,feed_dict={a:[1,2,3]}))

a=tf.add(2,5)
b=tf.multiply(a,3)

with tf.Session() as sess:
    print(sess.run(b,feed_dict={a:15}))