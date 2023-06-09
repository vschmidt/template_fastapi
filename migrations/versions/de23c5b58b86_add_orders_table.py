"""add orders table

Revision ID: de23c5b58b86
Revises: 
Create Date: 2023-03-17 09:19:07.811236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "de23c5b58b86"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("code", sa.Integer(), nullable=False),
        sa.Column("value", sa.Numeric(), nullable=False),
        sa.Column("cpf", sa.String(length=11), nullable=False),
        sa.Column("status", sa.String(length=20), nullable=True),
        sa.Column("date", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("orders")
    # ### end Alembic commands ###
