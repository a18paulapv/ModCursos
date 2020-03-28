# -*- coding: utf-8 -*-

import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
from datetime import datetime, timedelta, date


logger = logging.getLogger(__name__)

class CoursesCourse(models.Model):
    _name = 'courses.course'
    _description='Courses Course'

    name = fields.Char('Name', required=True)
    acronyms=fields.Char('Acronyms')
    level=fields.Integer('Level', required=True, default=1)
    teach_ids=fields.One2many('courses.teaching', inverse_name='course_id')
    


class CoursesStudent(models.Model):
    _name='courses.student'
    _description='Courses Student'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    date_start = fields.Date('Student Since', default=lambda*a:datetime.now().strftime('%Y-%m-%d'))
    student_phone = fields.Char()
    date_birth = fields.Date('Date of birth')
    photo = fields.Binary('Photo', related='partner_id.image')
    age=fields.Integer('Age', compute='check_age', store=False)
    is_assigned=fields.Boolean('Assigned', compute='check_assigned', default=False)
    state = fields.Selection([
        ('unavailable', 'Locked'),
        ('available', 'Available')],
        'State', default="available")


    @api.multi
    def check_age(self):
        nac = self.date_birth
        hoy = date.today()
        cumple = self.date_birth.replace(year=hoy.year)
        if cumple > hoy:          
            self.age = hoy.year - nac.year - 1 
        else: 
            self.age = hoy.year - nac.year 
        return

    @api.multi    
    def check_assigned(self):
        for record in self:
            domain = [
                '&', 
                ('student_id.id', '=', record.id), 
                ('date_end', '>=', datetime.now())
            ]
            record.is_assigned= self.env['courses.teaching'].search(domain, count=True)>0


    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('unavailable', 'available'),
                   ('available', 'unavailable')]
        return (old_state, new_state) in allowed

    @api.multi
    def change_state(self, new_state):
        for student in self:
            if student.is_allowed_transition(student.state, new_state):
                student.state = new_state
            else:
                message = _('Moving from %s to %s is not allowed') % (student.state, new_state)
                raise UserError(message)

    def make_available(self):
        self.change_state('available')

    def make_unavailable(self):
        self.change_state('unavailable')

class CoursesTeaching(models.Model):
    _name='courses.teaching'
    _description='Courses Teaching'
    _rec_name='course_id'

    student_id=fields.Many2one('courses.student', required=True)
    course_id=fields.Many2one('courses.course', required=True)
    date_start=fields.Date('Start date of the course', default=lambda*a:datetime.now().strftime('%Y-%m-%d'))
    date_end=fields.Date('End date of the course', default=lambda*a:(datetime.now()+timedelta(days=(270))).strftime('%Y-%m-%d'))
    student_photo=fields.Binary('Student Photo', related='student_id.photo')
    course_level=fields.Integer('Level', related='course_id.level')


    @api.constrains('date_start', 'date_end')
    def _check_date(self):
        for record in self:
                if record.date_start > record.date_end:
                    raise models.ValidationError('Start date Afer end date!')    

    @api.constrains('student_id')
    def _check_student_id(self):
        for record in self:
            student = record.student_id
            domain = [
                '&',
                ('student_id.id', '=', student.id),
                ('date_end', '>=', datetime.now())
            ]
            student.is_assigned = self.search(domain, count=True) > 1
            if student.is_assigned:
                raise models.ValidationError('This Student is Assigned with other course!')

