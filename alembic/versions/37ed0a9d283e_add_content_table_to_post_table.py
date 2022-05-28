"""add content table to post table

Revision ID: 37ed0a9d283e
Revises: c1ba624cd479
Create Date: 2022-05-27 13:23:31.388864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37ed0a9d283e'
down_revision = 'c1ba624cd479'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
