- 目标
  - 将一个NxH（N表示数目、H表示隐藏层单元数目）的字典映射为MxH（M<<N）的字典
- 压缩方法
  - 行维度出发，也即将N变为M，H不变
    - 利用hash操作
      - Double Hash (NIPS 2017 [1])
        - 定义k个独立的hash函数，每个函数的空间皆为M，对于NxH中的每一个向量都将其通过哈希函数映射到M个表示中，然后对于映射为同一个位置的k个向量进行聚合（求和、均值、相乘、concat）之后会形成MxH个向量用于表示原始的向量空间NxH
      - Hybrid Hash（Recsys 2020 [2]）
        - 针对特征分布的长尾效应，将NxH中的一部分重要的特征不变进行一一映射（例如nxH仍然保留），对于剩下的部分(N-n)xH将其用Double Hash映射到(M-n)xH中
      - QR (KDD 2020 [3])
        - 为了缓解冲突，先将NxH划分为多个子集S，对于集合S里的任意两个元素a和b，存在一个互补划分方式使得a和b所属的划分结果在b和a分区里是均匀分布的。具体方法为在划分两个hash矩阵时，一个取模，一个取商，来降低hash整体冲突率并确保每个特征key表示的唯一性。
      - Binary Code Based Hash (CIKM 2021 [4])
        - 引入二进制编码来唯一对应不同的hash id，不论M有多小，都能够为不同的特征值赋予唯一的独特索引值
  - 有监督方法
    - 卷积压缩，NxH经过多次卷积操作变为MxH
      - 参考方法：https://mp.weixin.qq.com/s/wxCsR6hFQN-Evky4JTlNBw
    - 使用自编码器
  - 无监督方法
    - K-means聚类，将NxH放进聚类模型，聚为M类，最后变为MxH
    - PCA降维度，直接将NxH映射为MxH
      - 参考方法：https://mp.weixin.qq.com/s/aqjf63AgPc0fUkyYIjcpdw
  - 值精度出发，也即从fp32转到int8、int4进行量化（可以极大节约存储空间）[7,8]
    - PTQ又称为后训练量化，也就是不修改模型训练，只在模型推送的时候做模型量化。这种方式一定会比原模型损失精度，但是便捷快速，会增加一个反量化的计算代价。
    - QAT又称为训练中量化，一般是通过在原来模型中插入伪量化(Fake-Quantization)节点，在训练时模拟量化引入的误差，通过梯度下降来微调模型权重，统计并更新量化参数，要修改训练代码。
  - 列维度出发，也即将H变为H1，其中H1<<H
    - 训练层面出发，可以做蒸馏[10]、做预训练剪枝 [5]
- 参考文献
  - 1.Double Hash: https://arxiv.org/abs/1709.03933
  - 2.Hybrid Hash: https://arxiv.org/abs/2007.14523
  - 3.QR Trick: https://arxiv.org/abs/1909.02107
  - 4.Binary Code: https://arxiv.org/abs/2109.0247
  - 5.https://mp.weixin.qq.com/s/Z3dbhoUcXSCY5xCFtSy5hQ
  - 6.卷积神经网络压缩方法：https://mp.weixin.qq.com/s/wxCsR6hFQN-Evky4JTlNBw
  - 7.Training Transformers with 4-bit Integers:https://arxiv.org/pdf/2306.11987.pdf
  - 8.大模型int8量化技术：https://mp.weixin.qq.com/s/_JirS9knfTlta0qOzo3i6A
  - 9.大模型蒸馏：https://github.com/google-research/distilling-step-by-step
  - 10.推荐模型中embedding的压缩方式：https://mp.weixin.qq.com/s/l4w3FyoF48bi7vR_LhOdyw
