# -*- coding: utf-8 -*-
from odoo import http

# class MyCourses(http.Controller):
#     @http.route('/my_courses/my_courses/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_courses/my_courses/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_courses.listing', {
#             'root': '/my_courses/my_courses',
#             'objects': http.request.env['my_courses.my_courses'].search([]),
#         })

#     @http.route('/my_courses/my_courses/objects/<model("my_courses.my_courses"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_courses.object', {
#             'object': obj
#         })