# -*- coding: utf-8 -*-

from odoo import fields, models

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    payment_method = fields.Many2one('account.journal', string='Mode de payement', domain="[('type','in',['bank','cash'])]",related='company_id.payment_method')
