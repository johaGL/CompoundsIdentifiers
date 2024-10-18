# Uses the output of yufree script
# to generate the table 
# johaGL 2024

import os
import pandas as pd

DATE_XML_DOWNLOAD = "05-07-24"   # MM-DD-YY

print(f"The specified date of the HMDB xml file download is : " 
      f"{DATE_XML_DOWNLOAD}. If this is not corrrect, change "
      f"the script's DATE_XML_DOWNLOAD variable")
      
print("reading hmdb.csv file")

df = pd.read_csv("../extra/hmdb.csv", header=0, dtype=str)

print("selecting columns, filtering out rows with NA KEGG ids") 
df = df[["accession", "kegg"]]
df = df.dropna()
df = df.loc[df["kegg"] != "", :]
df = df.loc[df["kegg"] != "NA", :]
df.columns = ["HMDB","KEGG"]
print(df.head(2))

print("saving to file")
df.to_csv(f"../tables/HMDB-to-KEGG_{DATE_XML_DOWNLOAD}.tsv", sep='\t', index=False)
print("finished")
