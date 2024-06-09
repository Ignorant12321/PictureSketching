# 使用说明

功能：利用`Python`的`PIL`库实现图片风格素描化

语法说明：

```tex
usage: 图片风格素描化.exe [-h] -i INPUT [-o OUTPUT] [-m {1,2,3,4,5}] [-s SKETCH] [-b BLUR] [-e ENHANCE]

程序功能：图像处理（黑白，素描，浮雕，模糊，锐化）

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        输入图像
  -o OUTPUT, --output OUTPUT
                        输出图像
  -m {1,2,3,4,5}, --mode {1,2,3,4,5}
                        图像处理模式: {1: '黑白', 2: '素描', 3: '浮雕', 4: '模糊', 5: '锐化'}【默认为素描模式】
  -s SKETCH, --sketch SKETCH
                        素描阴影程度【默认为-1，即不使用该参数而采用另一种算法】
  -b BLUR, --blur BLUR  模糊模式层数
  -e ENHANCE, --enhance ENHANCE
                        锐化模式层数
```

具体案例:

- Pycharm终端（前提安装`PIL`库）：

| 示例命令                                              | 说明               |
| :---------------------------------------------------- | ------------------ |
| `python main.py  -h`                                  | 查看指令的使用说明 |
| `python main.py -i 示例图片.png -o 输出图片.png -s 1` | 图片风格素描化     |

- 打包程序：

  ```cmd
  pyinstaller main.py -i 素描.ico --name 图片风格素描化 -F
  ```

- 运行程序：

  在cmd中打开该程序

  ```cmd
  图片风格素描化.exe  -i 示例图片.png -o output.png -s 1
  ```

  

# 参考资料

- [Python3 用PIL处理图像（二）——将图片装换成素描](https://blog.csdn.net/u014663232/article/details/105777826)
- [Python -- argparse(命令行与参数解析)_python argparse 数组-CSDN博客](https://blog.csdn.net/weixin_43990846/article/details/107824317)