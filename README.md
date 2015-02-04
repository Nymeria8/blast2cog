# Rap2cog

To simply annotate localy sequences based on the cog or kog databases, using as search for homologies the [RAPSEARCH2](http://omics.informatics.indiana.edu/mg/RAPSearch2/).
It outputs a tab separated file of Gene, Hit, Category, Subcategory, Description, Organism.

##Usage:


In the command line:
<pre><code>python rap2cog.py rapsearchoutput.m8 outputfile
</code></pre>


Notes:

+ The script is hard coded for the files of the KOG database. In that way, if you want to use the COG database, you shoud change the kog file name to whog. Also, the database files should be in the same directory of the script.

##Depends on:

The [COG](ftp://ftp.ncbi.nih.gov/pub/COG/COG/) or [KOG](ftp://ftp.ncbi.nih.gov/pub/COG/KOG/) databases, specificly the files fun.txt, pa and kog/whog, depending of the database used.

+ Rapseach2 .m8 file of your sequences against the sequences of the COG/KOG database

+ Python3



##License:

GPLv2
