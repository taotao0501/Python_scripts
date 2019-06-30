# 很久之前的脚本
# id_dict = {}
# outfile = open('id.txt', 'a')
# for i in open("convert.txt"):
#     gbid = str(i.strip().split()[0])
#     symbol = str(i.strip().split()[1])
#     id_dict[gbid] = symbol
#     # outfile.write(gbid + '\t' + symbol + '\n')
# outfile2 = open('id2.txt', 'a')
# for line in open("geneMatrix.txt"):
#     j = line.strip()
#     if 'geneNames' not in j:
#         rna_id = j.strip().split()[0]
#         if j in id_dict.keys():
#             print(j + '\t' + id_dict[j] + '\n')
#             outfile2.write(j + '\t' + id_dict[j] + '\n')

# 6-25 对fasta文件进行匹配，同时用到了python 正则 re.search(r'(>.*);', line).group(1)
# import re
# seq = ''
# out_file = open("LPS_speical_pepID.gtf", 'w')
# for line in open("only_LPS.gtf"):
#     if line.startswith(">Cluster") and seq == '':
#         header = line.rstrip()
#     elif line[0] == "0":
#         sbt = re.search(r'(>.*);', line).group(1)
#         seq += sbt + '\t'
#     elif line.startswith(">Cluster") and seq != '':
#         out_file.write(header + '\t' + seq + '\n')
#         seq = ''
#         header = line.rstrip()
#
# out_file.write(header + '\t' + seq + '\n')
# out_file.close()

# 6-25 匹配输出 tip:这里用到了readlines()一次读完所有文件，导致对内存消耗大
# f1 = open('LCPZ_pep.gtf','r')
# f2 = open('lcpz_common_pepID.gtf','r')
# f3 = open('lcpz_common_pepID.fasta','w')
# line1 = f1.readlines()
# line2 = f2.readlines()
# for a2 in line2:
#     for a1 in line1:
#         if a1.split('\t')[0] == a2.split('\t')[1].strip():
#             f3.write(a1.split('\t')[0] + '\n')
#             f3.write(a1.split('\t')[1].strip() + '\n')
# f1.close()
# f2.close()
# f3.close()

# 6-26 计算各个分类的总数
per = open('file5_c.txt')
sum1 = 0
sum0 = 0
sum2 = 0
sum3 = 0
sum4 = 0
for i in per:
    a = i.split('\t')[0]
    b = i.split('\t')[1]
    if a == "1":
        sum1 += int(b)
    elif a == "0":
        sum0 += int(b)
    elif a == "2":
        sum2 += int(b)
    elif a == "3":
        sum3 += int(b)
    elif a == "4":
        sum4 += int(b)
print(str(sum0) + ' ' + str(sum1) + ' ' + str(sum2) + ' ' + str(sum3) + ' ' + str(sum4))

# 6-27 night 对cdhit聚类结果文件 .clstr 进行如下操作：
# 1.选取实验组 只含有HBS的聚类结果
# 读入fasta格式文件
out1_file = open("xq87_HBS_clstr.gtf", "w")
seq = ''
for line in open('xq87_95_1_merged.fasta.clstr'):
    if line.startswith('>Cluster') and seq == '':
        id = line
    elif line[0] != '>':
         seq += line
    elif line.startswith('>Cluster') and seq != '':
        if "LPS" not in seq:
            out1_file.write(id + seq)
        id = line
        seq = ''


if "LPS" not in seq:
    out1_file.write(id + seq)
out1_file.close()

# 2. 对每一个cluster 统计所有成员的size数目的总和即DNA数，同时还选取了一个成员作为代表
# 读入fasta格式的文件
out1_file = open("xq87_HBS_count.gtf", "w")
count = 0
for line in open('xq87_HBS_clstr.gtf'):
    if line.startswith('>Cluster') and count == 0:
        id = line.strip()
    elif line[0] != '>':
         if line[0] == "0":
             seq = line.strip()
         count += int(line.split(";")[1].split("=")[1])

    elif line.startswith('>Cluster') and count != 0:
        out1_file.write(id + '\t' + str(count) + '\n' + seq + '\n')
        count = 0
        id = line.strip()
        seq = ''

out1_file.write(id + '\t' + str(count) + '\n' + seq + '\n')
out1_file.close()

# 3. 对每一个cluster 统计所有成员的size数目的总和即DNA总数，没有代表序列。
# 读入fasta文件
out1_file = open("xq87_HBS_count_only_Sum.gtf", "w")
count = 0
for line in open('xq87_HBS_clstr.gtf'):
    if line.startswith('>Cluster') and count == 0:
        id = line.strip()
    elif line[0] != '>':
         count += int(line.split(";")[1].split("=")[1])
    elif line.startswith('>Cluster') and count != 0:
        out1_file.write(id + '\t' + str(count) + '\n')
        count = 0
        id = line.strip()

out1_file.write(id + '\t' + str(count) + '\n')
out1_file.close()





















