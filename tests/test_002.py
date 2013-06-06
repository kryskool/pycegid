# -*- coding: utf-8 -*-
##############################################################################
#
#    PyCEGID is a library to export datas in TRA format
#    Copyright (C) 2013 SYLEAM (<http://syleam.fr>) Christophe CHAUVET
#
#    This file is a part of PyCEGID
#
#    PyCEGID is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PyCEGID is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from pycegid.export import ExportTra, MandatoryException
import pytest


class TestSAT(object):

    def test_SAT_mandatory(self):
        try:
            tra = ExportTra()
            tra.setHeader('S5', 'CLI', 'JRL')
            tra.addSAT('PROJ1', 'Projet1')
            pytest.fail('Axe content is mandatory, missing value must be raise and error')
        except MandatoryException:
            pass

    def test_SAT_export(self):
        tra = ExportTra()
        tra.setHeader('S5', 'CLI', 'JRL')
        tra.addSAT('PROJ1', 'Projet1', 'Axe1')
        content = tra._content['lines'][0]
        assert content[:3] == '***', 'Bad starting record!'
        assert len(content) == 251, 'SAT Line in 007 format must containt 251 characters'
        assert content[248:] == 'M  ', 'Sens field must be set with M by default'

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
