#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# ip address = http://162.243.79.199/

__author__ = "Parama_Fadli_Kurnia"
__date__ = "$Apr 12, 2016 4:46:03 PM$"

import MySQLdb

class MakeConnect:
    def getSolrConnection(self, ip_address="", port="", core=""):
        solrHome = "http://" + ip_address + ":" + port + "/solr/" + core;
        return solrHome
            
    def getDBConnection(self, privacy, database):
        if(privacy == "private"):
            return MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db=database)
        else:
            return MySQLdb.connect(host="localhost", user="root", passwd="", db=database)
    