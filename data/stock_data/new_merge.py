import pandas as pd
with open('/Users/duanshuxi/Desktop/大数据经济学大作业/整合数据/all_name.txt',encoding='utf_8_sig') as f1:
    names=f1.readlines()
    path=[]
    for t in names:
        n='/Users/duanshuxi/Desktop/大数据经济学大作业/整合数据/'+t[:-1]
        path.append(n)
# f=pd.DataFrame(columns=['时间','评论'])
#print(path)
df1=pd.read_csv('/Users/duanshuxi/Desktop/大数据经济学大作业/整合数据/incomplete_all_data_2.csv',encoding='utf_8_sig')
df=pd.DataFrame(columns=['日期','评论'])
for i in path:
     print(i)
     df2=pd.read_csv(i,encoding='utf_8_sig')
     df2=df2[['日期','评论']]
     df=pd.concat([df,df2])
df.to_csv('complete.csv',encoding='utf_8_sig')