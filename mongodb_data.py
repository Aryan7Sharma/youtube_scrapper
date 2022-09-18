import json

import pymongo
import logging

logging.basicConfig(filename='loggers/mongodb.txt',level=logging.INFO,format='%(asctime)s -- %(filename)s -- %(message)s -- %(levelname)s')
logs = logging.getLogger()
def create_connection():
    try:
        client = pymongo.MongoClient("mongodb+srv://aryan:Elon2003@cluster0.obq5u.mongodb.net/?retryWrites=true&w=majority")
        logs.info("mongodb-connection %s", client)
        return client
    except Exception as e:
        logs.exception(e)

def upload_Videos_data(coll_name, data):
    try:
        clients = create_connection()
        logs.info("connected with momngodb %s", clients)

        database = clients['youtube_scrapper']
        coll = database[coll_name]
        coll.insert_one(data)
    except Exception as e:
        logs.exception(e)
    finally:
        clients.close()

def upload_Comments_section(coll_name, data):
    try:
        clients = create_connection()
        database = clients['youtube_scrapper']
        coll = database[coll_name]
        coll.insert_one(data)
    except Exception as e:
        logs.exception(e)
    finally:
        clients.close()

def drop_old_data(coll_name):
    try:
        client = create_connection()
        database = client['youtube_scrapper']
        coll = database['{}'.format(coll_name)]
        coll.drop()
        logs.info("old data deleted")
    except Exception as e:
        logs.exception(e)
    finally:
        client.close()

