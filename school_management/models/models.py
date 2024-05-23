# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions

class SchoolCourse(models.Model):
    _name = 'school_management.course'  
    _description = 'School Course'

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text(string="Description")
    course_code = fields.Char(string="Course Code", required=True, unique=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    students = fields.Many2many('school_management.student', string="Students")

    @api.constrains('start_date', 'end_date')
    def _check_end_date_after_start_date(self):
        for record in self:
            if record.start_date and record.end_date and record.start_date > record.end_date:
                raise exceptions.ValidationError("End Date must be after Start Date!")

class SchoolStudent(models.Model):
    _name = 'school_management.student'  
    _description = 'School Student'

    name = fields.Char(string="Student Name", required=True)
    age = fields.Integer(string="Age", required=True, positive=True)
    enrolment_date = fields.Date(string="Enrolment Date", required=True, default=fields.Date.today)
    active = fields.Boolean(string="Active", default=True)
