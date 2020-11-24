# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = (" CREATE TABLE IF NOT EXISTS songplays " \
                         " ( " \
                         "      songplay_id SERIAL , " \
                         "      start_time timestamp NOT NULL," \
                         "      user_id int NOT NULL, " \
                         "      level varchar(10), " \
                         "      song_id varchar(30)," \
                         "      artist_id varchar(30),"\
                         "      session_id int, "\
                         "      location varchar(250)," \
                         "      user_agent varchar(250)," \
                         "      PRIMARY KEY(songplay_id) "
                         " ) ")


user_table_create = (" CREATE TABLE IF NOT EXISTS users " \
                     " ( " \
                     "      user_id int, " \
                     "      first_name varchar(100) NOT NULL, " \
                     "      last_name varchar(100) NOT NULL, " \
                     "      gender varchar(10) NOT NULL, " \
                     "      level varchar(10) NOT NULL," \
                     "      PRIMARY KEY(user_id)" \
                     " )" )

song_table_create = (" CREATE TABLE IF NOT EXISTS songs " \
                     " ( " \
                     "      song_id varchar(30), " \
                     "      title varchar(100) NOT NULL, " \
                     "      artist_id varchar(30) NOT NULL, " \
                     "      year int , " \
                     "      duration int NOT NULL, " \
                     "      PRIMARY KEY(song_id) " \
                     " )" )

artist_table_create = (" CREATE TABLE IF NOT EXISTS artists " \
                     " ( " \
                     "      artist_id varchar(30), " \
                     "      name varchar(100) NOT NULL, " \
                     "      location varchar(100), " \
                     "      latitude int, " \
                     "      longitude int, " \
                     "      PRIMARY KEY(artist_id)" \
                     " )" )

time_table_create = (" CREATE TABLE IF NOT EXISTS time " \
                     " ( " \
                     "      start_time timestamp, " \
                     "      hour int, " \
                     "      day int, " \
                     "      week int, " \
                     "      month int, " \
                     "      year int, " \
                     "      weekday int, " \
                     "      PRIMARY KEY(start_time) " \
                     " )" )


# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent ) values (%s,%s,%s,%s,%s,%s,%s,%s)")

user_table_insert = ("INSERT INTO users (user_id, first_name, last_name, gender, level) values (%s, %s, %s, %s, %s) ON CONFLICT(user_id) DO NOTHING ")

song_table_insert = ("INSERT INTO songs (song_id, title, artist_id, year, duration) values (%s, %s, %s, %s, %s) ON CONFLICT(song_id) DO NOTHING")

artist_table_insert = ("INSERT INTO artists (artist_id, name, location, latitude, longitude) values (%s, %s, %s, %s, %s) ON CONFLICT(artist_id) DO NOTHING")

time_table_insert = ("INSERT INTO time (start_time, hour, day, week, month, year, weekday) values (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT(start_time) DO NOTHING")

# FIND SONGS

song_select = ("SELECT s.song_id, s.artist_id from ( songs s join artists a on s.artist_id = a.artist_id) where s.title = %s and a.name = %s and s.duration = %s" )

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]