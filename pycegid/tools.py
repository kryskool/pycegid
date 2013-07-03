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

def position(content, start, length):
    """
    Return the content start at the position X with this length

    :param content: String to extract position
    :type  content: str
    :param start: Position in the string in human representation
    :type  start: int
    :param length: Length of the record to retrieve
    :type  length: int
    """
    start -= 1  # Human representation start at position 1, but in Python it start at 0
    return content[start: start + length]

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
