# Summary
This project creates the below mentioned tables in sparkify database in postgres and loads the data from the below mentioned directory inside the project folder 

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

# Sparkify DB

Sparkify DB is created using a star schema and optimized for song play analysis queries and the DB contains the following fact and dimension tables

#### FACT TABLES 
    songplays - Tracks all the song playback for different users capturing the start time of the playback.

#### DIMENSION TABLES
    users - Users table constains all users information along with their subscription level (Free/Paid)
    songs - Songs table contains song information and the corresponding artist id's
    artist - artist table contains all the artist information 
    time - time table gives information about the actual playback time of the songs with specific units captured 

#### Schema Design and ETL Pipeline 
Sparkify DB is designed using a star schema with the above mentioned fact and dimension tables particularly to easily analyze the song playback data. Data is modeled in such a way that it fits 3N form and all the song, artist, users and time are part of dimension tables and that fact tables have appropriate id's from those dimension tables to avoid redundant information getting stored in the fact table.

ETL process loads the data from the logs to users, time and songplays table and when populating data to users tables and whenever there is a conflict on user id it updates the user level information so that the user updated subscription status is captured in the table.

Songplays ETL load from the log data confirms that the song and artist information is not available in the dimension tables. It seems the data is missing in the dimension tables and that issue needs to be fixed.

#### Sample Data Screen Shots
Songplays Table Sample Data
![ Songplays Table Sample Data](https://github.com/reachgopi/DEN.DataModeling.postgres/blob/develop/images/artists.png)

Users Table Sample Data
![User Table Sample Data](https://github.com/reachgopi/DEN.DataModeling.postgres/blob/develop/images/users.png)

Songs Table Sample Data
![Songs Table Sample Data](https://github.com/reachgopi/DEN.DataModeling.postgres/blob/develop/images/songs.png)

Artists Table Sample Data
![Artists Table Sample Data](https://github.com/reachgopi/DEN.DataModeling.postgres/blob/develop/images/artists.png)

Time Table Sample Data
![Time Table Sample Data](https://github.com/reachgopi/DEN.DataModeling.postgres/blob/develop/images/time.png)

#### ETL Report for given DataSet
    songplays - 6820 Records Loaded
    users - 96 Records Loaded
    songs - 71 Records Loaded
    artists - 69 Records Loaded
    time - 6813 Records Loaded 

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