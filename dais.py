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

print("Loading file:", cfg.reqfile, "(last modified:", req.datemodified(cfg.reqfile) + ")")
allreqs = req.readall(cfg.reqfile)

pocreqs = req.filterstartswith(allreqs, req.Field.ProviderPoC, "PoC")
nopocreqs  = req.union(req.filterby(allreqs, req.Field.ProviderPoC, ""), req.filterby(allreqs, req.Field.ProviderPoC, "not yet identified"))

print("All Reqs (Total):", len(allreqs))
print("Reqs in PoC (Total):", len(pocreqs))
print("Reqs not in PoC (Total):", len(nopocreqs))

count = req.countby(allreqs, req.Field.ProviderSC)
req.plot_counter(count, "DAIS-All-Reqs.pdf")
print("All Reqs by Provider SC:", count)
print()

print("Reqs in PoC:", req.countby(pocreqs, req.Field.ProviderPoC))
print()

print("All Reqs by Lead:", req.countby(allreqs, req.Field.LeadImplementerPartner))
