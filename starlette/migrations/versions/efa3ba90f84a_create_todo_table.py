"""Create todo table

Revision ID: efa3ba90f84a
Revises: 411f808ca6d4
Create Date: 2021-01-09 13:42:54.440071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "efa3ba90f84a"
down_revision = "411f808ca6d4"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "todo",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(), index=True),
        sa.Column("description", sa.Text(), index=True),
        sa.Column("author_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("created_on", sa.DateTime(timezone=True)),
        sa.Column("modified_on", sa.DateTime(timezone=True), nullable=True),
    )


def downgrade():
    op.drop_table("todo")
