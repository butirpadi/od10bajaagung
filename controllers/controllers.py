# -*- coding: utf-8 -*-
from odoo import http

# class /home/eries/odoo10/addons/bajaagung(http.Controller):
#     @http.route('//home/eries/odoo10/addons/bajaagung//home/eries/odoo10/addons/bajaagung/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/eries/odoo10/addons/bajaagung//home/eries/odoo10/addons/bajaagung/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/eries/odoo10/addons/bajaagung.listing', {
#             'root': '//home/eries/odoo10/addons/bajaagung//home/eries/odoo10/addons/bajaagung',
#             'objects': http.request.env['/home/eries/odoo10/addons/bajaagung./home/eries/odoo10/addons/bajaagung'].search([]),
#         })

#     @http.route('//home/eries/odoo10/addons/bajaagung//home/eries/odoo10/addons/bajaagung/objects/<model("/home/eries/odoo10/addons/bajaagung./home/eries/odoo10/addons/bajaagung"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/eries/odoo10/addons/bajaagung.object', {
#             'object': obj
#         })