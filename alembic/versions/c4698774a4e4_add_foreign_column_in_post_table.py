"""add foreign column in post table

Revision ID: c4698774a4e4
Revises: d35aa55dd88b
Create Date: 2022-05-27 13:50:30.409001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4698774a4e4'
down_revision = 'd35aa55dd88b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'],
                          remote_cols=['id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint('post_users_fk'
                       , table_name='posts')
    op.drop_column('posts', 'owner_id')
