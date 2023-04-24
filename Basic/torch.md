- 改变学习率，使用周期性学习率替代原先的静态学习率，因为学习率schedule的选择对模型的收敛速度和泛化性能有巨大影响
  - 参考论文：《Cyclical Learning Rates for Training Neural Networks》、《Super-Convergence: Very Fast Training of Neural Networks Using Large Learning Rates》
  - 实现链接：[optim](https://pytorch.org/docs/stable/optim.html)
  
- 在数据加载中使用多个worker和页锁定内存
  - 使用torch.utils.data.DataLoader时候设置num_workers>0并且将pin_memory设置为True
  - 参考链接：[data](https://pytorch.org/docs/stable/data.html)
  
- 将batch调大，这样可以加快模型收敛速率
  - 参考论文：《An Empirical Model of Large-Batch Training》、《How to get 4x speedup and better generalization using the right batch size》
  
- 使用自动混合精度，自动决定使用什么精度进行运算,使用方法如下

```
  import torch
# Creates once at the beginning of training
scaler = torch.cuda.amp.GradScaler()

for data, label in data_iter:
   optimizer.zero_grad()
   # Casts operations to mixed precision
   with torch.cuda.amp.autocast():
      loss = model(data)

   # Scales the loss, and calls backward()
   # to create scaled gradients
   scaler.scale(loss).backward()

   # Unscales gradients and calls
   # or skips optimizer.step()
   scaler.step(optimizer)

   # Updates the scale for next iteration
   scaler.update()
```
 
- 使用不同优化器，Adamw是一种具有权重衰减的Adam，使用torch.optim.AdamW实现

- cudaNN基准，使用torch.backends.cudnn.benchmark = True实现

- 避免cpu与gpu之间频繁地数据传输

- 使用梯度/激活 checkpointing
  - 参考资料：[Priya Goyal](https://github.com/prigoyal/pytorch_memonger/blob/master/tutorial/Checkpointing_for_PyTorch_models.ipynb)

- 使用梯度累积
  - 参考文章：《Training Neural Nets on Larger Batches: Practical Tips for 1-GPU, Multi-GPU & Distributed setups》
  - 代码实现如下
    ```
      model.zero_grad()                                   # Reset gradients tensors
      for i, (inputs, labels) in enumerate(training_set):
          predictions = model(inputs)                     # Forward pass
          loss = loss_function(predictions, labels)       # Compute loss function
          loss = loss / accumulation_steps                # Normalize our loss (if averaged)
          loss.backward()                                 # Backward pass
          if (i+1) % accumulation_steps == 0:             # Wait for several backward steps
              optimizer.step()                            # Now we can do an optimizer step
              model.zero_grad()                           # Reset gradients tensors
              if (i+1) % evaluation_steps == 0:           # Evaluate the model when we...
                  evaluate_model()                        # ...have no gradients accumulat
    ```
- 使用分布式数据并行进行多GPU训练
  - 使用 torch.nn.DistributedDataParallel 实现
  - 参考链接：[dist_overview](https://pytorch.org/tutorials/beginner/dist_overview.html)
  
  
- 设置梯度为None而不是0
  - 梯度设置为. zero_grad(set_to_none=True) 而不是 .zero_grad()
  - 参考链接：[optim](https://pytorch.org/docs/stable/optim.html)
  
  
- 使用.as_tensor()而不是.tensor()
  - 后者总是会复制数据，应该尽量避免该操作
  
  
- 必要的时候打开调试工具，例如 autograd.profiler、autograd.grad_check、autograd.anomaly_detection

- 使用梯度裁剪
  - 使用梯度裁剪（gradient = min(gradient, threshold)）可以加速收敛，在 PyTorch 中可以使用 torch.nn.utils.clip_grad_norm_来实现
  
- 在BatchNorm之前关闭bias
 
- 验证期间关闭梯度计算，使用torch.no_grad()实现

- 在输入时先进行batch归一化





