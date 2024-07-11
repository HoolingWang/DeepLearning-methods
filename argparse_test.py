import argparse

# 创建 ArgumentParser 实例
parser = argparse.ArgumentParser("用来介绍parser！！")

# 添加命令行参数
#help用于在命令行中打印“--batch_size”的用法，可以提醒自己和其他使用此程序的人
parser.add_argument('--batch_size', type=int, default=64, help="定义batch")
parser.add_argument('--epoch', type=int, default=200, help="定义训练轮数")
parser.add_argument('--learning_rate', type=float, default=0.001, help="定义学习率")

# 解析命令行参数
args = parser.parse_args()

# 访问命令行参数的值
model_batch_size = args.batch_size
model_epoch = args.epoch
model_learning_rate = args.learning_rate

# 输出batch_size参数的值
print(model_batch_size)
print(model_epoch)
print(model_learning_rate)






