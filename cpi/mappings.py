#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Parses the mapping files that explain various codes contained within each series.
"""
from .parser import BaseParser
from .models import ObjectList, Area, Period


class ParseArea(BaseParser):
    """
    Parses the raw list of CPI areas.
    """
    def parse(self):
        """
        Returns a list Area objects.
        """
        object_list = ObjectList()
        for row in self.get_file('cu.area'):
            obj = Area(row['area_code'], row['area_name'])
            object_list.append(obj)
        return object_list


class ParsePeriod(BaseParser):
    """
    Parses the raw list of CPI periods.
    """
    def parse(self):
        """
        Returns a list Area objects.
        """
        object_list = ObjectList()
        for row in self.get_file('cu.period'):
            obj = Period(row['period'], row['period_abbr'], row['period_name'])
            object_list.append(obj)
        return object_list