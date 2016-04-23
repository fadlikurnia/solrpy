#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Parama_Fadli_Kurnia"
__date__ = "$Apr 19, 2016 10:07:40 AM$"

from py.connecty import MakeConnect
import MySQLdb

mc = MakeConnect()
class MakeModel:
    def getFlightCache(self, offset = 0, limit = 10):
        con = mc.getDBConnection("private", "ezy_flight")
        cursor = con.cursor()
#        cursor.execute('SELECT * FROM a_view LIMIT '+str(limit)+' OFFSET '+str(offset))
        cursor.execute('SELECT * FROM cache_view LIMIT '+str(limit)+' OFFSET '+str(offset))
#        return [str(row[0]).replace("+"," ") for row in cursor.fetchall()]
        return cursor
    
