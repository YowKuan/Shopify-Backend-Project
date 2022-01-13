"""empty message

Revision ID: fa3dc841a5ea
Revises: c9c02fcb3267
Create Date: 2022-01-13 11:57:15.298930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa3dc841a5ea'
down_revision = 'c9c02fcb3267'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('warehouse', sa.Column('created_time', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('warehouse', 'created_time')
    # ### end Alembic commands ###
