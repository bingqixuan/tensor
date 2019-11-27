import xlrd
import os
import numpy as np
from tensorflow import keras
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))


# 产业分类
def find_peer(name, nrows=0, table=0):
    array = []
    for rownum in range(2, nrows):
        row = table.row_values(rownum)
        if row[8] == name:
            array.append(row)
    return array


# 训练模型并保存
def train(hy, x, y):
    # 添加一层神经网络，输入的参数是一维向量
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    # 为模型添加sgd优化器 损失函数为均方误差
    model.compile(optimizer='sgd', loss='mse')
    # 输入的数据及正确的数据
    xs = np.array(x, dtype=float)
    ys = np.array(y, dtype=float)
    # 训练模型50轮
    model.fit(xs, ys, epochs=50)
    # 输出模型详细信息
    model.summary()
    # 保存模型
    ind = '%d' %hy
    name = ind + 'model.h5'
    model.save(name)


# 循环遍历取结果
def forfunc(data, index):
    array = []
    for item in range(0, len(data)):
        array.append(data[item][index])
    return array


def excel_table_byname(file=u'stock.xlsx', by_name=u'Sheet1'):  # 修改自己路径
    data = open_excel(file)
    table = data.sheet_by_name(by_name)  # 获得表格
    nrows = table.nrows  # 拿到总共行数

    for hy in range(1, 11):
        # 1. 取出每个行业的样本
        wind1 = find_peer(hy, nrows, table)
        # 2. 取出该行业的每股收益-自变量
        x = forfunc(wind1, 6)
        # 3. 取出该行业的每股价格-因变量
        y = forfunc(wind1, 2)
        # 4. 训练模型
        train(hy, x, y)


def main():
    excel_table_byname()


if __name__ == "__main__":
    main()
