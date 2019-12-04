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


# 训练最大值模型并保存
def trainMaxValue(hy, x, y):
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
    name = ind + 'MaxValue.h5'
    model.save(name)


# 训练最大值模型并保存
def trainKLowValue(hy, x1, x2, y):
    # 添加一层神经网络，输入的参数是一维向量
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    # 为模型添加sgd优化器 损失函数为均方误差
    model.compile(optimizer='sgd', loss='mse')
    # 输入的数据及正确的数据
    xs1 = np.array(x1, dtype=float)
    xs2 = np.array(x2, dtype=float)
    ys1 = np.array(y, dtype=float)
    # 训练模型50轮
    model.fit([xs1, xs2], ys1, epochs=50)
    # 输出模型详细信息
    model.summary()
    # 保存模型
    ind = '%d' %hy
    name = ind + 'KLowValue.h5'
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
    # nrows = table.nrows  # 拿到总共行数
    nrows = 18  # 拿到总共行数

    for hy in range(1, 13):
        # 1. 取出每个行业的样本
        wind1 = find_peer(hy, nrows, table)
        if len(wind1) == 0:
            continue
        # 取出该行业的每股收益
        ps = forfunc(wind1, 6)
        # 取出该行业的每股最高价格
        pv = forfunc(wind1, 2)
        # 取出该行业的开板最低值
        pl = forfunc(wind1, 9)
        # 训练模型
        # trainMaxValue(hy, ps, pv)
        trainKLowValue(hy, ps, pv, pl)


def main():
    excel_table_byname()


if __name__ == "__main__":
    main()
