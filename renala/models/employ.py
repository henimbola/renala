# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Employ(models.Model):
    _name = 'aina.affiche'

    employees_name = self.env['hr.employee'].name
