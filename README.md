# CompoundsIdentifiers

This repository provides tables of metabolites identifiers. 

The `tables` folder is the main folder and contains the following tables:

* *`HMDB-to-KEGG_<date>.tsv`*: table with HMDB identifiers matching to KEGG identifiers.
* *`LipidMaps-to-KEGG_<date>.tsv`*: table with LipidMaps identifiers matching to KEGG identifiers.

------
A nice compound
<img width="150" src="https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid=572215&t=l"/>

-------

Further details on  how the tables were produced
---

Re-producing the tables is completely optional. 

Expected structure of this folder for re-producing the tables:
```.
├── extra
│   └── <empty>     <- here the file of hmdb database (see "Instructions for HMDB")
├── scripts
│   ├── hmdb.py
│   ├── hmdb_ids-tokegg.py
│   └── lipidmaps_ids-tokegg.py
└── tables
    └── <empty>
```

The scripts in `scripts`  folder produce the content of the `tables` folder:

* `hmdb_ids-tokegg.py`
* `lipidmaps_ids-tokegg.py`

The `extra` folder contains pre-downloaded data to use as in the case of the HMDB database. 

## Description of the scripts

* lipidmaps_ids-tokegg.py: searches with the API of LipidMaps database and directly generates the final table. It takes 1 minute.

* `hmdb_ids-tokegg.py` and `hmdb.py`: Detailed information, and/or if needing to re-run it, see the [Instructions for HMDB](#instructions-for-hmdb). Importantly *hmdb.py* is an identical copy of the fantastic script created by yufree (https://gist.github.com/yufree/f552d865096010445fc7b969e7e9d439) which is an xml parser suited for the hmdb dowloaded database; takes ~ 10 min to complete.


> [!CAUTION]
> to be solved:  how to be sure that compounds are only from human ?  is it desirable to include non-human in same table ? 


### Instructions for HMDB

If willing to re-run the scripts to produce the final HMDB table, before anything, the following is required:

1. go to  https://hmdb.ca/downloads
2. download "All Metabolites" dataset, it's a zip file
3. locate the zip file into the `extra/` folder
4. unzip the file, this will produce the `hmdb_metabolites.xml` file, of ~6.5GB (too heavy, so not included in this repository)
5. The two scripts must be executed in the following order:
   * **a)** Run `hmdb.py` and wait until completed (~10min); it outputs `extra/hmdb.csv`
   * **b)** Run `hmdb_ids-tokegg.py, it uses the output of a); it outputs `tables/hmdb_ids-tokegg.py`

*Note* : the generated table provided in this repository used the  `HMDB Version 5.0 Released on 2021-11-17` downloaded on 07-May-2024 .


## Help

Contact johaGL for any question

