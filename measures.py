from main import clean_measures, engine
if __name__=="__main__":
   ins_mea = clean_measures.insert()
   print(str(ins_mea))
   ins_mea = clean_measures.insert().values(station = 'USC00519397', data='1/1/2010', precip=0.08, tobs=65) 
   conn = engine.connect()
   result = conn.execute(ins_mea)

   conn.execute(ins_mea, [ 
      {'id':2, 'station':'USC00519397', 'data':'1/2/2010', 'precip':0, 'tobs':63},
      {'id':3, 'station':'USC00519397', 'data':'1/3/2010', 'precip':0, 'tobs':74},
      {'id':4, 'station':'USC00519397', 'data':'1/4/2010', 'precip':0, 'tobs':76},
      {'id':5, 'station':'USC00519397', 'data':'1/6/2010', 'precip':0, 'tobs':73},
      {'id':6, 'station':'USC00519397', 'data':'1/7/2010', 'precip':0.06, 'tobs':70},
      {'id':7, 'station':'USC00519397', 'data':'1/8/2010', 'precip':0, 'tobs':64},
      {'id':8, 'station':'USC00519397', 'data':'1/9/2010', 'precip':0, 'tobs':61},
      {'id':9, 'station':'USC00519397', 'data':'1/10/2010', 'precip':0, 'tobs':66},
      {'id':10, 'station':'USC00519397', 'data':'1/11/2010', 'precip':0.1, 'tobs':64},
      {'id':11, 'station':'USC00519397', 'data':'1/12/2010', 'precip':0, 'tobs':61},
      {'id':12, 'station':'USC00519397', 'data':'1/14/2010', 'precip':0, 'tobs':66},
      {'id':13, 'station':'USC00519397', 'data':'1/15/2010', 'precip':0, 'tobs':65},
      {'id':14, 'station':'USC00519397', 'data':'1/16/2010', 'precip':0, 'tobs':68},
      {'id':15, 'station':'USC00519397', 'data':'1/17/2010', 'precip':0, 'tobs':64},
      {'id':16, 'station':'USC00519397', 'data':'1/18/2010', 'precip':0, 'tobs':72},
      {'id':17, 'station':'USC00519397', 'data':'1/19/2010', 'precip':0, 'tobs':66},
      {'id':18, 'station':'USC00519397', 'data':'1/20/2010', 'precip':0, 'tobs':66}   
    ])
