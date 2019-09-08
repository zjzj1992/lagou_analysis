#!/usr/bin/env python
# coding: utf-8

# 这份数据是我用爬虫软件从拉钩网上爬取的，是一份关于全国所有数据分析岗位的数据，而我的目的有以下几点：
# #找出数据分析岗位在不同地区的分布情况
# #不同地区的数据分析岗位的薪资分布情况
# #招收数据分析工程师都有哪些类型的公司
# #数据分析岗位对于学历的要求
# #总结数据分析岗位的硬性要求有哪些

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


# In[2]:


jobs_data = pd.read_excel("D:/jobs.xls")


# In[25]:


len(jobs_data)


# 一共有450条数据

# In[27]:


jobs_data


# 数据中有些属性不够规范，也有些是用不到的，下面先做一下处理

# In[3]:


jobs_data.columns


# In[4]:


jobs_data = jobs_data.drop(['标题链接','li_b_l1','format-time','li_b_r','缩略图','li_b_l2','li_b_l3','li_b_l4'],axis=1)


# In[30]:


jobs_data


# In[5]:


jobs_data.columns = ['title','infomation','salary','address','company_name','industry','description']


# In[32]:


jobs_data


# 下面对数据分析岗位的地区分布进行统计

# In[165]:


address = {}

#统计每个地区出现的次数
for i in range(len(jobs_data)):
    addr = jobs_data['address'][i].split("·")[0][1:3]
    address[addr] = address.get(addr,0) + 1


# In[166]:


#排序
address = sorted(address.items(),key=lambda address:address[1],reverse=False)


# In[167]:


address_number = []
address_addr = []

for i in range(len(address)):
    address_number.append(address[i][1])
    address_addr.append(address[i][0])


# In[171]:


matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(9,9))
plt.barh(address_addr,address_number,height=0.9,color='steelblue',alpha=0.8)
plt.yticks(range(24),address_addr)
plt.xlim(0,170)
plt.xlabel("数量")
plt.title("不同地区数据分析岗位的分布情况")
for x, y in enumerate(address_number):
    plt.text(y + 0.2, x - 0.1, '%s' % y)
plt.show()


# 从结果可以看出，北京对于数据分析的需求是最多的，有156条，然后依次是上海、深圳、广州、杭州，所以对于数据分析岗位来说，只有一线大城市才会有需求，小城市的需求量非常少

# 下面对岗位的薪资分布进行统计

# In[200]:


jobs_data


# In[239]:


jobs_salary = {}

for i in range(len(jobs_data)):
    #最低薪资
    low_salary = int(jobs_data['salary'][i].split('-')[0][:len(jobs_data['salary'][i].split('-')[0])-1])
    #最高薪资
    high_salary = int(jobs_data['salary'][i].split('-')[1][:len(jobs_data['salary'][i].split('-')[1])-1])
    #10k以内
    if (low_salary + high_salary)//2 < 10:
        jobs_salary['10k以内'] = jobs_salary.get('10k以内',0) + 1
    #15k
    elif (low_salary + high_salary)//2 < 16:
        jobs_salary['15k左右'] = jobs_salary.get('15k左右',0) + 1
    #25k
    elif (low_salary + high_salary)//2 < 26:
        jobs_salary['25k左右'] = jobs_salary.get('25k左右',0) + 1
    #35k
    elif (low_salary + high_salary)//2 < 36:
        jobs_salary['35k左右'] = jobs_salary.get('35k左右',0) + 1
    #40以上
    else:
        jobs_salary['40k以上'] = jobs_salary.get('40k以上',0) + 1


# 数据中的薪资区间很混乱，很难做统一的统计，所以我是通过平均值来定义薪资范围的

# In[254]:


fig = plt.figure(figsize=(9,9))
labels = list(jobs_salary.keys())
nums = list(jobs_salary.values())
explode = (0,0,0,0,0)
plt.pie(nums,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150,textprops={'fontsize':15,'color':'black'})
plt.show()


# 从上面的结果可以看出，该岗位在全国的薪资表现是比较高的，15k左右和25k左右占了很大的比重，两个极端占的比重很少，不过这样的表现也只存在于一线城市

# 下面分析一下北京、上海和深圳这三座城市在薪资方面的具体表现是怎样的

# 首先是北京

# In[262]:


#将address属性做精简
for i in range(len(jobs_data)):
    jobs_data['address'][i] = jobs_data['address'][i].split('·')[0][1:3]


# In[263]:


jobs_data


# In[264]:


jobs_beijing = jobs_data[jobs_data.address == '北京']


# In[271]:


jobs_beijing.index = np.arange(len(jobs_beijing))


# In[273]:


jobs_beijing_salary = {}

for i in range(len(jobs_beijing)):
    #最低薪资
    low_salary = int(jobs_beijing['salary'][i].split('-')[0][:len(jobs_beijing['salary'][i].split('-')[0])-1])
    #最高薪资
    high_salary = int(jobs_beijing['salary'][i].split('-')[1][:len(jobs_beijing['salary'][i].split('-')[1])-1])
    #10k以内
    if (low_salary + high_salary)//2 < 10:
        jobs_beijing_salary['10k以内'] = jobs_beijing_salary.get('10k以内',0) + 1
    #15k
    elif (low_salary + high_salary)//2 < 16:
        jobs_beijing_salary['15k左右'] = jobs_beijing_salary.get('15k左右',0) + 1
    #25k
    elif (low_salary + high_salary)//2 < 26:
        jobs_beijing_salary['25k左右'] = jobs_beijing_salary.get('25k左右',0) + 1
    #35k
    elif (low_salary + high_salary)//2 < 36:
        jobs_beijing_salary['35k左右'] = jobs_beijing_salary.get('35k左右',0) + 1
    #40以上
    else:
        jobs_beijing_salary['40k以上'] = jobs_beijing_salary.get('40k以上',0) + 1


# In[283]:


fig = plt.figure(figsize=(9,9))
labels = list(jobs_beijing_salary.keys())
nums = list(jobs_beijing_salary.values())
explode = (0,0,0,0,0)
plt.pie(nums,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150,textprops={'fontsize':15,'color':'black'})
plt.title("北京数据分析岗位薪资分布情况")
plt.show()


# 上面是北京的情况，其中有一半的岗位薪资在25k左右，然后是15k的也比较多，所以依然是15k和25
# k左右的薪资是最多的，两个极端的岗位薪资很少

# 然后是上海

# In[275]:


jobs_shanghai = jobs_data[jobs_data.address == '上海']
jobs_shanghai.index = np.arange(len(jobs_shanghai))


# In[278]:


jobs_shanghai_salary = {}

for i in range(len(jobs_shanghai)):
    #最低薪资
    low_salary = int(jobs_shanghai['salary'][i].split('-')[0][:len(jobs_shanghai['salary'][i].split('-')[0])-1])
    #最高薪资
    high_salary = int(jobs_shanghai['salary'][i].split('-')[1][:len(jobs_shanghai['salary'][i].split('-')[1])-1])
    #10k以内
    if (low_salary + high_salary)//2 < 10:
        jobs_shanghai_salary['10k以内'] = jobs_shanghai_salary.get('10k以内',0) + 1
    #15k
    elif (low_salary + high_salary)//2 < 16:
        jobs_shanghai_salary['15k左右'] = jobs_shanghai_salary.get('15k左右',0) + 1
    #25k
    elif (low_salary + high_salary)//2 < 26:
        jobs_shanghai_salary['25k左右'] = jobs_shanghai_salary.get('25k左右',0) + 1
    #35k
    elif (low_salary + high_salary)//2 < 36:
        jobs_shanghai_salary['35k左右'] = jobs_shanghai_salary.get('35k左右',0) + 1
    #40以上
    else:
        jobs_shanghai_salary['40k以上'] = jobs_shanghai_salary.get('40k以上',0) + 1


# In[284]:


fig = plt.figure(figsize=(9,9))
labels = list(jobs_shanghai_salary.keys())
nums = list(jobs_shanghai_salary.values())
explode = (0,0,0,0,0)
plt.pie(nums,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150,textprops={'fontsize':15,'color':'black'})
plt.title("上海数据分析岗位薪资分布情况")
plt.show()


# 上面是上海的统计结果，其中薪资在25k的占比与北京基本一样，但是15k的岗位比北京要多，35k薪资的岗位比北京少，薪资水平依然保持在15k和25k左右的水平

# 最后是深圳

# In[280]:


jobs_shenzhen = jobs_data[jobs_data.address == '深圳']
jobs_shenzhen.index = np.arange(len(jobs_shenzhen))


# In[281]:


jobs_shenzhen_salary = {}

for i in range(len(jobs_shenzhen)):
    #最低薪资
    low_salary = int(jobs_shenzhen['salary'][i].split('-')[0][:len(jobs_shenzhen['salary'][i].split('-')[0])-1])
    #最高薪资
    high_salary = int(jobs_shenzhen['salary'][i].split('-')[1][:len(jobs_shenzhen['salary'][i].split('-')[1])-1])
    #10k以内
    if (low_salary + high_salary)//2 < 10:
        jobs_shenzhen_salary['10k以内'] = jobs_shenzhen_salary.get('10k以内',0) + 1
    #15k
    elif (low_salary + high_salary)//2 < 16:
        jobs_shenzhen_salary['15k左右'] = jobs_shenzhen_salary.get('15k左右',0) + 1
    #25k
    elif (low_salary + high_salary)//2 < 26:
        jobs_shenzhen_salary['25k左右'] = jobs_shenzhen_salary.get('25k左右',0) + 1
    #35k
    elif (low_salary + high_salary)//2 < 36:
        jobs_shenzhen_salary['35k左右'] = jobs_shenzhen_salary.get('35k左右',0) + 1
    #40以上
    else:
        jobs_shenzhen_salary['40k以上'] = jobs_shenzhen_salary.get('40k以上',0) + 1


# In[285]:


fig = plt.figure(figsize=(9,9))
labels = list(jobs_shenzhen_salary.keys())
nums = list(jobs_shenzhen_salary.values())
explode = (0,0,0,0,0)
plt.pie(nums,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150,textprops={'fontsize':15,'color':'black'})
plt.title("深圳数据分析岗位薪资分布情况")
plt.show()


# 上面是深圳的薪资分布情况，可以看到25k这个薪资水平比北京和上海都要低一点，而15k水平的比北京、上海都要多，在40k以上的职位是非常少的

# 以上三座城市在数据分析岗位的薪资水平的分布是差不多的，所以一线城市基本的薪资水平都在15k和25k左右的状态

# 下面统计一下数据分析岗位主要分布在哪些类型的公司中

# In[287]:


jobs_data['industry']


# In[293]:


#切分数据
for i in range(len(jobs_data)):
    jobs_data['industry'][i] = jobs_data['industry'][i].split("/")[0]


# In[297]:


jobs_industry = {}

#统计不同公司类型出现的次数
for i in range(len(jobs_data)):
    industry = jobs_data['industry'][i]
    jobs_industry[industry] = jobs_industry.get(industry,0) + 1


# In[298]:


jobs_industry


# In[300]:


#排序
jobs_industry = sorted(jobs_industry.items(),key=lambda jobs_industry:jobs_industry[1],reverse=False)


# In[302]:


industry_number = []
industry_names = []

for i in range(len(jobs_industry)):
    industry_number.append(jobs_industry[i][1])
    industry_names.append(jobs_industry[i][0])


# In[309]:


fig = plt.figure(figsize=(15,15))
plt.barh(industry_names,industry_number,height=0.9,color='steelblue',alpha=0.8)
plt.yticks(industry_names)
plt.xlim(0,80)
plt.xlabel("数量")
plt.title("统计哪些类型的公司在招收数据分析工程师")
for x, y in enumerate(industry_number):
    plt.text(y + 0.2, x - 0.1, '%s' % y)
plt.show()


# 上面就是统计结果，总结一下top10的公司：
# #1、金融
# #2、移动互联网
# #3、文娱
# #4、移动互联网金融
# #5、消费生活
# #6、电商
# #7、教育
# #8、数据服务
# #9、游戏
# #10、企业服务

# 下面统计学历的分布情况

# In[331]:


#分割处理
for i in range(len(jobs_data)):
    jobs_data['education'][i] = jobs_data['infomation'][i].split('/')[1]


# In[333]:


educations = {}

#统计不同学历出现的次数
for i in range(len(jobs_data)):
    education = jobs_data['education'][i]
    educations[education] = educations.get(education,0) + 1


# In[336]:


educations


# In[338]:


fig = plt.figure(figsize=(9,9))
labels = list(educations.keys())
nums = list(educations.values())
explode = (0,0,0,0)
plt.pie(nums,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150,textprops={'fontsize':15,'color':'black'})
plt.title("全国数据分析岗位对于学历的要求分布情况")
plt.show()


# 本科的比重是最大的，占了85%，其他的学历都很少

# 而像北京这样的一线城市，肯定是符合这种分布的，因为一线城市的数据占了大部分

# 下面是最后一个任务，找出数据分析岗位的任职要求都有哪些硬性的要求

# In[6]:


#去除description中含有缺失值的项
new_jobs_data = jobs_data[jobs_data['description'].notnull()]
new_jobs_data.index = np.arange(len(new_jobs_data))


# In[9]:


new_jobs_data['description'].head()


# 最后一个任务算是最难的，因为从上面的数据就可以看出来，数据是很混乱的，有中文、英文、数字和一些标点符号，所以必须合理的筛选才可以

# 还有一点，内容中有很多中文，而中文不像英文那样用空格分隔单词，中文都是连贯起来的，所以需要先对其进行分词处理，而我使用的是Pkuseg，这是北大的开源分词工具，是目前分词准确率最高的工具，分词结束后才可以进行后续的处理

# In[550]:


#导入分词工具和正则化工具
import pkuseg
import re


# In[567]:


texts = []

#筛选出所有符合要求的字段
for i in range(len(new_jobs_data)):
    if '岗位要求' in new_jobs_data['description'][i]:
        text = new_jobs_data['description'][i].split('岗位要求')[1]
        texts.append(text)
    elif '任职要求' in new_jobs_data['description'][i]:
        text = new_jobs_data['description'][i].split("任职要求")[1]
        texts.append(text)
    elif '任职资格' in new_jobs_data['description'][i]:
        text = new_jobs_data['description'][i].split('任职资格')[1]
        texts.append(text)
    elif '职位要求' in new_jobs_data['description'][i]:
        text = new_jobs_data['description'][i].split("职位要求")[1]
        texts.append(text)
    elif '基本要求' in new_jobs_data['description'][i]:
        text = new_jobs_data['description'][i].split('基本要求')[1]
        texts.append(text)
    elif '工作要求' in new_jobs_data['description'][i]:
        text = new_jobs_data['description'][i].split("工作要求")[1]
        texts.append(text)
    elif '任职条件' in new_jobs_data['description'][i]:
        text = new_jobs_data['description'][i].split("任职条件")[1]
        texts.append(text)
    elif '岗位职责' in new_jobs_data['description'][i]:
        text = new_jobs_data['description'][i].split("岗位职责")[1]
        texts.append(text)
    elif '岗位需求' in new_jobs_data['description'][i]:
        text = new_jobs_data['description'][i].split("岗位需求")[1]
        texts.append(text)
    elif new_jobs_data['description'][i].count('1') == 2:
        text = new_jobs_data['description'][i].split("1")[2]
        texts.append(text)
    else:
        texts.append(new_jobs_data['description'][i])


# 下面定义正则表达式函数，用于筛选数据

# In[568]:


#过滤出中文
def find_chinese(text):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', text)
    return chinese

#过滤出英文
def find_unchinese(text):
    pattern = re.compile(r'[\u4e00-\u9fa5\0-9\.\。\:\：\；\[\]\【\】\《\》\（\）\！]')
    unchinese = re.sub(pattern,"",text)
    return unchinese


# 下面先处理数据中的英文部分

# In[569]:


unchinese_texts = []

#筛选出所有的英文字符
for i in range(len(texts)):
    unchinese_texts.append(find_unchinese(texts[i]))


# In[570]:


#将字符串用逗号分隔开
for i in range(len(unchinese_texts)):
    mes = unchinese_texts[i].split('，')
    unchinese_texts[i] = mes


# 用上面的方法处理完以后会生成很多没用的逗号和顿号，还需要清洗一下

# In[571]:


#清洗掉逗号和顿号
for i in range(len(unchinese_texts)):
    for j in range(len(unchinese_texts[i])):
        pattern = re.compile(r'[\，\、\,]')
        unchinese = re.sub(pattern,"",unchinese_texts[i][j])
        unchinese_texts[i][j] = str.lower(unchinese)


# In[572]:


requirement = {}

#统计每个要求出现的次数
for i in range(len(unchinese_texts)):
    for r in unchinese_texts[i]:
        requirement[r] = requirement.get(r,0) + 1


# In[573]:


#升序排序
requirement = sorted(requirement.items(),key=lambda requirement:requirement[1],reverse=True)


# In[586]:


result = {}

#常用的技能项列表
skills = ['Python','SQL','R','Excel','PPT','Office','Hive','Tableau','Hadoop','SPSS',
          'Java','Matlab','Spark','Nosql','Scala','PHP','Oracle','Mysql','Shell']

#机器学习算法列表
mls = ['svm','kmeans','lr','knn','xgboost','gbdt','xgb']

#对所有的技能项进行统计
for i in range(len(u)):
    for skill in skills:
        if str.lower(skill) in u[i][0]:
            result[skill] = result.get(skill,0) + 1
    for ml in mls:
        if ml in u[i][0]:
            result['Machine Learning'] = result.get('Machine Learning',0) + 1


# In[587]:


#降序排序
requirement = sorted(result.items(),key=lambda result:result[1],reverse=False)


# In[588]:


requirement_number = []
requirement_name = []

for i in range(len(requirement)):
    requirement_number.append(requirement[i][1])
    requirement_name.append(requirement[i][0])


# In[589]:


matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(9,9))
plt.barh(requirement_name,requirement_number,height=0.8,color='steelblue',alpha=0.8)
plt.yticks(requirement_name)
plt.xlim(0,210)
plt.xlabel("数量")
plt.title("不同技能项出现的次数")
for x, y in enumerate(requirement_number):
    plt.text(y + 0.2, x - 0.1, '%s' % y)
plt.show()


# 从上面的结果可以看出，R语言出现的次数最多，有193次，而第二名是SQL这样的结构化查询语言，也是非常重要的技能，第三名是Python，Python是一个处理数据非常方便的工具

# 有一点需要注意，一般有些技能项是只要掌握其一就可以，比如对于R、Python、SPSS这三个来说，掌握其中一个就可以。所以真正需要的技能可以总结为以下几点：
# #第一：掌握像R、Python这样的数据处理、同时兼顾数据可视化能力的工具
# #第二：Excel，有些公司是不需要编程语言那样的数据处理方式的，所以更需要会Excel
# #第三：Hive、Spark、Hadoop，这三项技能属于大数据方向，是用来存储和处理大数据的平台
# #第四：Machine Learning：机器学习算法，很多机器学习算法是可以帮助处理和转换数据的，而对于数据分析师来说，掌握这样的技能也是必不可少的
# #第五：PPT等Office办公工具，编辑文档时是需要的
# 

# 下面处理中文

# In[800]:


chinese_text = []

#筛选出中文
for i in range(len(texts)):
    chinese_text.append(find_chinese(texts[i]))


# In[801]:


#定义一些常见的词组
lexicon = ['数据分析工具','数据敏感','数据可视化','概率基础','基本数据方法','逻辑思维','数据分析']

#对中文进行分词处理
seg = pkuseg.pkuseg(user_dict=lexicon)
messages = []
for i in range(len(chinese_text)):
    mes = seg.cut(chinese_text[i])
    messages.append(mes)


# In[802]:


#定义停用词列表，主要用来剔除掉无意义的词汇
stopwords = []
new_messages = []
    
with open('D://stopwords.txt',encoding='utf-8') as f:
    stopwords = f.read()

#去除停用词
for i in range(len(messages)):
    mes = []
    for w in messages[i]:
        if w not in stopwords:
            mes.append(w)
    mes = ' '.join(mes)
    new_messages.append(mes)


# In[803]:


#导入jieba模块提供的关键词提取功能
import jieba.analyse as analyse

#定义提取关键词函数，top=5
def analysis(data):
    return ' '.join(analyse.extract_tags(data,topK=5,withWeight=False,allowPOS=()))


# In[804]:


result_messages = []

#进行关键词提取
for i in range(len(new_messages)):
    mes = analysis(new_messages[i]).split(" ")
    result_messages.append(mes)


# In[805]:


results = {}

#对关键词进行统计
for i in range(len(result_messages)):
    for j in result_messages[i]:
        results[j] = result.get(j,0) + 1


# In[806]:


#降序排序
results = sorted(results.items(),key=lambda results:results[1],reverse=True)


# In[807]:


results


# 上面是最终的统计结果，可以看出，对于数据分析师的要求有以下几点是最重要的：
# #数据分析能力
# #逻辑思维能力
# #数据建模能力
# #数据挖掘能力
# #数据清洗能力
# #数据可视化能力
# #统计学知识
# #数据库知识
# #数学知识
# #责任感
# #洞察能力
# #沟通能力

# 以上就是我的整个分析过程，谢谢观看！
