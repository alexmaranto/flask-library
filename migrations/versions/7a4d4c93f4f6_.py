"""empty message

Revision ID: 7a4d4c93f4f6
Revises: 
Create Date: 2023-12-30 17:49:20.985368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a4d4c93f4f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('book',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('author', sa.String(length=200), nullable=True),
    sa.Column('cover', sa.String(length=20), nullable=True),
    sa.Column('isbn', sa.String(length=200), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    op.drop_table('user')
    # ### end Alembic commands ###
