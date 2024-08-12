# -*- coding: utf-8 -*-
# from odoo import http


# class OdooLibrary(http.Controller):
#     @http.route('/odoo_library/odoo_library', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_library/odoo_library/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_library.listing', {
#             'root': '/odoo_library/odoo_library',
#             'objects': http.request.env['odoo_library.odoo_library'].search([]),
#         })

#     @http.route('/odoo_library/odoo_library/objects/<model("odoo_library.odoo_library"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_library.object', {
#             'object': obj
#         })

