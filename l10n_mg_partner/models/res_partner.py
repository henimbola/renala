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
