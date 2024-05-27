# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import timedelta

#course model
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

#student model
class SchoolStudent(models.Model):
    _name = 'school_management.student'  
    _description = 'School Student'

    name = fields.Char(string="Student Name", required=True)
    age = fields.Integer(string="Age", required=True, positive=True)
    enrolment_date = fields.Date(string="Enrolment Date", required=True, default=fields.Date.today)
    active = fields.Boolean(string="Active", default=True)
    email = fields.Char(string="Email", required=True)  # Add this line


#email reminder model
class CourseReminder(models.Model):
    _name = 'school_management.course_reminder'
    _description = 'Course Reminder'

    course_id = fields.Many2one('school_management.course', string="Course", required=True)
    student_id = fields.Many2one('school_management.student', string="Student", required=True)
    reminder_sent = fields.Boolean(string="Reminder Sent", default=False)

    @api.model
    def send_course_reminders(self):
        today = fields.Date.context_today(self)
        one_week_later = today + timedelta(days=7)
        courses = self.env['school_management.course'].search([('start_date', '=', one_week_later)])
        template = self.env.ref('school_management.email_template_course_reminder')

        for course in courses:
            for student in course.students:
                reminder = self.create({
                    'course_id': course.id,
                    'student_id': student.id,
                })
                if template:
                    self.env['mail.template'].browse(template.id).send_mail(reminder.id, force_send=True)
                reminder.reminder_sent = True

