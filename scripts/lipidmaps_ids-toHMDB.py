# johaGL 2024
import os
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

interesting_columns = ['lm_id', 'hmdb_id']
final_column_names = ['LipidMaps', 'HMDB']
the_dfs_dict = {}
lipidmaps_groups = ["LMFA", "LMGL", "LMGP", "LMSP",
                    "LMST", "LMPR", "LMSL", "LMPK"]

for u in lipidmaps_groups:
    print(f"\nretrieving {u}\n")
    response = requests.get(
        f"https://www.lipidmaps.org/rest/compound/lm_id/{u}/all/download")
    txt = response.text
    lines = txt.split("\n")

    download_date = lines[0].replace("/",
                                     "-")  #  the first line is a download_date
    print(download_date)
    expected_header_all_db_records = lines[1].split("\t")

    foo = {}

    counter = 0
    for l in lines[2:]:
        try:
            elems = l.split('\t')
            foo[counter] = {}
            for i_ele in range(len(elems)):
                foo[counter][expected_header_all_db_records[i_ele]] = elems[i_ele]
        except Exception as e:
            print(
                f"Error {e}, fields not matching for this record {l[:18]} ...")
            print(
                "rescue: excluding extra-name field that interferes with adequate allocation to fields")
            try:
                elems = l.split('\t')
                elems.pop(4)  # verified extra-name field to pop out
                foo[counter] = {}
                for i_ele in range(len(elems)):
                    foo[counter][expected_header_all_db_records[i_ele]] = \
                        elems[i_ele]
                # if verif needed, paste here chunk 2 ((see comment at the bottom)
            except:
                print("sorry rescue was impossible, skipping this record")
                continue
        counter += 1
    df = pd.DataFrame.from_dict(foo).T

    df.columns = expected_header_all_db_records
    df = df[interesting_columns]
    df = df.dropna()
    df = df.loc[df['hmdb_id'] != "", :]
    the_dfs_dict[u] = df
#  end for

dfs_list_to_concat = []
for k in the_dfs_dict.keys():
    dfs_list_to_concat.append(the_dfs_dict[k])

final_df = pd.concat(dfs_list_to_concat,
                     axis=0)  #  TODO re-do with new pandas version to verify axis
final_df.columns = final_column_names
final_df.to_csv(f"../tables/LipidMaps-to-HMDB_{download_date}.tsv", sep='\t',
                index=False)

########### end
# dudu = {0: {"cosa1": 33, "cosa2": 44},
#         1: {"cosa1": 70, "cosa2": 55}}

# print(pd.DataFrame.from_dict(dudu))

