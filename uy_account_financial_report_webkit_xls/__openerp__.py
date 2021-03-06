# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Enterprise Management Solution
#    GRP Estado Uruguay
#    Copyright (C) 2017 Quanam (ATEL SA., Uruguay)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Inherit Account Financial Report Webkit',
    'version': '1.0',
    'category': 'Accounting & Finance',
    'author': 'Quanam',
    'website':  'http://www.quanam.com',
    'description': """

    """,
    'depends': ['account_financial_report_webkit_xls'],
    'data': [
       'wizard/balance_partner_wizard_view.xml',
       'wizard/partners_ledger_wizard_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
