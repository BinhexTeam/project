# Copyright 2024 Binhex - Adasat Torres de León
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = "project.task"

    repeat_start = fields.Date("Start Recurrence Date", default=fields.Date.today)
    allow_repeat_start = fields.Boolean("Allow Start Recurrence Date", default=False)

    def _get_recurrence_start_date(self):
        self.ensure_one()
        if self.allow_repeat_start:
            return self.repeat_start
        return super()._get_recurrence_start_date()

    @api.depends(
        "recurring_task",
        "repeat_interval",
        "repeat_unit",
        "repeat_type",
        "repeat_until",
        "repeat_number",
        "repeat_on_month",
        "repeat_on_year",
        "mon",
        "tue",
        "wed",
        "thu",
        "fri",
        "sat",
        "sun",
        "repeat_day",
        "repeat_week",
        "repeat_month",
        "repeat_weekday",
        "repeat_start",
        "allow_repeat_start",
    )
    def _compute_recurrence_message(self):
        super()._compute_recurrence_message()
