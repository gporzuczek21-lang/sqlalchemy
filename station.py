
from main import clean_station, engine
if __name__=="__main__":
   ins_sta = clean_station.insert()
   print(str(ins_sta))

   ins_sta = clean_station.insert().values(station = 'USC00519397', latitude = 21.2716,longitude =-157.8168,elevation = 3, name ='WAIKIKI 717.2', contry ="US", state="HI")
   conn = engine.connect()
   result = conn.execute(ins_sta)
   conn.execute(ins_sta, [  
      {'id': 2, 'station':'USC00513117', 'latitude': 21.4234 , 'longitude': -157.8015, 'elevation': 14.6, 'name': 'KANEOHE 838.1', 'contry': "US", 'state': "HI"},
      {'id': 3, 'station':'USC00514830', 'latitude': 21.5213, 'longitude': -157.8374, 'elevation': 7, 'name': 'KUALOA RANCH HEADQUARTERS 886.9', 'contry': "US", 'state': "HI"},
      {'id': 4, 'station':'USC00517948', 'latitude': 21.3934, 'longitude': -157.9751, 'elevation': 11.9, 'name': 'PEARL CITY', 'contry': "US", 'state': "HI"},
      {'id': 5, 'station':'USC00518838', 'latitude': 21.4992, 'longitude': -158.0111, 'elevation': 306.6, 'name': 'UPPER WAHIAWA 874.3', 'contry': "US", 'state': "HI"},
      {'id': 6, 'station':'USC00519523', 'latitude': 21.33556, 'longitude': -157.71139, 'elevation': 19.5, 'name': 'WAIMANALO EXPERIMENTAL FARM', 'contry': "US", 'state': "HI"},
      {'id': 7, 'station':'USC00519281', 'latitude': 21.45167, 'longitude': -157.84889, 'elevation': 32.9, 'name': 'WAIHEE 837.5', 'contry': "US", 'state': "HI"},
      {'id': 8, 'station':'USC00511918', 'latitude': 21.3152, 'longitude': -157.9992, 'elevation': 0.9, 'name': 'HONOLULU OBSERVATORY 702.2', 'contry': "US", 'state': "HI"},
      {'id': 9, 'station':'USC00516128', 'latitude': 21.3331, 'longitude': -157.8025, 'elevation':152.4, 'name': 'MANOA LYON ARBO 785.2', 'contry': "US", 'state': "HI"}
    ])
