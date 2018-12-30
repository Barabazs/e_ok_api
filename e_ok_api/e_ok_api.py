# -*- coding: utf-8 -*-

import re
import urllib

import demjson
import requests
from lxml import etree

START_URL = 'https://time.e-ok.be/'


class TimeEOK:

    def __init__(self):
        self.session = requests.Session()

    def login(self, login, password):
        token_request = self.session.get(START_URL)
        parser = etree.HTMLParser()
        tree = etree.fromstring(token_request.text, parser)
        # Extract the RequestVerificationToken  to be used in the login query
        verification_token = tree.xpath('//form//input[@name="__RequestVerificationToken"]/@value')[0]
        # set the SessionCookies
        session_cookies = token_request.cookies
        payload = {
            '__RequestVerificationToken': verification_token,
            'Username': login,
            'LegacyPass': password
        }
        raw = urllib.parse.urlencode(payload)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        # return the open session object for future handling
        return self.session.post(START_URL + 'user/login/', data=raw, cookies=session_cookies, headers=headers)

    def get_userid(self):
        html = self.session.get(START_URL).text
        regex = '(?<=var mdwID = )[^;]+'
        match = re.findall(regex, html)
        return_id = demjson.decode(match[0])
        return str(return_id)

    def get_todays_logs(self, mdwid):
        todays_logs = self.session.get(START_URL + 'api/TijdLog/GetTijdLogsVanMedewerker/' + mdwid)
        # return(todays_logs.text)
        # Convert the javascript object to Python object
        return demjson.decode(todays_logs.text)

    def get_todays_workhours(self, mdwid):
        todays_workhours = self.session.get(START_URL + 'api/TijdLog/GetWerkurenMedewerker/' + mdwid)
        return todays_workhours.text

    def get_remaining_workhours(self, mdwid):
        remaining_workhours = self.session.get(START_URL + 'api/TijdLog/GetNegPresterenMedewerker/' + mdwid)
        return remaining_workhours.text

    def get_statistics(self, mdwid):
        # TODO Implement method to get_statistics
        return

    def get_organisation_counter_settings(self, mdwid):
        counter_settings = self.session.get(START_URL + 'api/TijdLog/orgCon_counter_settings?mdwid=' + mdwid)
        return demjson.decode(counter_settings.text)
