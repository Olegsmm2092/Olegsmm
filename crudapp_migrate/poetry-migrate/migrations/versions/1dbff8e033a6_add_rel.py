"""add rel

Revision ID: 1dbff8e033a6
Revises: d45430b23b84
Create Date: 2023-11-07 02:20:33.763552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dbff8e033a6'
down_revision = 'd45430b23b84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('units')

    op.create_table('units',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, primary_key=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.Column('desc', sa.String(), nullable=False),
        sa.Column('photo', sa.LargeBinary(), nullable=False, default=b'\x00\x01\x02\x03'),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),  # Foreign key column
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('units')