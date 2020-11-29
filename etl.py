import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import datetime as dt


def process_song_file(cur, filepath):
    '''
    Process the files from song_data directory and loads the data into songs and artists table.
    '''
    # open song file
    df = pd.read_json(filepath, typ='series')

    # insert song record
    song_data = [df["song_id"],df["title"],df["artist_id"],df["year"], df["duration"]]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = [df["artist_id"],df["artist_name"],df["artist_location"],df["artist_latitude"], df["artist_longitude"]]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    '''
        Process the log files from the log_data directory and loads the data into the users, 
        time and songplays table. 
        While loading the data into songplays table it fetches the artist_id and song_id 
        from the songs and artists table based on artist name, song name and duration.
    '''
    # open log file
    counter = 0
    print(pd.__version__)
    df = pd.read_json(filepath,lines=True)

    # filter by NextSong action
    filter_condition = df['page'] == 'NextSong'
    df_updated = df[filter_condition]

    # convert timestamp column to datetime
    df_updated_datetime = pd.to_datetime(df_updated['ts'], unit='ms')
    
    # insert time data records
    time_df = pd.DataFrame({
                 'start_time': df_updated_datetime,
                 'hour': df_updated_datetime.dt.hour,
                 'day': df_updated_datetime.dt.day,
                 'week': df_updated_datetime.dt.weekofyear, 
                 'month': df_updated_datetime.dt.month_name(),
                 'year': df_updated_datetime.dt.year, 
                 'weekday': df_updated_datetime.dt.day_name()})

    

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df_updated[["userId","firstName","lastName","gender","level"]]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df_updated.iterrows():
        
        # get songid and artistid from song and artist tables
        results = cur.execute(song_select, (row.song, row.artist, row.length))
        songid, artistid = results if results else None, None

        # insert songplay record
        val = dt.datetime.fromtimestamp(row['ts']//1000)

        userId = -1
        if row['userId'] == '' :
            counter += 1
            userId = -1
        else:
            userId = row['userId']

        songplay_data = [ val , userId, row['level'], songid, artistid, row['sessionId'],row['location'], row['userAgent']]
        
        cur.execute(songplay_table_insert, songplay_data)
    
    print("Data set contains {} empty user records".format(counter))


def process_data(cur, conn, filepath, func):
    '''
    Reads all the json files from the log and song data directory and loads the data into the tables
    '''
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()