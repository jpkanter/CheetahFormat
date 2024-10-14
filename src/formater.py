#!/usr/bin/env python3
# coding: utf-8

# Copyright 2022 by JPKanter, <kanter@ub.uni-leipzig.de>
#
# This file is part of CheetahFormat.
#
# CheetahFormat is free software: you can redistribute
# it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# CheetahFormat is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# @license GPL-3.0-only <https://www.gnu.org/licenses/gpl-3.0.en.html>


import tomli
import logging
import re
from inspect import getsourcefile
from os.path import abspath, dirname

logger = logging.getLogger(__name__)


class bcolors:
    """
    Some color codes lifted from a Stack Overflow post I forgot which lifted it from Blender it seems
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Formater:
    """
    The actual implementation of the formatter, uses a very primitiv (in terms of style not basic class)
    to replace parts of string for another. I originally build this for my meetings notes for Redmine
    which are written in Textile, but colors are a pain there, but I like colors, so I made a handy
    shortcut to write while jotting down the meeting talking points like I can do in Markdown
    """
    def __init__(self, config=None):
        self.config = self.import_config(config)

    @staticmethod
    def import_config(path_or_data=None) -> dict:
        """
        Opens the given config file and attempts to read & validate it as config
        :param str path_or_data: path to the toml file or a direct config
        :return: the dictionary that is the config
        :rtype: dict
        """
        # insert checks for integrity here
        pre_config = None
        fallback = False

        if isinstance(path_or_data, str):
            try:
                with open(path_or_data, "br") as that:
                    pre_config = tomli.load(that)
            except FileNotFoundError as e:
                logging.warn(f"{e} - Provided Path not found, Fallback to default")
                fallback = True
        if not path_or_data or fallback:
            local = dirname(abspath(getsourcefile(lambda: 0)))
            with open(f"{local}/example_config.toml", "br") as that:
                pre_config = tomli.load(that)
        if pre_config:
            keys = ['enclosure', 'start', 'end', 'multiline']
            if all(key in expression for key in keys for expression in pre_config.values()):
                return pre_config  # as config
        raise ValueError("Formater: loading of config failed")

    def list_filters(self) -> list[str]:
        lines = []
        for key, value in self.config.items():
            line =  f"{bcolors.BOLD}{key}{bcolors.ENDC}: "
            line += f"{bcolors.OKBLUE}{value['enclosure']}{bcolors.ENDC}"
            line += "your text"
            line += f"{bcolors.OKCYAN}{value['enclosure']}{bcolors.ENDC}"
            lines.append(line)
        return lines

    def format_line(self, line: str) -> str:
        """
        Formats a single line according to the config file
        :param str line: a singular line of string, hopefully without any line denominators
        :return: the formated string
        :rtype: str
        """
        for key, value in self.config.items():
            if value['multiline']:
                # todo: write actual multi line support you lazy bastard
                logging.warn(f"Multiline match '{value['enclosure']}' found, feature not implemented")
                continue  # single line function cannot support multiline
            logger.debug(f"OneLine>>Key: {key}")
            search = "\\{}(.+?)\\{}".format(value['enclosure'], value['enclosure'])
            matches = [match.span() for match in re.finditer(search, line)]
            if matches:
                for j in reversed(matches):  # reversed assuming regex finds will always be in order
                    line = line[:j[0]] + value['start'] + \
                           line[j[0]+len(value['enclosure']):j[1]-len(value['enclosure'])] + \
                           value['end'] + line[j[1]:]
        return line
        # apparently re.sub is a thing

