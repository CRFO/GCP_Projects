## Project: Data Modeling with Postgres

# Summary

The project builds an ETL pipeline for the music streaming app Sparkify using Python and SQL transferring data from 2 folders (log_data and song_data) that have JSON files localed in two local directories into 5 tables using a Postgres database: *songplays, users, songs, artists and time* located at GCP Cloud SQL with Postgres instance: my-sql-instance (trim-mix-266820 project).

# Files Structure

- *data/* folder contains log_data and song_data files in JSON format.
- *sql_queries.py* defines the SQL queries to create, drop and insert into tables.
- *create_tables.py* creates the Sparkify DB and executes creation and deletion of all tables.
- *etl.py* reads and processes the song and log JSON files and inserts them into the Postgres DB.
- *etl.ipynb* and test.ipynb test execution of the Python scripts and SQL statements respectively.

# Star Schema (PostgreSQL relational database)

## Fact Table
- songplays - list of records from log data withy song plays: *songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent*

## Dimension Tables
- users - list of users: *user_id, first_name, last_name, gender, level*
- songs - list of songs: *song_id, title, artist_id, year, duration*
- artists - list of artists: *artist_id, name, location, latitude, longitude*
- time - timestamps of records in song plays:  start_time, hour, day, week, month, year, weekday

The above schema was created and records were inserted from data/log_data and data/song_data JSON files into the tables one by one.

## Scripts

1. Execute "python create_tables.py" - Creates all tables in Cloud SQL instance with Postgres
2. Run all cells in etl.ipynb - Inserts records from data/log_data and data/song_data stored locally.
3. Run all cells in test.ipynb - Confirms that creations and insertions were successful.

