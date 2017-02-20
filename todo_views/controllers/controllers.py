# -*- coding: utf-8 -*-
from openerp import http

# class TodoViews(http.Controller):
#     @http.route('/todo_views/todo_views/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_views/todo_views/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_views.listing', {
#             'root': '/todo_views/todo_views',
#             'objects': http.request.env['todo_views.todo_views'].search([]),
#         })

#     @http.route('/todo_views/todo_views/objects/<model("todo_views.todo_views"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_views.object', {
#             'object': obj
#         })