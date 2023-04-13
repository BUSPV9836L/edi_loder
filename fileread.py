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

edi_list = object.Edi_split(data, seg_delimeter)

object.Isa_seg(edi_list[0], ele_delimeter)
