from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# 统计每条序列dna的长度
# def readLength(file):
#     fastq = {}
#     count = 1
#     for line in open(file):
#         if count % 2 == 1:
#             readID = line.strip()
#             fastq[readID] = [] #把readID作为key
#         elif count % 2 == 0:
#             seq = line.strip()
#             fastq[readID] = len(seq) #seq作为与上面key对应的value
#         count += 1
#     # for key, value in fastq.items():
#     #     print('>{}\t{}'.format(key, value))
#
#     with open('XQ_test_length_stat.txt', 'w') as f:
#         for key, value in fastq.items():
#             print('%s\t%s' % (key, value), file = f)
#
# readLength('L_XQ-HBS.fna')



# 在R中对每条序列长度进行统计，直方图显示>=370 占66% （15085/22828），因此挑选 >=370的dna序列用于后续分析
# Python 挑选 指定长度的dna序列，不再使用R来挑选了！
#
# def readLength(file):
#     fastq = {}
#     count = 1
#     for line in open(file):
#         if count % 2 == 1:
#             readID = line.strip()
#             fastq[readID] = [] #把readID作为key
#         elif count % 2 == 0:
#             seq = line.strip()
#             fastq[readID] = seq #seq作为与上面key对应的value
#         count += 1
#     for key, value in fastq.items():
#         for line in open("XQ_test350.gtf"):
#             id = line.split()[0]
#             if id in key:
#                 with open('XQ_test_dna.fasta', 'a') as f:
#                         print('%s\n%s' % (id, value), file=f)
#
# readLength("L_XQ-HBS.fna")

# 将单个文件中的DNA序列转化为蛋白序列
# sbt = open("XQ_test_pep.fasta", "w")
# for fa in SeqIO.parse("XQ_test_dna.fasta", "fasta"):
#     dna = Seq.Seq(str(fa.seq), IUPAC.unambiguous_dna)
#     mrna = dna[1:].transcribe()
#     protein = mrna.translate()
#     sbt.write(str('>' + fa.id) + '\n' + str(protein) + '\n')

#对fasta文件中的ID包含的数字进行计数
sum = 0
for fa in SeqIO.parse("PZ_control_pep.fasta", "fasta"):
    num = float(str(fa.id).split(";")[1].split("=")[1])
    sum = sum + num
print(sum)


