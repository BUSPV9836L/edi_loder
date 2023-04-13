from neo4j import GraphDatabase


class EDISPLIT:

    def Edi_split(self, data, seg_delimeter):
        edi_split = data.split(seg_delimeter)
        seg_list = []
        for seg in edi_split:
            seg_list.append([seg])
        return seg_list

    def Isa_seg(self, isa_seg_data, ele_delimiter):
        isa_seg = isa_seg_data[0].split(ele_delimiter)
        # print(isa_seg)
        isa_01_value = isa_seg[0]
        isa_02_value = isa_seg[1]
        isa_03_value = isa_seg[2]
        isa_04_value = isa_seg[3]
        isa_05_value = isa_seg[4]
        isa_06_value = isa_seg[5]
        isa_07_value = isa_seg[6]
        isa_08_value = isa_seg[7]
        isa_09_value = isa_seg[8]
        isa_10_value = isa_seg[9]
        isa_11_value = isa_seg[10]
        isa_12_value = isa_seg[11]
        isa_13_value = isa_seg[12]
        isa_14_value = isa_seg[13]
        Head_segment = isa_seg
        graphdb = GraphDatabase.driver(
            uri="bolt://localhost:7687", auth=("neo4j", "Bipin@5637"))
        session = graphdb.session()
        q1 = f"CREATE (isa:ISA {{ isa_01 :'{isa_01_value}', isa_02 :'{isa_02_value}', isa_03 :'{isa_03_value}', isa_04 :'{isa_04_value}', isa_05 :'{isa_05_value}', isa_06 :'{isa_06_value}',isa_07 :'{isa_07_value}',isa_08 :'{isa_08_value}',isa_09 :'{isa_09_value}',isa_10 :'{isa_10_value}',isa_11 :'{isa_12_value}',isa_13 :'{isa_13_value}',isa_14 :'{isa_14_value}'}})"
        print(q1)
        session.run(q1)
