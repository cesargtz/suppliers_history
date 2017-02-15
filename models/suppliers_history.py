# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Suppliers_History(models.Model):
    _inherit = 'res.partner'
    # _name = 'suppliers.history'

    contracts = fields.One2many('purchase.order', 'partner_id',selection="_compute_date_order")
    # date_cnt = fields.Selection(compute="_compute_date_order",
    #                        readonly=True, store=False)

    @api.returns
    @api.depends('contracts')
    def _compute_date_order(self):
        res = {}
        for record in self.contracts:
            res[record.partner_id] = str(record.date_order)
        print ("pruebas:  ", res)
        return res

# class suppliers_history(models.Model):
#     _inherit = 'res.partner'

#     history = fields.One2many('suppliers_history', 'contracts')
