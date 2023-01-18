"""create apt_num to address

Revision ID: 71c66a631c3c
Revises: bf5fafc22840
Create Date: 2023-01-16 10:47:45.921176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71c66a631c3c'
down_revision = 'bf5fafc22840'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('address', sa.Column('apt_num', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('address', 'apt_num')
