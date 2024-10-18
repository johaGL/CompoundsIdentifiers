# CompoundsIdentifiers

This repository provides tables of metabolites identifiers. 

The `tables` folder is the main folder and contains the following tables:

* *`HMDB-to-KEGG_<date>.tsv`*: table with HMDB identifiers matching to KEGG identifiers.
* *`LipidMaps-to-KEGG_<date>.tsv*: table with LipidMaps identifiers matching to KEGG identifiers.

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
│   ├── hmdb_generator.py
│   └── lipidmaps_generator.py
└── tables
    └── <empty>
```

The scripts in `scripts`  folder produce the content of the `tables` folder:

* hmdb_generator.py: HMDB_ids.tsv
* lipidmaps_matcher.py: Lipidmaps_ids.tsv (it has identifiers only)

The `extra` folder contains pre-downloaded data to use as in the case of the HMDB database. 

> [!CAUTION]
> to be solved:  how to be sure that compounds are only from human ?  is it desirable to include non-human in same table ? 

## Description of the scripts

* hmdb_generator.py: it is an identical copy of the script *hmdb.py* created by yufree (https://gist.github.com/yufree/f552d865096010445fc7b969e7e9d439) which is an xml parser suited for the hmdb dowloaded database. See the [Instructions for HMDB](#instructions-for-hmdb) section and follow steps there before using the script. 
 . It takes ~ 10 min to complete

* lipidmaps_generator.py: searches with the API of LIPIDMAPS database. It takes 1 minute.

### Instructions for HMDB

If willing to re-run its corresponding script, before anything, the following is required:

1. go to  https://hmdb.ca/downloads
2. download "All Metabolites" dataset, it's a zip file
3. locate the zip file into the `extra` folder
4. unzip the file, this will produce the `hmdb_metabolites.xml` file, of ~6.5GB (too heavy, so not included in this repository)
5. The script can be now executed, it will use `extra/hmdb_metabolites.xml` automatically as input 

*Note* : the generated table provided in this repository used the  `HMDB Version 5.0 Released on 2021-11-17` downloaded on 07-May-2024 .


## Help

Contact johaGL for any question

