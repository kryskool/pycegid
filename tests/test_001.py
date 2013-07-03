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
from pycegid.tools import position
import time
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
        tra.setHeader('S5', 'CLI', 'JRL', num_dossier='B105ZZ')
        content = tra.render()
        assert position(content, 1, 3) == '***', 'Bad starting record!'
        assert position(content, 4, 2) == 'S5', 'Bad identifiant!'
        assert position(content, 18, 8) == '01011900', 'Default date for "Date Bacule" not found!'
        assert position(content, 26, 8) == '01011900', 'Default date for "Date arrete periodique" not found!'
        assert position(content, 34, 3) == '007'
        assert position(content, 37, 5) == '     '
        assert position(content, 42, 8) == time.strftime('%d%m%Y')
        assert position(content, 128, 6) == 'B105ZZ'
        assert position(content, 145, 3) == '001'
        assert len(content.replace('\r\n', '')) == 147, 'Record length not valid (%d)' % len(content)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
