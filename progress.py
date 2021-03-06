#!/usr/bin/python3
#
# Copyright (C) 2021  Xenofon Fafoutis <xefa@dtu.dk>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from reqlib import req
import myconfig as cfg

report_prefix = "SC2-Report"

print("Loading file:", cfg.reqfile, "(last modified:", req.datemodified(cfg.reqfile) + ")")
allreqs = req.readall(cfg.reqfile)

sc2reqs = req.filterby(allreqs, req.Field.ProviderSC, "SC2")

filename = req.generate_report(sc2reqs, 'SC2 Progress Report', req.datemodified(cfg.reqfile), report_prefix)
print("report created: " + filename)
