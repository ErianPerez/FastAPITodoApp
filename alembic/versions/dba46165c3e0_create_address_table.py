"""create address table

Revision ID: dba46165c3e0
Revises: e59bddf76153
Create Date: 2023-01-16 10:13:09.264036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dba46165c3e0'
down_revision = 'e59bddf76153'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String, nullable=False),
                    sa.Column('address2', sa.String, nullable=False),
                    sa.Column('city', sa.String, nullable=False),
                    sa.Column('state', sa.String, nullable=False),
                    sa.Column('country', sa.String, nullable=False),
                    sa.Column('postalcode', sa.String, nullable=False),
                    )


def downgrade() -> None:
    op.drop_table('address')
