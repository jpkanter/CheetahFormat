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

import pyperclip

from formater import Formater

if __name__ == "__main__":
    """
    Default module uses clipboard as source for the formatting, will probably use default if not otherwise specified
    """
    duck = Formater()
    all_is_text = pyperclip.paste()
    lines = str(all_is_text).split("\n")
    yarn = ""
    for line in lines:
        yarn += duck.format_line(line) + "\n"
    pyperclip.copy(yarn)
