# -*- coding: utf-8 -*-

from openerp import models, fields, api



class TodoTask(models.Model):
	_inherit ='todo.two'
	user_id = fields.Many2one('res.user', 'Responsible')
	date_deadline = fields.Date('Deadline')
	name = fields.Char(help="What needs to be done?")
	@api.multi
	def do_toggle_done(self):
		for task in self:
			if task.user_id != self.env.user:
				raise ValidationError(
					'Only the responsible can do this!')

		return super(TodoTask, self).do_toggle_done()


	@api.multi
	def do_clear_done(self):
		domain = [('is_done', '=', True),
					'|',('user_id', '=',self.env.uid),
					('user_id','=',False)]
		dones = self.search(domain)
		dones.write({'active': False})
		return True