"""Revision ID: 0
Revises: 
"""

# revision identifiers, used by Alembic.
revision = '0'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('test',
        sa.Column('id', sa.Integer(), primary_key=True)
        )

def downgrade():
    op.drop_table('test')
