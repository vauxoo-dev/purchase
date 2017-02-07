# coding: utf-8
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) Vauxoo (<http://vauxoo.com>).
#    All Rights Reserved
# #############Credits#########################################################
#    Coded by: Jose Suniaga <josemiguel@vauxoo.com>
###############################################################################
#    This program is free software: you can redistribute it and/or modify it
#    under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or (at your
#    option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
from datetime import datetime

from odoo import models, api


class PurchaseQuotationReportXLS(models.AbstractModel):
    _name = 'report.purchase_rfq_xls.report_template'

    @api.multi
    def render_html(self, docids, data=None):
        print data
        docargs = {
            'doc_ids': docids,
            'doc_model': 'purchase.order',
            'docs': self.env['purchase.order'].browse(docids),
            'data': data,
            'datetime': datetime,
        }
        return self.env['report'].render(
            'purchase_rfq_xls.report_template', docargs)
