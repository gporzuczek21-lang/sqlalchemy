from main import engine, clean_measures, clean_station
from sqlalchemy import delete, update, select

if __name__ =="__main__":
   
   # C in CRUD
   ins_mea = clean_measures.insert()
   print(str(ins_mea))

   ins_sta = clean_station.insert()
   print(str(ins_sta))
   
   ins_mea = clean_measures.insert().values(station = 'USC00519397', data='1/21/2010', precip=0, tobs=69) 
   conn = engine.connect()
   result4 = conn.execute(ins_mea)
   
   # U in CURD 
   upd = clean_measures.update()
   print(str(upd))

   upd = (update(clean_measures).where(clean_measures.c.id == 16).values(tobs=1))
   result1 = conn.execute(upd)

   # R in CURD
   s = clean_measures.select()
   print(str(s))
   s = clean_measures.select().where(clean_measures.c.id > 7)
   result2 = conn.execute(s)
   for row in result2:
      print(row)

   ser = clean_measures.select()
   print(str(ser))
   ser = clean_measures.select()
   result3 = conn.execute(ser)
   for ro in result3:
      print(ro)
  
   # D in CURD   
   dele = clean_station.delete()
   print(dele)

   dele_15 = delete(clean_measures).where(clean_measures.c.id == 15)
   result = conn.execute(dele_15)
