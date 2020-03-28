# -*- coding: utf-8 -*-
{
    'name': "My Courses",

    'summary': "Manage your courses easily",

    'description': "Mange your courses and your studens with a perfect organization and without errors",

    'author': "Paula Paz",
    'website': "http://www.yourcourses.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/courses_course.xml',
        'views/courses_student.xml',
        'views/courses_teaching.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}