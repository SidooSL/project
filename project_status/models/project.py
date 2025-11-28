from odoo import SUPERUSER_ID, fields, models


class Project(models.Model):
    _inherit = "project.project"

    @staticmethod
    def _read_group_status_ids(self, groups, domain):
        status_ids = (
            self.env["project.status"].with_user(SUPERUSER_ID)._search([])
        )
        return self.env["project.status"].browse(status_ids)

    project_status = fields.Many2one(
        comodel_name="project.status",
        group_expand="_read_group_status_ids",
        copy=False,
        ondelete="restrict",
        index=True,
    )
