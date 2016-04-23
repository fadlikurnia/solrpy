#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Parama_Fadli_Kurnia"
__date__ = "$Apr 19, 2016 10:50:47 AM$"

class MakeComponent:
    def mergeDate(self, date, hour):
        strDate = ""
        if((date is not None)and(hour is not None)):
            date = str(date)
            strDate = date+"T"+hour+":00Z"
        else:
            date = str(date)
            strDate = date+"T00:00:00Z"
        return strDate

    def generateDate(self, date):
        strDate = ""
        if(date is not None):
            date = str(date)
            arrayDate = date.split()
            countData = len(arrayDate)
            if(countData>2):
                strDate = arrayDate[0]+"T"+arrayDate[1]+":00Z"
            else:
                strDate = arrayDate[0]+"T00:00:00Z"
        else:
            strDate = "0000-00-00T00:00:00Z"
        return strDate
