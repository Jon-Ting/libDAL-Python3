#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
"""
 * dalclient library - provides utilities to assist in using KDDart-DAL servers
 * Copyright (C) 2017  Diversity Arrays Technology
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from .IDALClient import IDALClient

__author__ = "alexs"
__copyright__ = "Copyright (C) 2017  Diversity Arrays Technology"
__license__ = "GPL 3.0"
__email__ = ""


class DALXmlConfig(object):

    def __init__(self):
        self._result = dict()

    def parse(self, root):
        for child in root:
            if not child.tag in list(self._result.keys()):
                self._result[child.tag] = []
            self._result[child.tag].append(self.child_as_dict(child))

        return self._result


    def child_as_dict(self, parent):

        dictresult = dict(parent.attrib)
        for child in parent:
            if not child.tag in list(dictresult.keys()):
                dictresult[child.tag] = []
            dictresult[child.tag].append(self.child_as_dict(child))

        return dictresult




