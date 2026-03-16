# ==========================
# 造价转行能源AI · 第3天
# 电力负荷数据读取与探索
# ==========================

# 1. 导入需要的工具包
import pandas as pd
import matplotlib.pyplot as plt

# 注释：pandas 用来读表格、处理数据
# 注释：matplotlib 用来画图

# 2. 设置中文字体（防止图表中文乱码）
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams['axes.unicode_minus'] = False

# 3. 创建模拟的电力负荷数据（也可以替换成真实CSV）
data = {
    'hour': list(range(24)),   # 0~23小时
    'load': [320, 310, 305, 300, 315, 340,
             380, 420, 450, 470, 480, 475,
             460, 450, 440, 460, 490, 520,
             550, 560, 530, 490, 430, 370]
}

# 4. 转成DataFrame表格（造价版Excel）
df = pd.DataFrame(data)

# 5. 查看前5行数据
print("数据前5行：")
print(df.head())

# 6. 查看数据基本信息
print("\n数据基本信息：")
print(df.info())

# 7. 查看统计信息（均值、最大、最小等）
print("\n数据统计：")
print(df.describe())

# 8. 绘制24小时负荷曲线
plt.figure(figsize=(10, 4))
plt.plot(df['hour'], df['load'], marker='o', color='#1f77b4')
plt.title('24小时电力负荷曲线')
plt.xlabel('时间(小时)')
plt.ylabel('负荷(MW)')
plt.grid(True, linestyle='--', alpha=0.3)
plt.show()
