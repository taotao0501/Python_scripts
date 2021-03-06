# 本脚本参考来自https://www.jianshu.com/p/ae3fe782d7c8，在此声明

# 1  RAP_ID →  MSU_ID

relation={}
for i in open("RAP-MSU_2018-03-29.txt"): #同目录下可找到该文件
    rap=str(i.split()[0])
    msu=str(i.split()[1])
    if msu!="None":
        relation[rap]=msu

for j in open("Os01g.txt"):
    id = j.strip()
    if id in relation.keys():
        if "," in relation[id]:
            s=relation[id].split(",")
            for a in s:
                print(id,a,sep="\t")
        else:
            print(id,relation[id],sep="\t")
    else:
        print(id,"None",sep="\t")
        
# 2 MUS_ID → RAP_ID

relation = {}
for i in open("RAP-MSU_2018-03-29.txt"):
    rap=str(i.split()[0])
    msu=str(i.split()[1])
    if msu!="None":
        if "," in msu:
            for a in msu.split(","):
                relation[a[0:-2]]=rap
        else:
            relation[msu[0:-2]]=rap
for j in open("MSU_IDtest.txt"):
    id=j.strip()
    if id[0:-2] in relation.keys():
        print(id,relation[id[0:-2]],sep="\t")
    else:
        print(id,"None",sep="\t")
       
# 3 RAP_ID 内部ID的转换  如 Os01g0102800 → Os01t0102800-01 并不是如此简单直接在后面加上-01，因为有些基因后面是-02，所以还是得找到一个ID匹配文档

relation={}
for i in open("RAP_Locus2ID.txt"):
    locus=str(i.split("\t")[0])
    id=str(i.split("\t")[1]).strip()
    relation[locus]=id
for j in open("Os01g.txt"):
    id = j.strip()
    if id in relation.keys():
       print(id,relation[id],sep="\t")
    else:
       print(id,"None",sep="\t")

# 4 再加一个 RAP_ID → Uniprot
relation={}
for i in open("Uniprot_id.txt"):
    locus=str(i.split()[0])
    id=str(i.split()[1])
    relation[locus]=id
for j in open("Os01g.txt"):
    id = j.strip()
    if id in relation.keys():
       print(id,relation[id],sep="\t")
    else:
       print(id,"None",sep="\t")

 
 # 这里有2个问题，就是 
#  1：locus=str(i.split("\t")[0]) 必须加"\t",因为不加就会出现“IndexError: list index out of range” 说索引越界了；
#  2：id=str(i.split("\t")[1].strip() 必须加strip()否则结果就是一行之后都有一个空行
#  关键的是并没有找到原因。
  
          
          
 
