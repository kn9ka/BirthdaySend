#!/usr/bin/env python
# -*- coding: utf-8 -*-

import win32com.client

OUTLOOK_MAIL_ITEM = 0
OUTLOOK_APPOINTMENT_ITEM  = 1
OUTLOOK_TASK_ITEM = 3

OUTLOOK_MEETING           = 1
OUTLOOK_ORGANIZER         = 0
OUTLOOK_REQUIRED_ATTENDEE = 1
OUTLOOK_OPTIONAL_ATTENDEE = 2

TWO_MINUTES = 2
FIVE_MINUTES = 5
FIFTY_MINUTES = 15
THIRTY_MINUTES = 30
ONE_HOUR       = 60
TWO_AND_HALF_OF_HOUR = 90
TWO_HOUR = 120

OUTLOOK_FORMAT = '%d/%m/%Y %H:%M'
outlook_date   = lambda dt: dt.strftime(OUTLOOK_FORMAT)


class OutlookClient(object):

    def __init__(self):
        self.outlook = win32com.client.Dispatch('Outlook.Application')

    def send_meeting_request(self, subject, time, location, body, required_recipients, optional_recipients=None):
        mtg = self.outlook.CreateItem(OUTLOOK_APPOINTMENT_ITEM)
        mtg.MeetingStatus = OUTLOOK_MEETING
        mtg.Location = location

        for recipient in required_recipients:
            invitee      = mtg.Recipients.Add(recipient)
            invitee.Type = OUTLOOK_REQUIRED_ATTENDEE

        if optional_recipients==None:
            pass
        else:
            for recipient in optional_recipients:
                invitee      = mtg.Recipients.Add(recipient)
                invitee.Type = OUTLOOK_OPTIONAL_ATTENDEE

        mtg.Subject                    = subject
        mtg.Start                      = outlook_date(time)
        mtg.Duration                   = 2
        mtg.ReminderMinutesBeforeStart = TWO_HOUR
        mtg.ResponseRequested          = False
        mtg.Body                       = body
        mtg.Send()

    def send_mail(self,recepient, subject, body):
        msg = self.outlook.CreateItem(OUTLOOK_MAIL_ITEM)
        msg.To = recepient
        msg.Subject = subject
        msg.body = body
        msg.Send()


    def send_appointment(self, Subject, Start, Body):
        mta = self.outlook.CreateItem(OUTLOOK_TASK_ITEM)
        mta.Subject = Subject
        mta.StartDate = outlook_date(Start)
        mta.DueDate = outlook_date(Start)
        mta.Status = 1
        mta.Importance = 1
        mta.ReminderSet = False
        mta.Body = Body
        mta.Save()

''' EXAMPLE
if __name__ == '__main__':
    import datetime
    from datetime import date, time, datetime
    ol = OutlookClient()
    ol.send_meeting_request('TEST', datetime.strptime('10/10/2016 17:00', '%d/%m/%Y %H:%M'),'','',['email@domain.com'])
'''