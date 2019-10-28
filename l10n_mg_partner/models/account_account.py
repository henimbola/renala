# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountAccount(models.Model):

    _inherit = 'account.account'

    capital = fields.Char(string='Capital')