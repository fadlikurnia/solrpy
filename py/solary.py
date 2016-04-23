#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Parama_Fadli_Kurnia"
__date__ = "$Apr 12, 2016 5:03:30 PM$"

from py.connecty import MakeConnect
from py.componenty import MakeComponent
from py.modely import MakeModel
import dateutil.parser as parser
import datetime, solr

mc = MakeConnect()
mm = MakeModel()
mcp = MakeComponent()
class MakeSolar:
    def insert_data(self, offset, limit, div=50000):
        index = 0
#        limit = 10000
#        offset = 0
#        div = 500
#        s = solr.SolrConnection(mc.getSolrConnection("localhost", "8983", "cache_flight"))
        s = solr.SolrConnection(mc.getSolrConnection("localhost", "8983", "cflight"))
        
        data = mm.getFlightCache(offset, limit)
        for row in data.fetchall():
            airline_id = row[0]
            cache_adult = row[1]
            cache_child = row[2]
            cache_infant = row[3]
            cache_from = row[4]
            cache_to = row[5]
            cache_departure_date = row[6]
            cache_return_date = row[7]
            cache_class = row[8]
            cache_queue_type = row[9]
            cache_queue_status = row[10]
            cache_queue_date = row[11]
            cache_flight_id = row[12]
            cache_flight_schedule_class = row[13]
            cache_flight_schedule_air_equip_type = row[14]
            cache_flight_schedule_airline_code = row[15]
            cache_flight_schedule_flight_number = row[16]
            cache_flight_schedule_from_name = row[17]
            cache_flight_schedule_from = row[18]
            cache_flight_schedule_to_name = row[19]
            cache_flight_schedule_to = row[20]
            cache_flight_schedule_departure_date = row[21]
            cache_flight_schedule_departure_time = row[22]
            cache_flight_schedule_departure_timezone = row[23]
            cache_flight_schedule_arrival_date = row[24]
            cache_flight_schedule_arrival_time = row[25]
            cache_flight_schedule_arrival_timezone = row[26]
            cache_flight_schedule_travel_time = row[27]
            cache_flight_schedule_type = row[28]
            cache_id = row[29]
            price_type_id = row[30]
            cache_flight_currency = row[31]
            cache_flight_base_adt = row[32]
            cache_flight_base_chd = row[33]
            cache_flight_base_inf = row[34]
            cache_flight_tax_adt = row[35]
            cache_flight_tax_chd = row[36]
            cache_flight_tax_inf = row[37]
            
            cache_departure_date = mcp.generateDate(cache_departure_date)
            cache_return_date = mcp.generateDate(cache_return_date)
            cache_queue_date = mcp.generateDate(cache_queue_date)
            cache_flight_schedule_departure_date = mcp.mergeDate(cache_flight_schedule_departure_date, cache_flight_schedule_departure_time)
            cache_flight_schedule_arrival_date = mcp.mergeDate(cache_flight_schedule_arrival_date, cache_flight_schedule_arrival_time)
            
            s0 = '%s' % (str(airline_id))
            s1 = '%s' % (str(cache_adult))
            s2 = '%s' % (str(cache_child))
            s3 = '%s' % (str(cache_infant))
            s4 = '%s' % (str(cache_from))
            s5 = '%s' % (str(cache_to))
            s6 = '%s' % (str(cache_departure_date))
            s7 = '%s' % (str(cache_return_date))
            s8 = '%s' % (str(cache_class))
            s9 = '%s' % (str(cache_queue_type))
            s10 = '%s' % (str(cache_queue_status))
            s11 = '%s' % (str(cache_queue_date))
            s12 = '%s' % (str(cache_flight_id))
            s13 = '%s' % (str(cache_flight_schedule_class))
            s14 = '%s' % (str(cache_flight_schedule_air_equip_type))
            s15 = '%s' % (str(cache_flight_schedule_airline_code))
            s16 = '%s' % (str(cache_flight_schedule_flight_number))
            s17 = '%s' % (str(cache_flight_schedule_from_name))
            s18 = '%s' % (str(cache_flight_schedule_from))
            s19 = '%s' % (str(cache_flight_schedule_to_name))
            s20 = '%s' % (str(cache_flight_schedule_to))
            s21 = '%s' % (str(cache_flight_schedule_departure_date))
            s22 = '%s' % (str(cache_flight_schedule_departure_time))
            s23 = '%s' % (str(cache_flight_schedule_departure_timezone))
            s24 = '%s' % (str(cache_flight_schedule_arrival_date))
            s25 = '%s' % (str(cache_flight_schedule_arrival_time))
            s26 = '%s' % (str(cache_flight_schedule_arrival_timezone))
            s27 = '%s' % (str(cache_flight_schedule_travel_time))
            s28 = '%s' % (str(cache_flight_schedule_type))
            s29 = '%s' % (str(cache_id))
            s30 = '%s' % (str(price_type_id))
            s31 = '%s' % (str(cache_flight_currency))
            s32 = '%s' % (str(cache_flight_base_adt))
            s33 = '%s' % (str(cache_flight_base_chd))
            s34 = '%s' % (str(cache_flight_base_inf))
            s35 = '%s' % (str(cache_flight_tax_adt))
            s36 = '%s' % (str(cache_flight_tax_chd))
            s37 = '%s' % (str(cache_flight_tax_inf))
            s_index = '%s' % (str(offset))
        
            s.add(id=s_index, 
                airline_id = s0,
                cache_adult = s1,
                cache_child = s2,
                cache_infant = s3,
                cache_from = s4,
                cache_to = s5,
                cache_departure_date = s6,
                cache_return_date = s7,
                cache_class = s8,
                cache_queue_type = s9,
                cache_queue_status = s10,
                cache_queue_date = s11,
                cache_flight_id = s12,
                cache_flight_schedule_class = s13,
                cache_flight_schedule_air_equip_type = s14,
                cache_flight_schedule_airline_code = s15,
                cache_flight_schedule_flight_number = s16,
                cache_flight_schedule_from_name = s17,
                cache_flight_schedule_from = s18,
                cache_flight_schedule_to_name = s19,
                cache_flight_schedule_to = s20,
                cache_flight_schedule_departure_date = s21,
                cache_flight_schedule_departure_time = s22,
                cache_flight_schedule_departure_timezone = s23,
                cache_flight_schedule_arrival_date = s24,
                cache_flight_schedule_arrival_time = s25,
                cache_flight_schedule_arrival_timezone = s26,
                cache_flight_schedule_travel_time = s27,
                cache_flight_schedule_type = s28,
                cache_id = s29,
                price_type_id = s30,
                cache_flight_currency = s31,
                cache_flight_base_adt = s32,
                cache_flight_base_chd = s33,
                cache_flight_base_inf = s34,
                cache_flight_tax_adt = s35,
                cache_flight_tax_chd = s36,
                cache_flight_tax_inf = s37
                )
                
            print offset, index, airline_id, cache_from, cache_to 
            index+=1
            offset+=1
            if(index%div==0):s.commit()
        print "FINISHED"

#http://localhost:8983/solr/cache_flight/update?stream.body=%3Cdelete%3E%3Cquery%3E*:*%3C/query%3E%3C/delete%3E&commit=true


