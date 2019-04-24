"""d migrate

Revision ID: f11325aecf8e
Revises: 9f2a8670cdf6
Create Date: 2019-04-24 09:46:24.326171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f11325aecf8e'
down_revision = '9f2a8670cdf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'pitch_statement')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch_statement', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###