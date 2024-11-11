# Copyright 2024 Binhex - Adasat Torres de León
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo.tests.common import TransactionCase, Form
from odoo.tests import tagged
from freezegun import freeze_time
from datetime import date


@tagged("post_install", "-at_install")
class TestProjectTask(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.project = cls.env["project.project"].create({"name": "Test Project"})

    def test_recurrence_date_start(self):
        with freeze_time("2024-11-11"):
            with Form(self.env["project.task"]) as task_form:
                task_form.name = "Test Task"
                task_form.project_id = self.project
                task_form.recurring_task = True
                task_form.repeat_interval = 1
                task_form.repeat_unit = "day"
                task_form.allow_repeat_start = True
                task_form.repeat_start = date(2024, 11, 14)
                task_form.repeat_type = "until"
                task_form.repeat_until = date(2024, 11, 18)
            task = task_form.save()
            task._compute_recurrence_message()

            self.assertTrue(bool(task.recurrence_id))
            self.assertEqual(
                task.recurrence_id.next_recurrence_date, date(2024, 11, 12)
            )
