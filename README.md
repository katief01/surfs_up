# Surfs Up Challenge (Module 9)

## Overview of the analysis: Explain the purpose of this analysis.
  The purpose of this Surfs Up analysis was to provide addition information about temperature trends in Oahu. Specifically, we provided temperature data for the months of June and December in Oahu, in order to determine if a surf and ice cream shop business is sustainable year-round.

## Results: 
* June temperature trends: We were able to review 1,700 June dates with corresponding temperatures from 2010 through 2017.  The results gave a nice picture of mild temperatures ranging from the coolest being 64 degrees and the hottest 85 degrees. The mean came out at a very pleasant 74 degrees.  
![image](https://user-images.githubusercontent.com/74223626/107865328-ce138680-6e2a-11eb-9792-69960d32ebd2.png)

* December temperature trends: Here we were able to review approximately 1,500 December dates with the correspondng temperature also from 2010 until the end of 2016.  The results were more varied with the coolest being 54 degrees and the hottest being 83 degrees.  The mean was still very pleasant at 71 degrees.

* Differences in time of year: Even though the coolest temperature in December is 10 degrees cooler than it is in June, the mean and quartile ranges are only a few degrees cooler in the winter.  

## Summary: 
  Using Python, Pandas functions and methods, and SQLAlchemy, we filtered the date column of the Measurements table in the hawaii.sqlite database in order to retrieve all temperatures for the months of June and December. We were able to then convert those temperatures to a list, create a DataFrame from the list, and generate the summary statistics. After reviewing the summary statistics, the results showed a definite probability of being able to sustain a surf and ice cream shop business year round based on mild temperatures. In order to vet this decision further I would suggest additional queries to find average rainfall data and hurricane or other storm data, if available.
