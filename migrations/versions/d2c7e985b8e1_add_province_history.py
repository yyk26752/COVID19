"""add province_history

Revision ID: d2c7e985b8e1
Revises: 
Create Date: 2020-08-30 16:17:07.384434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2c7e985b8e1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('province_history',
    sa.Column('time', sa.DATETIME(), nullable=False),
    sa.Column('province', sa.VARCHAR(length=50), nullable=True),
    sa.Column('confirm', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('time')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('province_history')
    # ### end Alembic commands ###