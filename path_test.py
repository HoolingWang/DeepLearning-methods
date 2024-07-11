from pathlib import Path
import sys

# a = Path(__file__).resolve()
# b = a.parents[0]
# c = sys.path
# # sys.path.append(str(b))
#
#
#
#
# print(a)
# print(b)
# print(c)
# print(c)

# img_path = Path(r"E:\pycharm\Retinex\result.jpg")
# img_name = img_path.name

# cur_path = Path(__file__)

# img_path = Path(r"E:\pycharm\Retinex\result.jpg")
# parent_path = img_path.parent
# parents0_path = img_path.parents[0]
# parents1_path = img_path.parents[1]
# parents2_path = img_path.parents[2]
# print(parent_path, parents0_path, parents1_path, parents2_path, sep = '\n')

# img_path = Path(r"./result.jpg")
# abs_path = img_path.resolve()


# path_suffix = img_path.suffix

# file_path = Path(r"E:\pycharm\Retinex\some_result")
# for path in file_path.iterdir():
#     print(path)

# file_path = Path(r"E:\pycharm\Retinex")
# img_path = file_path.joinpath(r"result.jpg")

file_path = Path(r"E:\pycharm\Retinex\some_result")
for dir in file_path.glob("*.png"):
    print(dir)

# print(img_path)



