- 图像增强
  - 颜色增强，该方式通过将每一个通道乘以随机选择的系数来随机调整图像的色调、饱和度和亮度。系数从[0:6,1:4]的范围内进行选择，以确保生成的图像不会过于失真，代码实现如下所示：
    ``` 
    def color_skew(image):
        h, s, v = cv2.split(image)
        h = h * np.random.uniform(low=0, high=6)
        s = s * np.random.uniform(low=1, high=4)
        v = v * np.random.uniform(low=0, high=6)
        return cv2.merge((h, s, v))
    ```
  - RGB标准化，该方式通过让每一个通道的值减去每一个通道的平均值并除以通道的标准差来标准化图像的RGB通道，代码实现如下：
    ```
      def rgb_norm(image):
        r, g, b = cv2.split(image)
        r = (r - np.mean(r)) / np.std(r)
        g = (g - np.mean(g)) / np.std(g)
        b = (b - np.mean(b)) / np.std(b)
        return cv2.merge((r, g, b))
    ```
  - Black and White，该方式将图像转换为灰度色彩，也即将图像转换为黑白图片，代码实现如下：
    ```
      def black_and_white(image):
         return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    ```
  - 灰度+高斯混合
        
- 其他资源
  - [图像增强方法](https://mp.weixin.qq.com/s/6xiGEQVzkCGcAthbr9qUOQ)
  - [CV训练tricks](https://mp.weixin.qq.com/s/die5NJQijonKGHizoJkHFw)