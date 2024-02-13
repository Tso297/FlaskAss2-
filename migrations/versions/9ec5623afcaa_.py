"""empty message

Revision ID: 9ec5623afcaa
Revises: ff0a9b854e5e
Create Date: 2024-02-13 14:28:03.179719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ec5623afcaa'
down_revision = 'ff0a9b854e5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car__dealership',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('contact')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('user_token', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], name='contact_user_token_fkey'),
    sa.PrimaryKeyConstraint('id', name='contact_pkey')
    )
    op.drop_table('car__dealership')
    # ### end Alembic commands ###
