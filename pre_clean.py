# @Version  : 1.0
# @athuor   : Tenyson
# @File     : pre_clean
# @Time     : 2025/6/25 13:31

import pandas as pd

#加载数据
raw_data = pd.read_excel("JD_Product_Reviews.xlsx")

# 1. 选择关键列 评价内容(content),评分（总分5分）(score)并重命名为Content,Rating
raw_data = raw_data[['评价内容(content)','评分（总分5分）(score)']].rename(columns = {'评价内容(content)':'Content','评分（总分5分）(score)':'Rating'})
print(raw_data.columns)

# 2. 过滤无效数据

#过滤评价内容 空值
raw_data = raw_data.dropna()

#过滤重复值 重复的数据保留第一次出现
raw_data = raw_data.drop_duplicates()

# 筛选评价内容小于50字符
raw_data = raw_data[raw_data['Content'].str.len()<50]


# 3. 构建二分类标签

#1正面 0负面
raw_data['Label'] = raw_data['Rating'].apply(lambda x: 1 if x > 3 else 0)

# 4. 保存待标注数据

#随机抽取200条数据 标注，调优
sample_raw_data = raw_data.sample(200,random_state= 42)

sample_raw_data[['Content','Label']].to_csv("reviews_to_label.csv",index=False)

#保存清洗数据
raw_data.to_csv("pre_clean.csv",index=False)