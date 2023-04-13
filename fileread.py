import EDI_SPLIT
from neo4j import GraphDatabase
import os


object = EDI_SPLIT.EDISPLIT()

filepath = r'C:\Users\Bipin Kumar\Desktop\python_loader\xyz\edi.txt'
f = open(filepath, 'r')
edi_data = f.read()
isa_seg = edi_data[:106]
data = edi_data


def getDelimiter(data):
    return data[-1], data[3]


seg_delimeter, ele_delimeter = getDelimiter(isa_seg)
isa_seg = isa_seg.split(ele_delimeter)

object.Edi_split(data, seg_delimeter)

# edi_split = data.split(seg_delimeter)
# print(edi_split)
# gs_split = edi_split[1].split(ele_delimeter)
# # print("gs-splittt", gs_split)
# # isa_01_value = isa_seg[0]
# # isa_02_value = isa_seg[1]
# # isa_03_value = isa_seg[2]
# # isa_04_value = isa_seg[3]
# # isa_05_value = isa_seg[4]
# # isa_06_value = isa_seg[5]
# # isa_07_value = isa_seg[6]
# # isa_08_value = isa_seg[7]
# # isa_09_value = isa_seg[8]
# # isa_10_value = isa_seg[9]
# # isa_11_value = isa_seg[10]
# # isa_12_value = isa_seg[11]
# # isa_13_value = isa_seg[12]
# # isa_14_value = isa_seg[13]
# # Head_segment = isa_seg
# # graphdb = GraphDatabase.driver(
# #     uri="bolt://localhost:7687", auth=("neo4j", "Bipin@5637"))
# # session = graphdb.session()
# # q1 = f"CREATE (isa:ISA {{ isa_01 :'{isa_01_value}', isa_02 :'{isa_02_value}', isa_03 :'{isa_03_value}', isa_04 :'{isa_04_value}', isa_05 :'{isa_05_value}', isa_06 :'{isa_06_value}',isa_07 :'{isa_07_value}',isa_08 :'{isa_08_value}',isa_09 :'{isa_09_value}',isa_10 :'{isa_10_value}',isa_11 :'{isa_12_value}',isa_13 :'{isa_13_value}',isa_14 :'{isa_14_value}'}})"
# # print(q1)
# # session.run(q1)
