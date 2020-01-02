# Edgar Analytics

## Content
1. [Overview](#overview) 
2. [Input Files](#input-files)
3. [Analysis](#analysis)
4. [Output File](#output-file)

## Overview

The Securities and Exchange Commission's Electronic Data Gathering, Analysis and Retrieval (EDGAR) system is used to 
retrieve financial documents. The SEC maintains EDGAR weblogs showing which IP addresses have accessed which documents for
what company, and the time and date of those events. Although the SEC usually makes the EDGAR weblogs publicly available 
after six month, we make the assumption that there is streaming data available without any delay.

The purpose of this project is to build a pipeline to ingest that stream of data and calculate how long a particular user spends on EDGAR 
during a visit and how many documents that user requests during the session.

## Assumptions

For this project, we made some assumptions to simplify the task.
1. Using only the publicly available EDGAR weblogs
2. Each line in the weblog file represents a single web request for an EDGAR doc
3. The amount of time that elapses between document requests should be used to determine when a visit beings and ends.
4. A single user session is defined to have started when the IP address first requests a document from the EDGAR system
and continues as long as the same user continues to make requests. 
5. Assume data is being streamed into the program in the same order that it appears in the file.
6. The combination of `cik`, `accession` and `extention` fields uniquely identifies a single web page document request. 



## Input Files

There are two input files:
1. `log.csv`: EDGAR weblog
2. `inactivity_period.txt`: Identify when a user session is over.

Error handling:
1. Input file name is not accurate
2. Input file field is not in the right format
3. No permission to the file
4. 


## Analysis

## Output File
The output file contains for each user visit the duration of the visit and the number of documents requested during that visit.

`sessionization.txt`: lists the IP address, duration of the session and number of documents accesssed on each line.
In total five columns and no header. 

`IP_Address` : IP address of the user
`First_dt`: Date and time of the first webpage request in the session (yyyy-mm-dd hh:mm:ss)
`Last_dt`: Date and time of the last webpage request in the session (yyyy-mm-dd hh:mm:ss)
`Session_Duration`: duration of the session in seconds
`Request_Count`: count of webpage requests during the session
 