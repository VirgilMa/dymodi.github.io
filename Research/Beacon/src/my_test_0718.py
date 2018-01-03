#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:22:41 2017

@author: eleme-yi
"""

# The ground truth trace of myTest0718
trace_latitude_truth = [31.232763,31.232769,31.232775,31.232781,\
                        31.232787,31.232793,31.232799,31.232805,\
                        31.232811,31.232817,31.2328237,31.23283039,\
                        31.23283709,31.23284378,31.23285048,31.23285717,\
                        31.23286387,31.23287057,31.23287726,31.23288396,\
                        31.23289065,31.23289735,31.23290404,31.23291074,\
                        31.23291743,31.23292413,31.23293083,31.23293752,\
                        31.23294422,31.23295091,31.23295761,31.2329643,\
                        31.232971,31.23297707,31.23298314,31.23298921,\
                        31.23299529,31.23300136,31.23300743,31.2330135,\
                        31.23301957,31.23302564,31.23303171,31.23303779,\
                        31.23304386,31.23304993,31.233056,31.233061,\
                        31.233066,31.233071,31.233076,31.233081,\
                        31.233086,31.233091,31.23308225,31.2330735,\
                        31.23306475,31.233056,31.233063,31.23307,\
                        31.233077,31.233084,31.233091,31.23309933,\
                        31.23310767,31.233116,31.23312433,31.23313267,\
                        31.233141,31.2331448,31.2331486,31.2331524,\
                        31.2331562,31.23316,31.233158,31.233156,\
                        31.233154,31.233152,31.23315,31.233148,\
                        31.233146,31.233144,31.233142,31.23314,\
                        31.233138,31.233136,31.233134,31.233132,\
                        31.23313,31.233128,31.233126,31.233124,\
                        31.233122,31.2331154,31.2331088,31.2331022,\
                        31.2330956,31.233089,31.2330824,31.2330758,\
                        31.2330692,31.2330626,31.233056,31.23305521,\
                        31.23305441,31.23305362,31.23305283,31.23305203,\
                        31.23305124,31.23305045,31.23304966,31.23304886,\
                        31.23304807,31.23304728,31.23304648,31.23304569,\
                        31.2330449,31.2330441,31.23304331,31.23304252,\
                        31.23304172,31.23304093,31.23304014,31.23303934,\
                        31.23303855,31.23303776,31.23303697,31.23303617,\
                        31.23303538,31.23303459,31.23303379,31.233033,\
                        31.23303221,31.23303141,31.23303062,31.23302983,\
                        31.23302903,31.23302824]

trace_longitude_truth = [121.382699,121.3826926,121.3826861,121.3826797,\
                         121.3826732,121.3826668,121.3826603,121.3826539,\
                         121.3826474,121.382641,121.38263,121.3826191,\
                         121.3826081,121.3825972,121.3825862,121.3825753,\
                         121.3825643,121.3825533,121.3825424,121.3825314,\
                         121.3825205,121.3825095,121.3824986,121.3824876,\
                         121.3824767,121.3824657,121.3824547,121.3824438,\
                         121.3824328,121.3824219,121.3824109,121.3824,\
                         121.382389,121.3823816,121.3823743,121.3823669,\
                         121.3823596,121.3823522,121.3823449,121.3823375,\
                         121.3823301,121.3823228,121.3823154,121.3823081,\
                         121.3823007,121.3822934,121.382286,121.3822744,\
                         121.3822629,121.3822513,121.3822397,121.3822281,\
                         121.3822166,121.382205,121.3821748,121.3821445,\
                         121.3821143,121.382084,121.3820758,121.3820676,\
                         121.3820594,121.3820512,121.382043,121.3820327,\
                         121.3820223,121.382012,121.3820017,121.3819913,\
                         121.381981,121.3819746,121.3819682,121.3819618,\
                         121.3819554,121.381949,121.3819474,121.3819457,\
                         121.3819441,121.3819425,121.3819408,121.3819392,\
                         121.3819376,121.3819359,121.3819343,121.3819327,\
                         121.3819311,121.3819294,121.3819278,121.3819262,\
                         121.3819245,121.3819229,121.3819213,121.3819196,\
                         121.381918,121.3819292,121.3819404,121.3819516,\
                         121.3819628,121.381974,121.3819852,121.3819964,\
                         121.3820076,121.3820188,121.38203,121.3820316,\
                         121.3820331,121.3820347,121.3820362,121.3820378,\
                         121.3820393,121.3820409,121.3820424,121.382044,\
                         121.3820455,121.3820471,121.3820486,121.3820502,\
                         121.3820517,121.3820533,121.3820548,121.3820564,\
                         121.3820579,121.3820595,121.382061,121.3820626,\
                         121.3820641,121.3820657,121.3820672,121.3820688,\
                         121.3820703,121.3820719,121.3820734,121.382075,\
                         121.3820766,121.3820781,121.3820797,121.3820812,\
                         121.3820828,121.3820843]

