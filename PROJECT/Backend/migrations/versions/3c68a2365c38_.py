"""empty message

Revision ID: 3c68a2365c38
Revises: 3cd74a6ef160
Create Date: 2021-06-01 14:28:03.218814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c68a2365c38'
down_revision = '3cd74a6ef160'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('client_box')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client_box',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('client_name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('client_status', sa.VARCHAR(length=255), nullable=True),
    sa.Column('client_desc', sa.VARCHAR(length=255), nullable=True),
    sa.Column('client_img', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
