## AWS Croc Captures to Data Lake

### 1 Intro

This repo provides working code notebooks that you can use to get a Data Lake operational in AWS using Croc Capture data.  You can execute code like the Delta Lake documentation with Scala Spark and PySpark on your local machine. It also provides Delta Lake function examples.

Running Delta commands on your local machine and studying the files that are created is a great way to learn about how Delta Lake works.

### 2 Notebooks

This repo has the following key components :

<dl>
  <dt>Source Data</dt>
  <dd>Croc Data Captures</dd>
  <dd>Croc Zones</dd>
  <dd>Croc Types</dd>
  <dd>Date Table</dd>
  <dt>Data Lake Setup</dt>
  <dd>Lab 1 - Setting up your AWS Environment</dd>
  <dd>Lab 2 - Setting up your storage and zones</dd>  
  <dt>Data Engineering</dt>
  <dd>Lab 3 - Uploading your source data to landing zone </dd>
  <dd>Lab 4 - Creating Landing to Bronze pipelines</dd>
  
  1 Notebook for all (pass in source and target file as parameters)
  
  The landing bronze pipeline does the following :
  Saves the file into delta format
  Does insert and update (3 croc files for each time period where we will insert three times)
  
  <dd>Lab 5 - Creating Bronze to Silver pipelines</dd>
  
  1 Notebook for all captures
  1 Notebook for zones
  1 Notebook for crocs
  1 Notebook for date
  
  The bronze to silver notebook does the following :
  Persists schema for files (declares data types)
  Transforms the data e.g. Transpose.
  
  <dd>Lab 6 - Creating Silver to Gold pipelines</dd>
  
  1 Notebook
  
  The silver to gold notebook does the following :
  Aggregates data for easy analysis e.g. number of captures group by year
  
</dl>

### Pandas

You can use pandas to do simple transformations if you don't have a Spark cluster. 

### Power BI

You can use pandas to do simple transformations if you don't have a Spark cluster. 

### Architecture Diagram

A diagram of the AWS environment is illustrated below relating AWS resources to equivalent Microsoft resources. 

## Learning More

To learn more about Data Lakes, head over to our webpage https://aidarwin.com.au for upcoming training courses.

## Maintenance

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


