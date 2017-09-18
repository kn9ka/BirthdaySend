#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from datetime import date, time, datetime
from outlook import OutlookClient
from excelread import readFromExcel

ol = OutlookClient()
excelFile = r'''path/to/file'''
excel = readFromExcel(excelFile)