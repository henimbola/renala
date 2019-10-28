# -*- coding: utf-8 -*-

from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    ref1 = fields.Char(string='Ref/Code 1', index=True)
    ref2 = fields.Char(string='Ref/Code 2', index=True)
    nif = fields.Char(string='NIF', index=True)
    nstat = fields.Char(string='Num STAT', index=True)

    # historisable dans une future version
    cif = fields.Char(string='Num CIF', index=True)
    dcif = fields.Date(string='Date CIF')

    # registre de commerce
    rcs = fields.Char(string='Imm. RCS', index=True)
    drcs = fields.Date(string='Date RCS')

    # scan signature
    signature_img = fields.Binary('Signature scannee')
    partner_origin = fields.Selection([('locale','Locale'), ('etrangere','Etrangère')], string='Origine', default='locale', required=True)

    ntva = fields.Char(string ='N° TVA', index = True)
    siret = fields.Char(string ='SIRET', index = True)
    


class Company(models.Model):

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


class Sale(models.Model):

    _inherit = 'sale.order'

    payment_method = fields.Many2one('account.journal', string='Mode de payement', domain="[('type','in',['bank','cash'])]",related='company_id.payment_method')


class Account(models.Model):

    _inherit = 'account.invoice'

    payment_method = fields.Many2one('account.journal', string='Mode de payement', domain="[('type','in',['bank','cash'])]",related='company_id.payment_method')


class Account_account(models.Model):

    _inherit = 'account.account'

    capital = fields.Char(string='Capital')