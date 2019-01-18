
# OpenStreetMap Data Wrangling, Lima (Perú) 
By [Adrián Vera Ros](https://www.linkedin.com/in/adrianveraros/) 

This project belongs to Udacity's [Data Analyst Nanodegree](https://eu.udacity.com/course/data-analyst-nanodegree--nd002). Below you'll find links to the rest of the Nanodegree projects. 

* [Intro to data analysis](https://github.com/AdrianVeraRos/Python-Medical-appointments-EDA)
* [Exploratory data analysis](https://github.com/AdrianVeraRos/R-White-wine-EDA)
* [Data wrangling](https://github.com/AdrianVeraRos/OpenStreetMap-Peru-Lima)
* [Machine learning](https://github.com/AdrianVeraRos/Enron-Fraud-Identification)
* [Data visualization](https://public.tableau.com/profile/adrian.vera.ros#!/vizhome/Flightdelaycausesfinal/Story1)

This project was developed in 2018 and it is no longer maintained. 

If you have trouble opening the python notebook file please follow this [link](https://nbviewer.jupyter.org/github/AdrianVeraRos/OpenStreetMap-Peru-Lima/blob/master/Lima.ipynb). 


## About
I lived most of my 2017 in Lima, and one of the first things that surprised me the most when I arrived was the laxitude of the people. I selected Lima for being a city I know and I'm fond of; but mostly because of the challenge that this laxitude could imply in a collaboratively created dataset like OpenStreetMap.

* Extracted on 2018 October 18th with Overpass-API from: https://overpass-api.de/api/map?bbox=-77.2693,-12.2784,-76.8996,-11.8577 

The size of the dowloaded file is 232MB.


## Project Outline
This project consists of three distinct parts:

### · Auditing
Dataset exploration to get to know more about the structure and set the rules to clean street names and phone numbers through regular expressions. 

### · Cleaning and creating a database
Based on the findings of our audit, we prepared some python code to clean and transform the original XML data into different .csv files to be dumped into a SQL database and analyzed using sqlite3. 

The cleaning and transformation process can be found in **cleaning.py** , **street_cleaner.py** and **phone_cleaner.py** . The schema for the csv files is found in **schema.py**. Finally, the code for creating the database is in **sql_db_creator.py**.

The file **sample_creator.py** was used to create a sample (sample.osm) to check that everything was running smoothly before cleaning the main dataset.    

### · Exploring the data
Database exploration through sqlite3 queries. Main focus on restaurant and place of worship tags. 