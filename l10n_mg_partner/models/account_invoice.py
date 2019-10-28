# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    payment_method = fields.Many2one('account.journal', string='Mode de payement', domain="[('type','in',['bank','cash'])]",related='company_id.payment_method')
