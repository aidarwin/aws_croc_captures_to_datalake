# AWS Croc Captures to Data Lake

## Intro

This repo provides working code notebooks that you can use to get a Data Lake operational in AWS using Croc Capture data.  You can execute code like the Delta Lake documentation with Scala Spark and PySpark on your local machine. It also provides Delta Lake function examples.

Running Delta commands on your local machine and studying the files that are created is a great way to learn about how Delta Lake works.

## Notebooks

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

## Pandas

You can use pandas to do simple transformations if you don't have a Spark cluster. 

## Architecture Diagram

A diagram of the AWS environment is illustrated below relating AWS resources to equivalent Microsoft resources. 

## Learning More

To learn more about Data Lakes, head over to our webpage https://aidarwin.com.au for upcoming training courses.


