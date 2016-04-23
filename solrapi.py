#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Parama_Fadli_Kurnia"
__date__ = "$Apr 12, 2016 5:03:30 PM$"

from py.solry import MakeSolr

msl = MakeSolr()
limit = 500000
offset = 0

msl.insert_data(offset, limit)
