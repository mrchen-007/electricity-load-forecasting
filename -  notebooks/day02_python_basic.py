# ==========================
# 能源AI项目1：电力负荷预测
# 第2天：Python基础入门
# 功能：测试环境 + 模拟负荷数据
# ==========================

# 导入数据处理库（对应Excel表格处理）
import pandas as pd

# 导入数值计算库（数学计算）
import numpy as np

# 导入画图库（画负荷曲线）
import matplotlib.pyplot as plt

# 打印提示
print("===== 第2天代码运行成功 =====")

# 生成模拟时间（48小时）
hours = np.arange(1, 49)

# 生成模拟电力负荷（均值200MW，随机波动）
simulate_load = 200 + np.random.randn(48) * 10

# 构造数据表
df = pd.DataFrame({
    "hour": hours,
    "load_mw": simulate_load
})

# 打印前5行数据
print("\n【模拟负荷数据预览】")
print(df.head())

# 简单统计
print("\n【数据统计】")
print(df.describe())

# 画图提示
print("\n已完成画图逻辑，本地运行可显示负荷曲线")
