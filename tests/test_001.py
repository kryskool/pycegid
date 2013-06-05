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

class TestExport1(object):

    def test_debug(self):
        tra = ExportTra()
        tra.setDebug(200)
        assert tra._debug_header == 200, 'Bad debug header length'

    def test_format_1(self):
        tra = ExportTra()
        content = tra._format('OK', 10)
        assert len(content) == 10
        assert content[:2] == 'OK', "Content doesn't start with OK!"

    def test_format_2(self):
        tra = ExportTra()
        content = tra._format('OK', 10, True)
        assert len(content) == 10
        assert content[8:] == 'OK', "Content doesn't end with OK!"

    def test_format_3(self):
        tra = ExportTra()
        content = tra._format('OK', 10, caract='=')
        assert len(content) == 10
        assert content == 'OK========'

    def test_format_4(self):
        tra = ExportTra()
        content = tra._format('OK', 10, True, caract='=')
        assert len(content) == 10
        assert content == '========OK'

    def test_mandatory_standard(self):
        tra = ExportTra()
        content = tra._mandatory('OK', 10)
        assert len(content) == 10

    def test_mandatory_exception(self):
        """Raise an error when the content is empty"""
        try:
            tra = ExportTra()
            tra._mandatory('', 10)
            pytest.fail('An empty content mandatory must raise and error')
        except MandatoryException:
            pass

    def test_header(self):
        tra = ExportTra()
        tra.setHeader('S5', 'CLI', 'JRL')
        content = tra.render()
        assert content[:3] == '***', 'Bad starting record!'
        assert content[3:5] == 'S5', 'Bad identifiant!'
        assert content[17:25] == '01011900', 'Default date for "Date Bacule" not found!'
        assert content[25:33] == '01011900', 'Default date for "Date arrete periodique" not found!'
        #assert len(content) == 148, 'Record length not valid (%d)' % len(content)

    def test_SAT(self):
        tra = ExportTra()
        tra.setHeader('S5', 'CLI', 'JRL')
        tra.addSAT('PROJ1', 'Projet1')
        content = tra._content['lines'][0]
        assert content[:3] == '***', 'Bad starting record!'

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
