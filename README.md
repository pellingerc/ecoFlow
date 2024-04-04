# ecoFlow
Final Project for CSCI1951A: Data Science

Original Datasets:
https://www.kaggle.com/datasets/aditya2803/india-floods-inventory
https://www.kaggle.com/datasets/abhijitdahatonde/india-population-1947-2011
https://www.kaggle.com/datasets/saisaran2/rainfall-data-from-1901-to-2017-for-india

Our final dataset is compiled in data/final.csv.

# Data Spec

subdivision - this is a string that represents a region of India. There are a total of 23 unique regions in this dataset. This value will be used to compare population growth in different regions depending on the weather they experience. This is a required value to compare different regions but is not required to complete basic analysis. This does not reveal sensitive information.

YEAR - this is an integer that represents which year an entry pertains to. It ranges from 1951-2011 for each subdivision. Every year in between these values has an entry. This is a required value and will be used in analysis for comparing population over time. 

JAN - this is the rainfall for January. It ranges from 0.0 to 196.4. The default value is 0.0. These values are not unique as months may share the same rainfall. This value is required and will be used to analyze how heavy rainfall affects population movement. It does not reveal sensitive information. 

FEB - this is the rainfall for February. It ranges from 0.0 to 306.3. The default value is 0.0. These values are not unique as months may share the same rainfall. This value is required and will be used to analyze how heavy rainfall affects population movement. It does not reveal sensitive information. 

MAR - this is the rainfall for March. It ranges from 0.0 to 379.5. The default value is 0.0. These values are not unique as months may share the same rainfall. This value is required and will be used to analyze how heavy rainfall affects population movement. It does not reveal sensitive information. 

APR - this is the rainfall for April. It ranges from 0.0 to 560.2. The default value is 0.0. These values are not unique as months may share the same rainfall. This value is required and will be used to analyze how heavy rainfall affects population movement. It does not reveal sensitive information. 

MAY - this is the rainfall for May. It ranges from 0.0 to 898.7. The default value is 0.0. These values are not unique as months may share the same rainfall. This value is required and will be used to analyze how heavy rainfall affects population movement. It does not reveal sensitive information. 

There is also data for the rest of the months.

Jan-Feb - This is combined rainfall for January and February in a given year. It ranges from 0.0 to 468.3. This value is not required by may be used instead of individual months to identify heavy seasonal rainfall, that may not be evident by months individually. This does not include sensitive information. There is also similar columns for Mar-May, Jun-Sep, and Oct-Dec

Decade Population -  This is the population of a region during that decade. Due to how census data is collected this data is the same for each year in a decade. It is possible that we may interpolate data for each year depending on the starting and ending populations of a decade. It does not contain sensitive data. This will be used to analyze how population shifted over time in relation to rainfall and floods.

Flood Count - This is a count of the number of floods occurring in a specific region in a year. The range is 0 to 4 and the default value is 0. These values are not unique. This is a required value as it indicates that a significant flood occurred during a specific year in a region. It will be used to see if flooding decreases population growth in a region. 


# Full Data

Our full data deliverable can be viewed in data/final.csv. 

# Sample Data

A small sample of our data can be viewed in data/sample_data.csv. It is the data for only Andhra Pradesh and is 62 rows. 

# Tech Report
Data Points
We have a total of 1400 data points, split by region. There are 23 regions and each region has data for 61 years (except one region, Arunachal Pradesh, which only has data for 58 years). We believe that this is enough data to perform analysis on. 
Identifying attributes
The identifying attributes of the data are the region and year. Each region has one entry for each year. The rest of the columns of data are information about that region’s rainfall, population, and floods during that year.
Data source and collection
We collected the data from three datasets on Kaggle (linked at the top). According to the descriptions of each dataset, the rainfall data was sourced from data.gov.in, the population data is from census records, and the flood data does not have a clearly cited source, though it is noted as the “first ever dataset on India floods”. The government and census sources are reputable, but it would be ideal to have a clearer understanding of where the flood data came from. Unfortunately we were unable to find another dataset to use in its place.
We tried to use the complete datasets of our sources to compile our final dataset, however we had to cut down on the years included for each region since we only have population data from 1951-2011. For the sample in this deliverable, we decided to just include one region’s data. It represents about 1/23 of the complete dataset. It is a full representation of Andhra Pradesh, that region, but it does not represent the other regions. 

Data cleaning
To clean the data first regions across the datasets had to be standardized to be their lower for. The rainfall dataset then was filtered only for the years in which there is population data (1951-2011). The rainfall data was then filtered again for only regions that were in both the population and rainfall datasets. The columns in the population dataframe were then renamed to be only the year inorder to match the rainfall dataset. The corresponding region's population was then added to each year of the rainfall dataset. This joined the population and rainfall data. The year of each entry in the flood dataset then had to be extracted as dates were in various formats. Once this was done all entries which did not have any type of location data needed to be dropped. Finally the flood dataset was then iterated through to compile a list of floods in each region each year. This was then appended to the rainfall and population data to achieve the final dataset. Most of this cleaning occurred while datasets were loading in as pandas dataframes. 

Challenges/Observations
One challenge with the data we have is that we only have population data from every ten years so population changes have to be looked at at a larger scale than rainfall and flood changes, which we have new data for each year, and even month to month for rainfall. Another large challenge was how the flood data was originally collected and formatted. Over time it seemed that the format of collecting this data changed. This led to there being multiple columns describing where the flood took place, sometimes stating a state, region, or multiple regions. In addition the date format was also very different with some entries containing month and year, some having the exact date, and some having only year. Processing this data led to many entries having to be discarded. 
