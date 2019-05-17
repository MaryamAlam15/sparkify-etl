## Summary
 A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new
 music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. 
 Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity 
 on the app, as well as a directory with JSON metadata on the songs in their app.

#### So, to revolve this issue:
In this project, 
   - data modeling is implemented with Postgres.
   - an ETL pipeline is built using Python which will transform data from JSON files to dimension and fact tables using "star" schema.

### Dimension Tables:
   - users
   - songs
   - artists
   - time
   
### Fact Table:
   - songplays
   
### ETL Pipeline:
   - transfers data from two local directories (data/song_data, data/log_data) into the tables using SQL and Python.
   
### How to run:
   - run command to install requirements.
        > pip install -r requirements.txt
        
   - run ``create_tables.py`` to create database and tables.
   - run ``etl.py`` to execute the pipeline to read data from data files and transfer to respective tables.