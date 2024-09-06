# CompoundsIdentifiers

This repository provides tables of metabolites identifiers. 

The `tables` folder is the main folder and contains the following tables:

* *KEGG-full.tsv*
* *HMDB-full.tsv*
* *Lipidmaps-to-kegg.tsv*

Detais of each one are given in next subsections

## KEGG-full.tsv
organism: human

## HMDB-full.tsv
organism: mostly human

## Lipidmaps-to-kegg.tsv
 organism: mostly human
 

> [!CAUTION]
> to be solved:  how to be sure that compounds are only from human ?  is it better to include non-human in same table ? 


<img src=https://commons.wikimedia.org/wiki/File:Orsellinaldehyde.png alt="chem_img" width="170"/>

-------

Further details on  how the tables were produced
---

Re-producing the tables is completely optional. 

Expected structure of this folder for re-producing the tables:
```.
├── extra
│   └── <empty>     <- here the file of hmdb database (see "Instructions for HMDB")
├── scripts
│   ├── kegg_generator.py 
│   ├── hmdb_generator.py
│   └── lipidmaps_matcher.py
└── tables
    └── <empty>
```

The scripts in `scripts`  folder produce the content of the `tables` folder:

* kegg_generator.py : KEGG-full.tsv
* hmdb_generator.py: HMDB-full.tsv
* lipidmaps_matcher.py: Lipidmaps-to-kegg.tsv (it has identifiers only)

The `extra` folder contains pre-downloaded data to use as in the case of the HMDB database. 

## Description of the scripts

* kegg_generator.py: uses the API REST, it takes XX hours to be completed. 

* hmdb_generator.py: it is an identical copy of the script *hmdb.py* created by yufree (https://gist.github.com/yufree/f552d865096010445fc7b969e7e9d439) which is an xml parser suited for the hmdb dowloaded database. See the instructions for the database download before using the script. 
 . It takes ~ 10 min to complete

* lipidmaps_generator.py: searches with the API of LIPIDMAPS database. It takes XX minutes ??? hours ???.

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

