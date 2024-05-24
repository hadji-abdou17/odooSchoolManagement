# -*- coding: utf-8 -*-

from . import models  # Import models.py
from . import views  # Import views.xml
from . import controllers  # (Optional) Import controllers.py if you have one

def pre_init_check(cr):
  from odoo.service import security_model
  security_model.check_hr_holidays_module()

def register(cr):
  from odoo.addons.base.models.ir_ui_view import custom_view
  custom_view([
      ('school_management.course.tree', 'tree'),
      ('school_management.course.form', 'form'),
      ('school_management.student.tree', 'tree'),
      ('school_management.student.form', 'form'),
  ])