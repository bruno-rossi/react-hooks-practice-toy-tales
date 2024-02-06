"""empty message

Revision ID: 43bd45e5962a
Revises: 
Create Date: 2024-02-06 13:45:54.367436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43bd45e5962a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('toys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_toys'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('toys')
    # ### end Alembic commands ###
