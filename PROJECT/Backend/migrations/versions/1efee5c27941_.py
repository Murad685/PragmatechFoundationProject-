"""empty message

Revision ID: 1efee5c27941
Revises: 
Create Date: 2021-05-31 14:07:54.076225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1efee5c27941'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('about_heading',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('about_subheading', sa.String(length=255), nullable=True),
    sa.Column('about_heading', sa.String(length=255), nullable=True),
    sa.Column('about_desc', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('brand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand_imgname', sa.String(length=255), nullable=True),
    sa.Column('brand_img', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact_heading',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contact_subheding', sa.String(length=255), nullable=True),
    sa.Column('contact_heading', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customer_heading',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_subheding', sa.String(length=255), nullable=True),
    sa.Column('customer_heading', sa.String(length=255), nullable=True),
    sa.Column('customer_desc', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gallery_heading',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gallery_subheding', sa.String(length=255), nullable=True),
    sa.Column('gallery_heading', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gallery_menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gallery_menu', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news_post_heading',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('newspost_subheading', sa.String(length=255), nullable=True),
    sa.Column('newspost_heading', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('services_box',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('servicesbox_head', sa.String(length=255), nullable=True),
    sa.Column('servicesbox_desc', sa.String(length=255), nullable=True),
    sa.Column('servicesbox_url', sa.String(length=255), nullable=True),
    sa.Column('servicesbox_icon', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('services_heading',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('servicessubheading', sa.String(length=255), nullable=True),
    sa.Column('service_heading', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('services_heading')
    op.drop_table('services_box')
    op.drop_table('news_post_heading')
    op.drop_table('gallery_menu')
    op.drop_table('gallery_heading')
    op.drop_table('customer_heading')
    op.drop_table('contact_heading')
    op.drop_table('brand')
    op.drop_table('about_heading')
    # ### end Alembic commands ###