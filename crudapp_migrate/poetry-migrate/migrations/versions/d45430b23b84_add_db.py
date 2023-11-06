"""add db

Revision ID: d45430b23b84
Revises: 
Create Date: 2023-11-07 02:01:42.835048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd45430b23b84'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('units',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, primary_key=True),
    sa.Column('name', sa.String(), nullable=False, unique=True),
    sa.Column('desc', sa.String(), nullable=False),
    sa.Column('photo', sa.LargeBinary(), nullable=False, default=b'\x00\x01\x02\x03'),
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, primary_key=True),
    sa.Column('username', sa.String(), nullable=False, unique=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False, default=False),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('units')
    # ### end Alembic commands ###
