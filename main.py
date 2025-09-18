from sqlalchemy import Table, Column, Integer,ForeignKey, Float, Text, String, MetaData
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database02.db')

meta = MetaData()

clean_station = Table(
   'clean_station', meta,
   Column('id', Integer, primary_key=True),
   Column('station', String),
   Column('latitude', Float),
   Column('longitude', Float),
   Column('elevation', Integer),
   Column('name', Text),
   Column('contry', String),
   Column('state', String),
)

clean_measures = Table(
    'clean_measures', meta,
   Column('id', Integer, primary_key=True),
   Column("station", String, ForeignKey("clean_station.station")),
   Column('data', String),
   Column('precip', Float),
   Column('tobs', Integer),
)
if __name__ == "__main__":
   meta.create_all(engine)
   print(engine.table_names())
