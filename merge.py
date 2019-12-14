import pandas as pd
df=pd.DataFrame(columns=['序号','时间','发布人','评论','标题'])
#file_name=['000002万科','000063中兴通讯','000333美的集团','000538云南白药','000725京东方','000876新希望','002024苏宁易购','002271东方雨虹','002352顺丰控股','002415海康威视','300498温氏股份','600019宝钢股份','600031三一重工','600050中国联通',]
with open('Users/duanshuxi/Desktop/大数据经济学大作业/股民数据（新浪财经）/所有文件名.txt',encoding='utf-8') as f1:
    names=f1.readlines()
    path=[]
    for t in names:
        n='/Users/duanshuxi/Desktop/大数据经济学大作业/股民数据（新浪财经）/'+t[:-1]
        path.append(n)/

# print(path)
for p in path:
    print(p)
    with open(p, encoding='gbk') as f2:
        lines=f2.readlines()
        for i in lines:
            list=i.split(',')
            d={'序号':list[0],'时间':list[1],'发布人':list[2],'评论':list[3],'标题':list[4]}
            df.loc[df.shape[0]+1]=d
print(df)

df.to_csv('all_data.csv')