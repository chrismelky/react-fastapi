"""Create user table

Revision ID: a91259e88e9d
Revises: 
Create Date: 2022-07-13 12:48:19.809515

"""
from enum import unique
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a91259e88e9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('first_name', sa.String(200), nullable=True),
        sa.Column('last_name', sa.String(200), nullable=True),
        sa.Column('email', sa.String(200), nullable=False),
        sa.Column('password_hash', sa.String, nullable=False),
        sa.Column('is_active', sa.Boolean(), default=True)
    )
    op.create_index(op.f('idx_unique_email'), 'users', ['email'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('idx_unique_email'), table_name='users')
    op.drop_table('users')
