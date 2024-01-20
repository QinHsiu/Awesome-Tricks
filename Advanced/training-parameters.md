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
  - [超级参数调优](https://analyticsindiamag.com/top-8-approaches-for-tuning-hyperparameters-of-machine-learning-models/)

- XGBoost
  - [参数设置技巧](https://mp.weixin.qq.com/s/OWkde_9FAT6TxoSr9AzlQw)   

- 模型压缩
  - [加快LLM推理速度(2080Ti跑70B)](https://mp.weixin.qq.com/s/FqxwoR-466_je-7beFZh1A)
  - [扩散模型加速](https://mp.weixin.qq.com/s/u3RN-Ci4iReKNYHQW7ghgA)
  - [模型压缩算法](https://mp.weixin.qq.com/s/Z3dbhoUcXSCY5xCFtSy5hQ)
  - [大模型训练Scaling Law](https://mp.weixin.qq.com/s/lSLJhyT5LKuKtZMD3EaR_A)
  - [模型压缩技术-推荐中的应用](https://mp.weixin.qq.com/s/Z5aRBj6AEXGEkpikFkOcEw)

- 参数高效微调
  - [使用LoRA技术微调RoBert、Llama2、Mistral](https://mp.weixin.qq.com/s/UX561hFEtFNr3WZ8O88Iig)

- 提示工程
  - [提示代替微调](https://mp.weixin.qq.com/s/28ltYJ7h14ooSMGGQV7Brg)

- 大模型修复bad case
  - [大模型修复bad case](https://mp.weixin.qq.com/s/mLmL19FI-ZpX9BMJWpY2rw)

- 缓解LLM幻觉
  - [OPERA-基于注意力惩罚与回退机制](https://mp.weixin.qq.com/s/SOnP9quuRXKOB-qImIYLGg)
