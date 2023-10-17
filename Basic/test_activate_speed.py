import torch 
import torch.nn as nn
from time import time

def test(n):
    a=torch.randn((n,n,n))
    # sigmoid
    b_sigmoid=time()
    sigmoid_output=nn.Sigmoid()(a)
    e_sigmoid=time()
    
    # softmax
    b_softmax=time()
    softmax_output=nn.Softmax()(a)
    e_softmax=time()

    # relu
    b_relu=time()
    relu_output=nn.ReLU()(a)
    e_relu=time()

    # tanh
    b_tanh=time()
    tanh_output=nn.Tanh()(a)
    e_tanh=time()

    # gelu
    b_gelu=time()
    gelu_output=nn.GELU()(a)
    e_gelu=time()



    print("sigmoid cost:{0}\n softmax cost:{1}\n relu cost:{2}\n tanh cost:{3}\n gelu cost:{4}".format((e_sigmoid-b_sigmoid),(e_softmax-b_softmax),(e_relu-b_relu),(e_tanh-b_tanh),(e_gelu-b_gelu)))

if __name__=="__main__":
   n=int(input())
   test(n)



