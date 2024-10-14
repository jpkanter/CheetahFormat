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
#v
# @license GPL-3.0-only <https://www.gnu.org/licenses/gpl-3.0.en.html>

import pyperclip
import logging
import argparse

from formater import Formater

def filter_lines(filters: list, insert_in: str):
    all_is_text = pyperclip.paste()
    lines = str(all_is_text).split("\n")
    out = ""
    for line in lines:
        if line.strip() == "":
            continue
        for one_filter in filters:
            if one_filter in line:
                continue
        out += insert_in.format(line)
    pyperclip.copy(out)


if __name__ == "__main__":
    """
    Default module uses clipboard as source for the formatting, will probably use default if not otherwise specified
    """
    parser = argparse.ArgumentParser(
        description="Cheetah Formater  - Quick Formater for some texts",
        usage="main.py --config [configPath]",
        epilog="Changes whatever text currently is in your clipboard.",
        prefix_chars="-"
    )
    parser.add_argument("--config", type=str, help="path to individual *.toml")
    parser.add_argument("--tags", action='store_true', help="list current used replacement tags")
    args = parser.parse_args()

    #print("[Cheetah] CWD" + os.getcwd())
    if args.config:
        logging.info(f"[Cheetah] Config Path: {args.config}")
        config_path = args.config
    else:
        config_path = None

    if args.tags:
        goose = Formater(config_path)
        for each in goose.list_filters():
            print(each)
        exit(0)

    duck = Formater(config_path)
    all_is_text = pyperclip.paste()
    lines = str(all_is_text).split("\n")
    yarn = ""
    for line in lines:
        yarn += duck.format_line(line) + "\n"
    pyperclip.copy(yarn)
    logging.info("[Cheetah] Done")
