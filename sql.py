import logging
import mysql.connector

logging.basicConfig(filename='loggers/sql.txt',level=logging.DEBUG,format='%(asctime)s -- %(filename)s -- %(message)s -- %(levelname)s')
local_logger = logging.getLogger()
def create_sql_tables(user, host_name, password, database_name):
    try:
        mydb = mysql.connector.connect(user=user, host=host_name, password=password, database=database_name)
        local_logger.info("mysql_database_connection -- ")
    except Exception as e:
        local_logger.error(e)

    try:
        cursor = mydb.cursor()
        table1 = "CREATE TABLE IF NOT EXISTS youtubers_data (channel_name varchar(100), subscribers varchar(12), no_of_videos int, PRIMARY KEY (`channel_name`));"
        table2 = "CREATE TABLE IF NOT EXISTS videos_data (videos_id varchar(15), channel_name varchar(100), views int, likes varchar(10), comments_counts varchar(10), age_rest varchar(3), videos_url varchar(100),PRIMARY KEY (`videos_id`),FOREIGN KEY (`channel_name`) REFERENCES `youtubers_data`(`channel_name`));"
        table3 = "CREATE TABLE IF NOT EXISTS comments_data (`videos_id` varchar(15), `commenter_name` varchar(50), FOREIGN KEY (`videos_id`) REFERENCES `videos_data`(`videos_id`));"
        cursor.execute(table1)
        local_logger.info("youtubers_data table created successfully")
        cursor.execute(table2)
        local_logger.info("videos_data table created successfully")
        cursor.execute(table3)
        local_logger.info("comments_data table created successfully")
    except Exception as e:
        local_logger.error(e)
    finally:
        mydb.close()
create_sql_tables('root', 'localhost', 'Elon2003', 'test_1')

