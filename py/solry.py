#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Parama_Fadli_Kurnia"
__date__ = "$Apr 12, 2016 5:03:30 PM$"

from py.connecty import MakeConnect
from py.componenty import MakeComponent
from py.modely import MakeModel
#import dateutil.parser as parser
import datetime, solr
import urllib2

mc = MakeConnect()
mm = MakeModel()
mcp = MakeComponent()
class MakeSolr:
    def insert_data(self, offset, limit, div=200):
        index = 0
#        limit = 10000
#        offset = 0
#        div = 500
        s = solr.SolrConnection(mc.getSolrConnection("localhost", "8983", "cache_flight"))
#        s = solr.SolrConnection(mc.getSolrConnection("localhost", "8983", "cflight"))
        
        data = mm.getFlightCache(offset, limit)
        for row in data.fetchall():
            supplier_id = row[0]
            cache_airline = row[1]
            cache_adult = row[2]
            cache_child = row[3]
            cache_infant = row[4]
            cache_from = row[5]
            cache_to = row[6]
            cache_departure_date = row[7]
            cache_return_date = row[8]
            cache_last_update = row[9]
            cache_flight_id = row[10]
            cache_flight_schedule_class = row[11]
            cache_flight_schedule_air_equip_type = row[12]
            cache_flight_schedule_airline_code = row[13]
            cache_flight_schedule_flight_number = row[14]
            cache_flight_schedule_from_name = row[15]
            cache_flight_schedule_from = row[16]
            cache_flight_schedule_to_name = row[17]
            cache_flight_schedule_to = row[18]
            cache_flight_schedule_departure_date = row[19]
            cache_flight_schedule_departure_time = row[20]
            cache_flight_schedule_departure_timezone = row[21]
            cache_flight_schedule_arrival_date = row[22]
            cache_flight_schedule_arrival_time = row[23]
            cache_flight_schedule_arrival_timezone = row[24]
            cache_flight_schedule_travel_time = row[25]
            cache_flight_schedule_type = row[26]
            cache_id = row[27]
            price_type_id = row[28]
            airline_id = row[29]
            cache_flight_currency = row[30]
            cache_flight_base_adt = row[31]
            cache_flight_base_chd = row[32]
            cache_flight_base_inf = row[33]
            cache_flight_tax_adt = row[34]
            cache_flight_tax_chd = row[35]
            cache_flight_tax_inf = row[36]
            
            cache_departure_date = mcp.generateDate(cache_departure_date)
            cache_return_date = mcp.generateDate(cache_return_date)
            cache_last_update = mcp.generateDate(cache_last_update)
            cache_flight_schedule_departure_date = mcp.mergeDate(cache_flight_schedule_departure_date, cache_flight_schedule_departure_time)
            cache_flight_schedule_arrival_date = mcp.mergeDate(cache_flight_schedule_arrival_date, cache_flight_schedule_arrival_time)
            
            s0 = '%s' % (str(supplier_id))
            s1 = '%s' % (str(cache_airline))
            s2 = '%s' % (str(cache_adult))
            s3 = '%s' % (str(cache_child))
            s4 = '%s' % (str(cache_infant))
            s5 = '%s' % (str(cache_from))
            s6 = '%s' % (str(cache_to))
            s7 = '%s' % (str(cache_departure_date))
            s8 = '%s' % (str(cache_return_date))
            s9 = '%s' % (str(cache_last_update))
            s10 = '%s' % (str(cache_flight_id))
            s11 = '%s' % (str(cache_flight_schedule_class))
            s12 = '%s' % (str(cache_flight_schedule_air_equip_type))
            s13 = '%s' % (str(cache_flight_schedule_airline_code))
            s14 = '%s' % (str(cache_flight_schedule_flight_number))
            s15 = '%s' % (str(cache_flight_schedule_from_name))
            s16 = '%s' % (str(cache_flight_schedule_from))
            s17 = '%s' % (str(cache_flight_schedule_to_name))
            s18 = '%s' % (str(cache_flight_schedule_to))
            s19 = '%s' % (str(cache_flight_schedule_departure_date))
            s20 = '%s' % (str(cache_flight_schedule_departure_time))
            s21 = '%s' % (str(cache_flight_schedule_departure_timezone))
            s22 = '%s' % (str(cache_flight_schedule_arrival_date))
            s23 = '%s' % (str(cache_flight_schedule_arrival_time))
            s24 = '%s' % (str(cache_flight_schedule_arrival_timezone))
            s25 = '%s' % (str(cache_flight_schedule_travel_time))
            s26 = '%s' % (str(cache_flight_schedule_type))
            s27 = '%s' % (str(cache_id))
            s28 = '%s' % (str(price_type_id))
            s29 = '%s' % (str(airline_id))
            s30 = '%s' % (str(cache_flight_currency))
            s31 = '%s' % (str(cache_flight_base_adt))
            s32 = '%s' % (str(cache_flight_base_chd))
            s33 = '%s' % (str(cache_flight_base_inf))
            s34 = '%s' % (str(cache_flight_tax_adt))
            s35 = '%s' % (str(cache_flight_tax_chd))
            s36 = '%s' % (str(cache_flight_tax_inf))
            s_index = '%s' % (str(offset))
        
            s.add(id=s_index, 
                supplier_id = s0,
                cache_airline = s1,
                cache_adult = s2,
                cache_child = s3,
                cache_infant = s4,
                cache_from = s5,
                cache_to = s6,
                cache_departure_date = s7,
                cache_return_date = s8,
                cache_last_update = s9,
                cache_flight_id = s10,
                cache_flight_schedule_class = s11,
                cache_flight_schedule_air_equip_type = s12,
                cache_flight_schedule_airline_code = s13,
                cache_flight_schedule_flight_number = s14,
                cache_flight_schedule_from_name = s15,
                cache_flight_schedule_from = s16,
                cache_flight_schedule_to_name = s17,
                cache_flight_schedule_to = s18,
                cache_flight_schedule_departure_date = s19,
                cache_flight_schedule_departure_time = s20,
                cache_flight_schedule_departure_timezone = s21,
                cache_flight_schedule_arrival_date = s22,
                cache_flight_schedule_arrival_time = s23,
                cache_flight_schedule_arrival_timezone = s24,
                cache_flight_schedule_travel_time = s25,
                cache_flight_schedule_type = s26,
                cache_id = s27,
                price_type_id = s28,
                airline_id = s29,
                cache_flight_currency = s30,
                cache_flight_base_adt = s31,
                cache_flight_base_chd = s32,
                cache_flight_base_inf = s33,
                cache_flight_tax_adt = s34,
                cache_flight_tax_chd = s35,
                cache_flight_tax_inf = s36
                )
                
            print offset, index, airline_id, cache_from, cache_to 
            index+=1
            offset+=1
            if(index%div==0):
                req = urllib2.Request('http://localhost:8983/solr/cache_flight/update?commit=true')
                urllib2.urlopen(req, "")
        print "FINISHED"
        #command = 'curl http://localhost:8983/solr/cache_flight/update?commit=true'
        

#http://localhost:8983/solr/cache_flight/update?stream.body=%3Cdelete%3E%3Cquery%3E*:*%3C/query%3E%3C/delete%3E&commit=true


