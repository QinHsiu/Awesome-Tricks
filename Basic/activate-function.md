### 使用非线性激活函数来捕捉数据之间的非线性关系，常用的非线性激活函数如下：
- Sigmoid激活函数
  $$sigmoid(x)=\frac{1}{1+e^{-x}}$$
- ReLU激活函数
  $$relu(x)=max(x,0)$$
- Tanh激活函数
  $$tanh(x)=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}$$
- Tips：一般情况下tanh效果更好一点，其是rescaled的sigmoid函数，sigmoid输出都为正数，根据BP规则，某层的神经元的权重的梯度的符号和后层误差的一样，也就是说，如果后一层的误差为正，则这一层的权重全部都要降低，如果为负，则这一层梯度全部为负，权重全部增加，权重要么都增加，要么都减少，这明显是有问题的；tanh是以0为对称中心的，这会消除在权重更新时的系统偏差导致的偏向性。（当然这是启发式的，并不是说tanh一定比sigmoid的好），ReLU也是很好的选择，最大的好处是，当tanh和sigmoid饱和时都会有梯度消失的问题，ReLU就不会有这个问题，而且计算简单，当然它会产生dead neurons；激活函数一个主要作用是限定输出范围，一般情况下不使用，二分类任务一般使用sigmod激活函数，多分类一般使用softmax激活函数；

### 参考资料：
- [神经网络训练trick总结](https://mp.weixin.qq.com/s/QfSzmQT1XcZGphrD-z0qKA)

  
