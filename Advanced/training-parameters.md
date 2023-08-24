- 学习率
  - 主要有三种方法，静态的，基于规则的更新，动态的更新；静态的方法一般设置为0.001，基于规则的一般在训练一段时间之后减小学习率（当验证误差不再下降之后将lr减小到原来的一半，使用迭代次数的倒数作为权重），第三种使用自适应的学习率adagrad或者使用额外的参数来学习lr；
  
- batch size
  - 太大的batch size会减小的梯度下降的随机性，对模型的精度产生负面影响，大的batch size需要训练更多的epoch来获得比较好的效果；使用小批量可以帮助训练过程中跳出局部最小值，另外使得模型进行更加平缓的局部最小值，提高泛化性能；

- 超参数自动化
  - [重参数化](https://mp.weixin.qq.com/s/KaJAR72W_1Ji_yOZNLmq9g)
  - [超参数自动化搜索](https://mp.weixin.qq.com/s/E2osIx2PEoR7ateEIN0FLQ)
  - [机器学习中的超参数搜索方法](https://mp.weixin.qq.com/s/t2ftmpU9VfC9PawDYvepHA)
  - [竞赛中参数搜索技巧](https://mp.weixin.qq.com/s/Wx1WMvQQQUV46ckGbE3Eag)
  - [WWW2022-MetaBalance](https://mp.weixin.qq.com/s/iJixbNLVPfARxndI0u5Lcg)

- 模型压缩
  - [模型压缩算法](https://mp.weixin.qq.com/s/Z3dbhoUcXSCY5xCFtSy5hQ)
 
