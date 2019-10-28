# -*- coding: utf-8 -*-
from odoo import http

# class Renala(http.Controller):
#     @http.route('/renala/renala/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/renala/renala/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('renala.listing', {
#             'root': '/renala/renala',
#             'objects': http.request.env['renala.renala'].search([]),
#         })

#     @http.route('/renala/renala/objects/<model("renala.renala"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('renala.object', {
#             'object': obj
#         })