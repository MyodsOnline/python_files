# import os
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.orm import mapper, sessionmaker
import datetime

class PCUS:
    """
    I will deal with that issue later.
    """
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def PCUS_on(self):
        print(f'{self.name} is on')

    def PCUS_off(self):
        print(f'{self.name} is off')


class ServerStorage:
    class AllObjects:
        def __init__(self, title):
            self.title = title
            self.created = datetime.datetime.now()
            self.id = None

    class AllUnits:
        def __init__(self, object_id, unit_title):
            self.object = object_id
            self.unit_title = unit_title
            self.id = None

    def __init__(self):
        self.database_engine = create_engine('sqlite:///db.db3', echo=False, pool_recycle=7200)
        self.metadata = MetaData()
        
