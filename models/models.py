# -*- coding: utf-8 -*-

from openerp import models, fields, api



class TodoUser(models.Model):
	_inherit ='todo.two'
	user_id = fields.Many2one('res.user', 'Responsible')
	date_deadline = fields.Date('Deadline')
	name = fields.Char(help="What needs to be done?")