# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class ImdbDataPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn=sqlite3.connect("imdb_data.db")
        self.curr=self.conn.cursor()
    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS movie_data """)
        self.curr.execute("""
            CREATE Table movie_data(
                    Title text,
                    releaseYear number,
                    desc1 text,
                    Meta_score number,
                    rating number,
                    vote text,
                    image text,
                    duration text,
                    rated text 
                    )""")
    def process_item(self, item, spider):
        self.Store_Data(item)
    def Store_Data(self,item):
        self.curr.execute("""
            INSERT INTO movie_data values(?,?,?,?,?,?,?,?,?)""",(
                item['Title'][0],
                item['releaseYear'][0],
                item['desc1'][0],
                item['Meta_score'][0],
                item['rating'][0],
                item['vote'][0],
                item['image'][0],
                item['duration'][0],
                item['rated'][0]
                ))
        self.conn.commit()    