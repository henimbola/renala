# -*- coding: utf-8 -*-

from odoo import fields, models

class ResCompany(models.Model):

    _inherit = 'res.company'

    nif = fields.Char(string = 'NIF', related = 'partner_id.nif',store=True)
    nstat = fields.Char(string = 'Num STAT', related = 'partner_id.nstat',store=True)
    rcs = fields.Char(string = 'Imm. RCS', related = 'partner_id.rcs',store=True)
    cif = fields.Char(string = 'Num CIF', related = 'partner_id.cif',store=True)
    siret = fields.Char(string='SIRET', related = 'partner_id.siret',store=True)
    ntva = fields.Char(string='N° TVA', related = 'partner_id.ntva',store=True)
    payment_method = fields.Many2one('account.journal', string = 'Mode de payement', domain = "[('type','in',['bank','cash'])]")
    account_id = fields.Many2one('account.account')
    capital = fields.Char(string = 'Capital',related = 'account_id.capital',store=True)