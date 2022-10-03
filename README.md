## AWS Croc Captures to Data Lake

### 1 Intro

This repo provides working code notebooks that you can use to get a Data Lake operational in AWS using Croc Capture data.  You can execute code like the Delta Lake documentation with Scala Spark and PySpark on your local machine. It also provides Delta Lake function examples.

### 2 Learning More

To learn more about Data Lakes, head over to our webpage https://aidarwin.com.au for upcoming training courses.

Running Delta commands on your local machine and studying the files that are created is a great way to learn about how Delta Lake works.

### 3 Architecture Diagram

A diagram of the AWS environment is illustrated below relating AWS resources to equivalent Microsoft resources. 

Note you will need an AWS account for these labs with permissions to create resources.

### 4 Notebooks and Assets

This repo has the following key assets :

<dl>
  <dt>Source Data</dt>
  <dd>Croc Data Captures</dd>
  <dd>Croc Zones</dd>
  <dd>Croc Types</dd>
 
  <dt>Data Lake Setup</dt>
  <dd>Lab 1 - Setting up your AWS Environment</dd>
  <dd>Lab 2 - Setting up your storage and zones</dd>  
 
  <dt>Data Engineering</dt>
  <dd>Lab 3 - Uploading your source data to landing zone </dd>
  <dd>Lab 4 - Creating Landing to Bronze pipelines</dd>
  <dd>Lab 5 - Creating Bronze to Silver pipelines</dd>
  <dd>Lab 6 - Creating Silver to Gold pipelines</dd>  
  
  <dt>Data Analysis</dt>
  <dd>Lab 7 - Preparing with Power BI Desktop </dd>
  <dd>Lab 8 - Reading Data from S3 using Python Visual</dd>
 

### There are 8 Labs in total

 Lab 1 - Setting up your AWS Environment
 ----------------------------------------

For the purposes of the croc labs, AWS EMR will need to be setup for compute, with notebooks executed by AWS Glue and output to S3.
  
Requires more explanations step by step...
  

 Lab 2 - Setting up your storage and zones
----------------------------------------

AWS S3 bucket will consist of the following folder structure.
  
Requires more explanations step by step...

  
 Lab 3 - Uploading your source data to landing zone
---------------------------------------------------

For the purposes of the croc data, this will be manually updates in AWS using Upload tools.
  
Requires more explanations step by step...

 Lab 4 - Creating Landing to Bronze pipelines
---------------------------------------------------

The landing bronze pipeline does the following :
  a. Converts source files from csv into delta format
  b. Combine all 3 croc capture time period files in a single delta file
  
 Lab 5 - Creating Bronze to Silver pipelines
-------------------------------------------
  
The bronze to silver notebook does the following :
  a. Persists schema for files (declares data types)
  b. Transforms the data e.g. Transpose from columns to rows for Zones
  
See Notebooks folder for :
  x. 1 Notebook for croc captures
  y. 1 Notebook for zones
  z. 1 Notebook for crocs

 Lab 6 - Creating Silver to Gold pipelines
 ------------------------------------------
The silver to gold notebook does the following :

  a. Perform correlation and time series analysis to delta gold files demonstrating data science gold assets
  b. Aggregate the number of crocs by region by year demonstrating analytics gold assets

 See Notebooks folder for :  
  z. 1 Notebook

 Lab 7 - Analysis with Power BI
 ------------------------------------------
The Power BI Desktop tool will be required for Analysis :

  a. Download Power BI Desktop
  b. Configure Python IDE in Power BI options
  c. Download packages

 See Notebooks folder for :  
  z. 1 Notebook

 Lab 8 - Reading Data from S3 using Python Visual
-------------------------------------------------
Using the Python visual for Power BI, copy in the python code to read from Delta lake tables from Amazon's AWS S3 bucket.
  
  a. Set connection keys
  b. Paste python code
  c. Execute and analyse Delta Lake files with Python visual 
  d. Perform analysis with Pandas to show how to read data from csv files if you don't have an EMR Spark cluster

See Notebooks folder for :  
  y. 1 Notebook for Python analysis of Delta Lake files in S3
  z. 1 Notebook for Pandas analysis on CSV files in S3
  

 
### Maintenance

To improve query speed, Delta Lake supports the ability to optimise the layout of data in storage. There are various ways to optimize the layout outlined here.

## Compaction - Delta Lake can improve the speed of read queries from a table by coalescing small files into larger ones.

from delta.tables import *

deltaTable = DeltaTable.forPath(spark, pathToTable)  # For path-based tables
For Hive metastore-based tables: deltaTable = DeltaTable.forName(spark, tableName)

deltaTable.optimize().executeCompaction()

If you have a large amount of data and only want to optimize a subset of it, you can specify an optional partition predicate using `where`

  deltaTable.optimize().where("date='2021-11-18'").executeCompaction()

You can alternatively compact a table by repartitioning it to smaller number of files.

path = "..."
numFiles = 16

(spark.read
 .format("delta")
 .load(path)
 .repartition(numFiles)
 .write
 .option("dataChange", "false")
 .format("delta")
 .mode("overwrite")
 .save(path))


 
## Z Ordering 
A technical to co-locate related information in the same set of files. Z-Ordering aims to produce evenly-balanced data files with respect to the number of tuples, but not necessarily data size on disk

from delta.tables import *

deltaTable = DeltaTable.forPath(spark, pathToTable)  # path-based table
* For Hive metastore-based tables: deltaTable = DeltaTable.forName(spark, tableName)

deltaTable.optimize().executeZOrderBy("eventType")

* If you have a large amount of data and only want to optimize a subset of it, you can specify an optional partition predicate using `where`
deltaTable.optimize().where("date='2021-11-18'").executeZOrderBy("eventType")


## Multi-part Checkpointing 
By default, Delta Lake protocol writes checkpoint to a single file.   Increasing to multiple files allows parallelism which speeds up writing to the checkpoint.

Delta Lake protocol allows splitting the checkpoint into multiple Parquet files. This parallelizes and speeds up writing the checkpoint. In Delta Lake, by default each checkpoint is written as a single Parquet file. To to use this feature, set the SQL configuration spark.databricks.delta.checkpoint.partSize=<n>, where n is the limit of number of actions (such as AddFile) at which Delta Lake on Apache Spark will start parallelizing the checkpoint and attempt to write a maximum of this many actions per checkpoint file.

## Remove files no longer referenced by Delta Lake

from delta.tables import *

deltaTable = DeltaTable.forPath(spark, pathToTable)  # path-based tables, or
deltaTable = DeltaTable.forName(spark, tableName)    # Hive metastore-based tables

deltaTable.vacuum()        # vacuum files not required by versions older than the default retention period

deltaTable.vacuum(100)     # vacuum files not required by versions more than 100 hours old

## Disable Spark caching

Best practices does not recommend using Spark caching for the following reasons :

You lose any data skipping that can come from additional filters added on top of the cached DataFrame.

The data that gets cached may not be updated if the table is accessed using a different identifier (for example, you do spark.table(x).cache() but then write to the table using spark.write.save(/some/path).


