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

    def get_employee_id(self):
        html = self.session.get(START_URL).text
        regex = '(?<=var mdwID = )[^;]+'
        match = re.findall(regex, html)
        return_id = demjson.decode(match[0])
        return str(return_id)

    def get_todays_logs(self, employee_id):
        """
        :param employee_id: Required: ID of the employee
        :return: List containing dictionary objects with log information for today.
        """
        todays_logs = self.session.get(START_URL + 'api/TijdLog/GetTijdLogsVanMedewerker/' + employee_id)
        # return(todays_logs.text)
        # Convert the javascript object to Python object
        return demjson.decode(todays_logs.text)

    def get_todays_workhours(self, employee_id):
        """
        :param employee_id: Required: ID of the employee
        :return: String with total amount of workhours that should be performed today.
        """
        todays_workhours = self.session.get(START_URL + 'api/TijdLog/GetWerkurenMedewerker/' + employee_id)
        return todays_workhours.text

    def get_todays_remaining_workhours(self, employee_id):
        """
        :param employee_id: Required: ID of the employee
        :return: String with remaining amount of workhours for today.
        """
        todays_remaining_workhours = self.session.get(
            START_URL + 'api/TijdLog/GetNegPresterenMedewerker/' + employee_id)
        return todays_remaining_workhours.text

    def get_statistics(self, employee_id):
        # TODO Implement method to get_statistics
        return

    def get_organisation_counter_settings(self, employee_id):
        """
        :param employee_id: Required: ID of the employee
        :return: Dictionary containing information about the settings for the timer.
        """
        counter_settings = self.session.get(START_URL + 'api/TijdLog/orgCon_counterSettings?mdwid=' + employee_id)
        return demjson.decode(counter_settings.text)

    def get_is_location_mandatory(self, employee_id):
        """
        :param employee_id: Required: ID of the employee
        :return: Dictionary containing information about location setting
        """
        is_location_mandatory = self.session.get(
            START_URL + 'api/TijdLog/GetIsLocatieVerplicht/?id=' + employee_id + '&apiVersie=2')
        return demjson.decode(is_location_mandatory.text)

    def get_summarised_timelogs_from_month(self, employee_id, month_year):
        """
        :param employee_id: Required: ID of the employee
        :param month_year: Required: String formatted like 'december 2018'
        :return: List containing dictionary objects with summarised timelog information about the selected month.
        """
        timelogs_from_month = self.session.get(
            START_URL + 'api/TijdLog/GetTijdLogsVanMaand/?userID=' + employee_id + '&maand=' + month_year + '&apiVersie=2')
        return demjson.decode(timelogs_from_month.text)

