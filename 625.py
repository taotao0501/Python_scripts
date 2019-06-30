# 6-24 对clsuster的结果进行统计，获取100%一致cluster的和各自不一致的cluster
#1.1 提取common
# out0_file = open("lcpz_common.gtf", "w")
# out1_file = open("lcpz_only_LPS.gtf", "w")
# out2_file = open("lcpz_only_HBS.gtf", "w")
# seq = ''
# for line in open('lcpz_cdhit.fa.clstr'):
#     if line.startswith('>Cluster') and seq == '':
#         id = line
#     elif line[0] != '>':
#         seq = seq + line
#     elif line.startswith('>Cluster') and seq != '':
#         if "100.00%" not in seq:
#             if "LPS" in seq:
#                 out1_file.write(id + seq)
#             elif "HBS" in seq:
#                 out2_file.write(id + seq)
#         else:
#             out0_file.write(id + seq)
#         seq = ''
#         id = line
#
# if "100%" not in seq:
#     if "LPS" in seq:
#         out1_file.write(id + seq)
#     elif "HBS" in seq:
#         out2_file.write(id + seq)
# else:
#     out0_file.write(id + seq)
#
# out1_file.close()
# out2_file.close()
# out0_file.close()

# 提取size数据
# import re
# seq = ''
# out_file = open("lcpz_only_LPS_pepID.gtf", 'w')
# for line in open("lcpz_only_LPS.gtf"):
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

#利用biopython中的SeqIO.parse模块来对fasta格式文件进行读取和操作
from Bio import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
# import re
# X = open("LCPZ_pep.gtf", 'w')
# for fa in SeqIO.parse("lcpz_all.fasta", "fasta"):
#     sss = re.search(r'(.*);(.*);', fa.id).group(1)
#     head = str('>' + sss)
#     X.write(head + '\t' + str(fa.seq) + '\n')


# sum = 0
# for fa in SeqIO.parse("5.gtf", "fasta"):
#     num = float(str(fa.id).split(";")[1].split("=")[1])
#     sum = sum + num
# print(sum)
# xq87 = open("xq87.fasta", 'w')
# for fa in SeqIO.parse("xq_remove_stop.fasta", "fasta"):
#     seq = str(fa.seq)[87:]
#     head = str('>' + fa.id)
#     xq87.write(head + '\n' + seq + '\n')

#序列分为5类 存储为5个文件
file0 = open("0.gtf", 'w')
file1 = open("1.gtf", 'w')
file2 = open("2.gtf", 'w')
file3 = open("3.gtf", 'w')
file4 = open("4.gtf", 'w')
file5 = open("5.gtf", 'w')
file4_c = []
file5_c = []

for fa in SeqIO.parse("XQ_control_pep.fasta", "fasta"):
    head = str('>' + str(fa.id))
    seq = str(fa.seq)
    if "*" not in seq:
        file0.write(head + '\n' + seq + '\n')
        if seq[25] == "C" and seq[86] == "C":
            if seq[32] == "C":
                file4.write(head + '\n' + seq + '\n')
                string = seq[88:104]
                num = string.count("C")
                rep = str(fa.id).split(";")[1].split("=")[1]
                file4_c.append(str(num) + '\t' + rep)
            else:
                file5.write(head + '\n' + seq + '\n')
                sbt = seq[88:104]
                sbt_num = sbt.count("C")
                rep2 = str(fa.id).split(";")[1].split("=")[1]
                file5_c.append(str(sbt_num) + '\t' + rep2)
        elif seq[25] == "C" and seq[86] != "C":
            file1.write(head + '\n' + seq + '\n')
        elif seq[25] != "C" and seq[87] == "C":
            file2.write(head + '\n' + seq + '\n')
        else:
            file3.write(head + '\n' + seq + '\n')

out4 = []
out5 = []
for value in file4_c:
    out4.append(value + "\n")
open('file4_c.txt', 'w').writelines(out4)

for value in file5_c:
    out5.append(value + "\n")
open('file5_c.txt', 'w').writelines(out5)

# 带着DNA重复数进行统计
# sum = 0
# for fa in SeqIO.parse("0.gtf", "fasta"):
#     num = float(str(fa.id).split(";")[1].split("=")[1])
#     sum = sum + num
# print(sum)


