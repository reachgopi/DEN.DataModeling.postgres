# Summary
This project creates the below mentioned tables in postgres and loads the data from the following directory inside the project folder 

    Tables
        1. songs
        2. artists
        3. users
        4. time
        5. songplays
    
    Data Directory
        1. data/log_data
        2. data/song_data

Data from logs directory are loaded into users, time and songplays table where as data from the songs folder are loaded into the songs and artists table.

# Project Files

Project contains the following files 

create_tables.py -  Script which is used to create the sparkify db and the mentioned tables into the databse

etl.py - Script which is used to load the data from the data directory to all the tables in Sparkify DB.

etl.ipynb -  Notebook file to run the code and visualize outputs 

test.ipynb - Test notebook to test if everything is working as expected.



# How to Run Scripts

#### Create Table
Use the following command to create the above mentioned tables in postgres 
    
    python3 create_tables.py

#### Load Data
Use the following command to load the data from Data Directory in to the mentioned tables

    python3 etl.py