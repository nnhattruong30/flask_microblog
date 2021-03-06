"""add language to posts

Revision ID: 7320e8daf0ff
Revises: ed62535654cf
Create Date: 2021-05-10 21:36:48.119503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7320e8daf0ff'
down_revision = 'ed62535654cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
