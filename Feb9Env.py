import paho.mqtt.client as mqtt
import json
import datetime
import pymysql
import pymysql.cursors
from time import sleep
from datetime import datetime, timezone
import threading
import gc
global kursor,con
kursor=0x7f1175640130
con=0x7f1175640130
def mysql_db():
    global kursor,con
    con = pymysql.connect(
                host = 'main.cue7elc3bjnz.ap-south-1.rds.amazonaws.com',
                user = 'env',
                password = 'Shunyaekai@2022',
                db = 'Env',
                connect_timeout=1800,
                cursorclass=pymysql.cursors.SSCursor,
                )
    print(con)
    kursor = con.cursor()
    kursor.execute("SET SESSION MAX_EXECUTION_TIME=1000")
def D_read():
    while 1:
        try:
            print("DB Working new")
            a="SELECT count_moist FROM devicetable" 
            kursor.execute(a)
            garData=kursor.fetchall()
            print(garData)
            sleep(3000)
        except Exception as e:
            sleep(5)
            print(e)
class env_mqtt():
    def __init__(self):
        self.user_Id=""
        self.Temp=""
        self.Humi=""
        self.Mois=""
        self.Fire_db=0
        self.IncomData=""
        self.AlertTemp=""
        self.AlertHumi=""
        self.AlertMoist=""
        self.AlertTypeTemp=0
        self.AlertTypeHumi=0
        self.AlertTypeMoist=0
        self.DevcId=""
        self.temp=0.0
        self.humi=""
        self.moist=""
        self.Fire=0
        self.DvcName=""
        self.update_Time=""
        self.maxTemp=0
        self.minTemp=0
        self.maxHumi=0
        self.minHumi=0
        self.maxMoist=0
        self.minMoist=0
    def on_connect(self, client, userdata, flags, rc):
        #print("connected with result code "+str(rc))
        client.subscribe("/Env_data")
        mysql_db()
        threading.Thread(target=D_read).start()
    def on_message(self,client, userdata, msg):
        global kursor,con
        data=msg.payload
        data=data.decode()
        print(data)
        try:
            now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
            print(now)
            # tme=str(now)
            # tme=tme[:len(tme)-4]
            # tme=(tme[:len(tme)-4])
            # print('Type:', type(now))
            self.IncomData=data
            self.IncomData=self.IncomData
            mainData=self.IncomData.split(",")
            # print(mainData)
            self.DevcId=mainData[0]
            self.temp=mainData[1]
            print(self.temp)
            self.humi=mainData[2]
            self.moist=mainData[3]
            self.Fire=mainData[4]
            print(self.DevcId,self.temp,self.humi,self.moist,self.Fire)
            Db_data= "SELECT userid,devicename,temperature, humidity,moisture,fire,alerttemp,alerthumi,alertmoisture,alerttypetemp,alerttypehumi,alerttypemoisture,maxtemprange,mintemprange,maxhumirange,minhumirange,maxmoistrange,minmoistrange FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
            kursor.execute(Db_data)
            rows=kursor.fetchall()
            Db_store_data=rows[0]
            # print(Db_store_data)
            self.user_Id=Db_store_data[0]
            self.DvcName=Db_store_data[1]
            self.Temp=Db_store_data[2]
            self.Humi=Db_store_data[3]
            self.Mois=Db_store_data[4]
            self.Fire_db=Db_store_data[5]
            self.AlertTemp=Db_store_data[6]
            self.AlertHumi=Db_store_data[7]
            self.AlertMoist=Db_store_data[8]
            self.AlertTypeTemp=Db_store_data[9]
            self.AlertTypeHumi=Db_store_data[10]
            self.AlertTypeMoist=Db_store_data[11]
            self.maxTemp=Db_store_data[12]
            self.minTemp=Db_store_data[13]
            self.maxHumi=Db_store_data[14]
            self.minHumi=Db_store_data[15]
            self.maxMoist=Db_store_data[16]
            self.minMoist=Db_store_data[17]
            # print(user_Id,Temp,Humi,Mois,Fire,AlertTemp,AlertHumi,AlertMoist,AlertTypeTemp,AlertTypeHumi,AlertTypeMoist)
            if self.AlertTypeTemp == 1:
                print("Alert_temp_above")
                threading.Thread(target=self.checkAlertTemp_entry_histTable_above()).start()
            elif self.AlertTypeTemp==0:
                print("Alert_temp_below")
                threading.Thread(target=self.checkAlertTemp_entry_histTable_below()).start()
            elif self.AlertTypeTemp==2:
                threading.Thread(target=self.rangeTempAlert()).start()   
            if self.AlertTypeHumi==1:
                print("Alert_humi_above")
                threading.Thread(target=self.checkAlertHumidity_entry_histTable_above()).start()
            elif self.AlertTypeHumi==0:
                print("Alert_humi_below")
                threading.Thread(target=self.checkAlertHumidity_entry_histTable_below()).start()
            elif self.AlertTypeHumi==2:
                threading.Thread(target=self.rangeHumiAlert()).start()  
            if self.AlertTypeMoist==1:
                print("Alert_moist_above")
                threading.Thread(self.checkAlertMoisture_entry_histTable_above()).start()
            elif self.AlertTypeMoist==0:
                print("Alert_moist_below")
                threading.Thread(self.checkAlertMoisture_entry_histTable_below()).start()
            elif self.AlertTypeMoist==2:
                threading.Thread(target=self.rangeMoistAlert()).start() 
            if int(self.Fire_db)!=int(self.Fire):
                print("Atert_Fire")
                sql = f"INSERT INTO history_table(userid, deviceid, devicename ,temperature ,humidity , moisture, fire) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}')"
                kursor.execute(sql)
                con.commit()
            print("update")
            print(self.temp,)
            if "nan" in str(self.temp):
                # threading.Thread(target=connect()).start()
                sql = "UPDATE Env.devicetable SET  moisture = '{}', fire='{}', notify_fire='{}', updt_time='{}' WHERE deviceid = '{}'".format(self.moist,self.Fire,self.Fire,now,self.DevcId)
                kursor.execute(sql)
                con.commit()
            else:
                # threading.Thread(target=connect()).start()
                sql = "UPDATE Env.devicetable SET temperature = '{}', humidity = '{}', moisture = '{}', fire='{}', notify_fire='{}',updt_time='{}'  WHERE deviceid = '{}'".format(self.temp,self.humi,self.moist,self.Fire,self.Fire,now,self.DevcId)
                kursor.execute(sql)
                con.commit()
        except Exception as e:
            print(e)
    def checkAlertTemp_entry_histTable_above(self):
        print(self.temp, self.AlertTemp)
        try:
            if float(self.temp)>=float(self.AlertTemp):
                # threading.Thread(target=connect()).start()
                Hist_db_data= "SELECT count_temp FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==0:
                    print("temp_above")
                    self.AlertTemp=1
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertTemp) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertTemp}')"
                    kursor.execute(sql)
                    con.commit()
                    self.AlertTemp=0
                    print(kursor.rowcount)
                    sql = "UPDATE Env.devicetable SET count_temp=1,notify_temp=1 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
            else:
                # threading.Thread(target=connect()).start()
                Hist_db_data= "SELECT count_temp FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==1:
                    print("normal_temp_above")
                    self.AlertTemp=0
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertTemp) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertTemp}')"
                    kursor.execute(sql)
                    con.commit()
                    sql = "UPDATE Env.devicetable SET count_temp=0,notify_temp=0 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
        except Exception as e:
            print(e)
    def checkAlertTemp_entry_histTable_below(self):
        try:
            if float(self.temp)<=float(self.AlertTemp):
                # threading.Thread(target=connect()).start()
                Hist_db_data= "SELECT count_temp FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==0:
                    print("Temp_below")
                    self.AlertTemp=1
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertTemp) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertTemp}')"
                    kursor.execute(sql)
                    con.commit()
                    self.AlertTemp=0
                    print(kursor.rowcount)
                    sql = "UPDATE Env.devicetable SET count_temp=1,notify_temp=1 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
            else:
                # threading.Thread(target=connect()).start()
                Hist_db_data= "SELECT count_temp FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==1:
                    print("normal_temp_below")
                    self.AlertTemp=0
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertTemp) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertTemp}')"
                    kursor.execute(sql)
                    con.commit()
                    sql = "UPDATE Env.devicetable SET count_temp=0,notify_temp=0 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
        except Exception as e:
            print(e)
    def checkAlertHumidity_entry_histTable_above(self):
        print(self.humi,self.AlertHumi)
        try:
            # threading.Thread(target=connect()).start()
            if float(self.humi)>=float(self.AlertHumi):
                Hist_db_data= "SELECT count_humi FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                # print(Alert)
                if Alert==0:
                    print("humi_above")
                    self.AlertHumi=1
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertHumi) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertHumi}')"
                    kursor.execute(sql)
                    con.commit()
                    self.AlertHumi=0
                    print(kursor.rowcount)
                    sql = "UPDATE Env.devicetable SET count_humi=1,notify_humi=1 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
            else:
                # threading.Thread(target=connect()).start()
                print("hel")
                Hist_db_data= "SELECT count_humi FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==1:
                    print("normal_humi_above")
                    self.AlertHumi=0
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertHumi) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertHumi}')"
                    kursor.execute(sql)
                    con.commit()
                    sql = "UPDATE Env.devicetable SET count_humi=0,notify_humi=0 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
        except Exception as e:
            print(e)
    def checkAlertHumidity_entry_histTable_below(self):
        try:
            if float(self.humi)<=float(self.AlertHumi):
                # threading.Thread(target=connect()).start()
                Hist_db_data= "SELECT count_humi FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==0:
                    print("humi_below")
                    self.AlertHumi=1
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertHumi) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertHumi}')"
                    kursor.execute(sql)
                    con.commit()
                    self.AlertHumi=0
                    print(kursor.rowcount)
                    sql = "UPDATE Env.devicetable SET count_humi=1,notify_humi=1 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
            else:
                # threading.Thread(target=connect()).start()
                Hist_db_data= "SELECT count_humi FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==1:
                    print("normal_humi_below")
                    self.AlertHumi=0
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertHumi) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertHumi}')"
                    kursor.execute(sql)
                    con.commit()
                    sql = "UPDATE Env.devicetable SET count_humi=0,notify_humi=0 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
        except Exception as e:
            print(e)
    def checkAlertMoisture_entry_histTable_above(self):
        print(self.moist,self.AlertMoist)
        try:
            if int(self.moist)>=int(self.AlertMoist):
                # threading.Thread(target=connect()).start()
                Hist_db_data= "SELECT count_moist FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==0:
                    print("moist_above")
                    self.AlertMoist=1
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertMoist) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertMoist}')"
                    kursor.execute(sql)
                    con.commit()
                    self.AlertMoist=0
                    print(kursor.rowcount)
                    sql = "UPDATE Env.devicetable SET count_moist=1,notify_moist=1 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
            else:
                # threading.Thread(target=connect()).start()
                Hist_db_data= "SELECT count_moist FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==1:
                    print("normal_moist_above")
                    self.AlertMoist=0
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertMoist) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertMoist}')"
                    kursor.execute(sql)
                    con.commit()
                    sql = "UPDATE Env.devicetable SET count_moist=0,notify_moist=0 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
        except Exception as e:
            print(e)
    def checkAlertMoisture_entry_histTable_below(self):
        print(self.moist,self.AlertMoist)
        try:
            if int(self.moist)<=int(self.AlertMoist):
                # threading.Thread(target=connect()).start()
                Hist_db_data= "SELECT count_moist FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==0:
                    print("moist_below")
                    self.AlertMoist=1
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertMoist) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertMoist}')"
                    kursor.execute(sql)
                    con.commit()
                    self.AlertMoist=0
                    print(kursor.rowcount)
                    sql = "UPDATE Env.devicetable SET count_moist=1,notify_moist=1 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
            else: # if int(self.temp)>=int(self.minTemp) and int(self.temp)<=int(self.maxTemp):
                #     print("alert temp normal")
                # elif int(self.temp)>=int(self.maxTemp):
                #     print("Alert_temp_rangeAbove")
                #     # threading.Thread(target=self.checkAlertTemp_entry_histTable_above()).start()
                # elif int(self.temp)<=int(self.minTemp):
                #     print("Alert_temp_rangebelow")
                # threading.Thread(target=connect()).start()
                Hist_db_data= "SELECT count_moist FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==1:
                    print("normal_Moist_below")
                    self.AlertMoist=0
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertMoist) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertMoist}')"
                    kursor.execute(sql)
                    con.commit()
                    sql = "UPDATE Env.devicetable SET count_moist=0,notify_moist=0 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql) # if int(self.temp)>=int(self.minTemp) and int(self.temp)<=int(self.maxTemp):
                #     print("alert temp normal")
                # elif int(self.temp)>=int(self.maxTemp):
                #     print("Alert_temp_rangeAbove")
                #     # threading.Thread(target=self.checkAlertTemp_entry_histTable_above()).start()
                # elif int(self.temp)<=int(self.minTemp):
                #     print("Alert_temp_rangebelow")
                    con.commit()
        except Exception as e:
            print(e)
    def rangeTempAlert(self):
        try:
            if int(self.temp)>=int(self.minTemp) and int(self.temp)<=int(self.maxTemp):
                print("alert temp normal")
                Hist_db_data= "SELECT count_temp FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==1:
                    print("normal_temp_below")
                    self.AlertTemp=0
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertTemp) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertTemp}')"
                    kursor.execute(sql)
                    con.commit()
                    sql = "UPDATE Env.devicetable SET count_temp=0,notify_temp=0 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
            elif int(self.temp)>=int(self.maxTemp):
                print("Alert_temp_rangeAbove")
                Hist_db_data= "SELECT count_temp FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==0:
                    print("temp_max")
                    self.AlertTemp=1
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertTemp) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertTemp}')"
                    kursor.execute(sql)
                    con.commit()
                    self.AlertTemp=0
                    print(kursor.rowcount)
                    sql = "UPDATE Env.devicetable SET count_temp=1,notify_temp=1 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
            elif int(self.temp)<=int(self.minTemp):
                print("Alert_temp_rangebelow")
                Hist_db_data= "SELECT count_temp FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==0:
                    print("Temp_min")
                    self.AlertTemp=1
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertTemp) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertTemp}')"
                    kursor.execute(sql)
                    con.commit()
                    self.AlertTemp=0
                    print(kursor.rowcount)
                    sql = "UPDATE Env.devicetable SET count_temp=1,notify_temp=1 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
        except Exception as e:
            print(e)
    def rangeHumiAlert(self):
        try:
            if int(self.humi)>=int(self.minHumi) and int(self.humi)<=int(self.maxHumi):
                print("alert humi normal")
                Hist_db_data= "SELECT count_humi FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==1:
                    print("normal_humi_below")
                    self.AlertHumi=0
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertHumi) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertHumi}')"
                    kursor.execute(sql)
                    con.commit()
                    sql = "UPDATE Env.devicetable SET count_humi=0,notify_humi=0 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
            elif int(self.humi)>=int(self.maxHumi):
                print("Alert_humi_rangeAbove")
                Hist_db_data= "SELECT count_humi FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==0:
                    print("humi_max")
                    self.AlertHumi=1
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertHumi) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertHumi}')"
                    kursor.execute(sql)
                    con.commit()
                    self.AlertHumi=0
                    print(kursor.rowcount)
                    sql = "UPDATE Env.devicetable SET count_humi=1,notify_humi=1 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
            elif int(self.humi)<=int(self.minHumi):
                print("Alert_temp_rangebelow")
                Hist_db_data= "SELECT count_humi FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==0:
                    print("Humi_min")
                    self.AlertHumi=1
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertHumi) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertHumi}')"
                    kursor.execute(sql)
                    con.commit()
                    self.AlertHumi=0
                    print(kursor.rowcount)
                    sql = "UPDATE Env.devicetable SET count_humi=1,notify_humi=1 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
        except Exception as e:
            print(e)
    def rangeMoistAlert(self):
        try:
            if int(self.moist)>=int(self.minMoist) and int(self.moist)<=int(self.maxMoist):
                print("alert moist normal")
                Hist_db_data= "SELECT count_moist FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==1:
                    print("normal_moist_below")
                    self.AlertMoist=0
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertMoist) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertMoist}')"
                    kursor.execute(sql)
                    con.commit()
                    sql = "UPDATE Env.devicetable SET count_moist=0,notify_moist=0 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
            elif int(self.moist)>=int(self.maxMoist):
                print("Alert_moist_rangeAbove")
                Hist_db_data= "SELECT count_moist FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==0:
                    print("moist_max")
                    self.AlertMoist=1
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertMoist) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertMoist}')"
                    kursor.execute(sql)
                    con.commit()
                    self.AlertMoist=0
                    print(kursor.rowcount)
                    sql = "UPDATE Env.devicetable SET count_moist=1,notify_moist=1 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
            elif int(self.moist)<=int(self.minMoist):
                print("Alert_moist_rangebelow")
                Hist_db_data= "SELECT count_moist FROM devicetable WHERE deviceid ='{}'".format(self.DevcId)
                kursor.execute(Hist_db_data)
                rows_data=kursor.fetchall()
                Alert=rows_data[0]
                Alert=Alert[0]
                print(Alert)
                if Alert==0:
                    print("Moist_min")
                    self.AlertMoist=1
                    sql = f"INSERT INTO history_table (userid, deviceid, devicename ,temperature ,humidity , moisture, fire, alertMoist) VALUES ('{self.user_Id}','{self.DevcId}','{self.DvcName}','{self.temp}','{self.humi}','{self.moist}','{self.Fire}','{self.AlertMoist}')"
                    kursor.execute(sql)
                    con.commit()
                    self.AlertMoist=0
                    print(kursor.rowcount)
                    sql = "UPDATE Env.devicetable SET count_moist=1,notify_moist=1 WHERE deviceid = '{}'".format(self.DevcId)
                    kursor.execute(sql)
                    con.commit()
        except Exception as e:
            print(e)
    def main(self):
            self.client = mqtt.Client()
            self.client.username_pw_set("supro", "T62$pO^GxSG94SFMvqNQgR1$k")
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.connect("supro.shunyaekai.tech", 1883, 60)
            self.client.loop_forever()
            gc.collect()
            return self
if __name__=="__main__":
    env_mqtt().main()
    handle=env_mqtt.on_message
    handle.join()
    
