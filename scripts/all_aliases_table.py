import requests
import pandas as pd

"""
Using :
https://www.lipidmaps.org/resources/rest

see also:
https://www.lipidmaps.org/databases/lmsd/overview

Fatty Acyls [FA] 	
Glycerolipids [GL] 
Glycerophospholipids [GP] 	
Sphingolipids [SP] 
Sterol Lipids [ST] 
Prenol Lipids [PR] 	
Saccharolipids [SL] 	
Polyketides [PK] 
"""

########
# note : all columns are retrieved['regno', 'lm_id', 'name', 'sys_name', 'synonyms', 'abbrev', 'abbrev_chains', 'core', 'main_class', 'sub_class', 'class_level4', 'exactmass', 'formula', 'inchi', 'inchi_key', 'kegg_id', 'hmdb_id', 'chebi_id', 'lipidbank_id', 'pubchem_cid', 'smiles']
#  but only lm_id and kegg_id are of our interest
#######

DATE_XML_DOWNLOAD_HMDB = "05-07-24"  # MM-DD-YY

# start
print(f"The specified date of the HMDB xml file download is : "
      f"{DATE_XML_DOWNLOAD_HMDB}. If this is not corrrect, change "
      f"the script's DATE_XML_DOWNLOAD variable")
#
print("Parsing LipidMaps")
interesting_columns = ['name', 'lm_id', 'kegg_id', 'hmdb_id']
final_column_names = ['compoundName_LipidMaps','LipidMaps', 'KEGG', 'HMDB']
the_dfs_dict = {}
lipidmaps_groups = ["LMFA", "LMGL", "LMGP", "LMSP",
                    "LMST", "LMPR", "LMSL", "LMPK"]

"""
LipidMaps information:
Their stablished header contains 'regno', 'lm_id', 'name' ... and many other columns,
that are 20 in total
so allowing to form the following dict for each record:
{'regno': '11203', 'lm_id': 'LMST02010033', 'name': '2-Methoxyestrone', 
'sys_name': '2-methoxy,3-hydroxy-estra-1,3,5(10)-trien-17-one', 
'synonyms': '', 'abbrev': 'ST 19:4;O3', 'abbrev_chains': '', 
'core': 'Sterols [ST]', 'main_class': 'Steroids [ST02]', 
'sub_class': 'C18 steroids (estrogens) and derivatives [ST0201]', 
'class_level4': '', 'exactmass': '300.172545', 'formula': 'C19H24O3',
 'inchi': 'InChI=1S/C19H24O3/c1-19-8-7-12-13(15(19)5-6-18(19)21)4-3-11-9-16(20)17(22-2)10-14(11)12/h9-10,12-13,15,20H,3-8H2,1-2H3/t12-,13+,15-,19-/m0/s1', 
 'inchi_key': 'WHEUWNKSCXYKBU-QPWUGHHJSA-N', 'kegg_id': 'C05299', 'hmdb_id': 'HMDB0000010', 'chebi_id': '1189', 'lipidbank_id': '', 'pubchem_cid': '440624', 
 'smiles': '[C@]12([H])CC[C@]3(C)C(CC[C@@]3([H])[C@]1([H])CCC1C=C(C(OC)=CC2=1)O)=O'}
 
Few exceptions were detected, could handle them by popping out an extra-field
see further details in comments at the bottom. 
"""

for u in lipidmaps_groups:
    print(f"\nretrieving {u}")
    response = requests.get(
        f"https://www.lipidmaps.org/rest/compound/lm_id/{u}/all/download")
    txt = response.text
    lines = txt.split("\n")

    download_date_lipidmaps = lines[0].replace("/",
                                     "-")  #  the first line is a download_date
    expected_header_all_db_records = lines[1].split("\t")

    foo = {}

    counter = 0
    for l in lines[2:]:
        try:
            elems = l.split('\t')
            foo[counter] = {}
            for i_ele in range(len(elems)):
                foo[counter][expected_header_all_db_records[i_ele]] = elems[i_ele]
            # if verif needed, paste here chunk 1  (see comment at the bottom)
        except Exception as e:
            print(f"Error {e}, fields not matching for this record {l[:18]} ...")
            print("rescue: excluding extra-name field that interferes with adequate allocation to fields")
            try:
                elems = l.split('\t')
                elems.pop(4)  # verified extra-name field to pop out
                foo[counter] = {}
                for i_ele in range(len(elems)):
                    foo[counter][expected_header_all_db_records[i_ele]] = \
                    elems[i_ele]
                print("ok (rescue succeeded)")
                # if verif needed, paste here chunk 2 ((see comment at the bottom)
            except:
                print("sorry rescue was impossible, skipping this record")
                continue

        counter += 1

    df = pd.DataFrame.from_dict(foo).T
    df.columns = expected_header_all_db_records
    df = df[interesting_columns]
    the_dfs_dict[u] = df
# end for

dfs_list_to_concat = []
for k in the_dfs_dict.keys():
    dfs_list_to_concat.append(the_dfs_dict[k])

lipidmaps_df = pd.concat(dfs_list_to_concat,
                         axis=0)  #  TODO re-do with new pandas version to verify axis
lipidmaps_df.columns = final_column_names
print("ok lipidmaps.")

print("parsing HMDB")
print("reading hmdb.csv file")
df = pd.read_csv("../extra/hmdb.csv", header=0, dtype=str)
df = df[["name", "accession", "kegg"]]

df["name"] = df["name"].str.slice(start=2, stop=-1)
df.columns = ["compoundName_HMDB", "HMDB", "KEGG"]

df = pd.merge(df, lipidmaps_df, how="outer",
              left_on=["HMDB", "KEGG"], right_on=["HMDB", "KEGG"] )
print("ordering columns and saving to file")
df = df[['HMDB', 'KEGG', 'LipidMaps', 'compoundName_HMDB', 'compoundName_LipidMaps']]
df.to_csv(f"../tables/aliases-HMDB-{DATE_XML_DOWNLOAD_HMDB}-"
          f"LipidMaps-{download_date_lipidmaps}.tsv",
          sep='\t',
          index=False)
print("finished")

#### NOTE:
# Two records (LMFA07090159 and LMFA07010549) have 21 fields instead 20 (expected are 20)
# 0  |  38729
# 1  |  LMFA07010549
# 2  |  WE 14:0(6Me,10Me,13Me)/4:0(3Me)
# 3  |  6,10,13-Trimethyltetradecyl 3-methylbutanoate
# 4  |  WE(14:0(6Me,10Me,13Me)/4:0(3Me));
# 5  |  6,10,13-Trimethyltetradecyl 14-isovalerate
# 6  |  WE 22:0
# 7  |
# 8  |  Fatty Acyls [FA]
# 9  |  Fatty esters [FA07]
# 10  |  Wax monoesters [FA0701]
# 11  |
# 12  |  340.334131
# 13  |  C22H44O2
# 14  |  InChI=1S/C22H44O2/c1-18(2)14-15-21(6)13-10-12-20(5)11-8-7-9-16-24-22(23)17-19(3)4/h18-21H,7-17H2,1-6H3
# 15  |  APHRWGIGLRUJLA-UHFFFAOYSA-N
# 16  |
# 17  |
# 18  |  196299
# 19  |
# 20  |  545664
# 21  |  O=C(CC(C)C)OCCCCCC(C)CCCC(C)CCC(C)C
# The exception handles this situation. OK and verified.

### used chunks for verification
# 1
# try:
#     if foo[counter]['lm_id'] == "LMST02010033":
#         print(['\n'.join([u for u in l.split('\t')])])
#         for item, x in enumerate(l.split('\t')):
#             print(item, " | ", x)
#         print("============= ok =========================")
# except:
#     pass
# ...
# 2
# print("\n============= not ok =========================")
# for item, x in enumerate(l.split('\t')):
#     print(item, " | ", x)
# print("\n============= not ok =========================")