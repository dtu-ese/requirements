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

import sys
sys.path.append('../lib/')
import req

file = '../Requirements.csv'

print("Loading file:", file, "(last modified:", req.datemodified(file) + ")")
allreqs = req.readall(file)

pocreqs = req.filterstartswith(allreqs, req.Field.ProviderPoC, "PoC")
nopocreqs  = req.union(req.filterby(allreqs, req.Field.ProviderPoC, ""), req.filterby(allreqs, req.Field.ProviderPoC, "not yet identified"))

print("All Reqs (Total):", len(allreqs))
print("Reqs in PoC (Total):", len(pocreqs))
print("Reqs not in PoC (Total):", len(nopocreqs))

print("All Reqs by Provider SC:", req.countby(allreqs, req.Field.ProviderSC))
print()

print("Reqs in PoC:", req.countby(pocreqs, req.Field.ProviderPoC))
print()

print("All Reqs by Lead:", req.countby(allreqs, req.Field.LeadImplementerPartner))
