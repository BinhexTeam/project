# Copyright 2025 Binhex - Zuzanna Elzbieta Szalaty Szalaty
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"
    project_id = fields.Many2one(
        comodel_name="project.project",
        string="Project",
        company_dependent=True,
        help="Select a billable project on which tasks can be created."
        " This setting must be set for each company.",
        domain="[('company_id', '=', current_company_id),"
        " ('allow_billable', '=', True), ('pricing_type', '=', 'task_rate'),"
        " ('allow_timesheets', 'in', "
        "[service_policy == 'delivered_timesheet', True])]",
    )
    project_template_id = fields.Many2one(
        comodel_name="project.project",
        string="Project Template",
        company_dependent=True,
        copy=True,
        help="Select a billable project to be the skeleton of"
        " the new created project when selling the current product."
        " Its stages and tasks will be duplicated.",
        domain="[('company_id', '=', current_company_id),"
        " ('allow_billable', '=', True), ('allow_timesheets',"
        " 'in', [service_policy == 'delivered_timesheet', True])]",
    )
