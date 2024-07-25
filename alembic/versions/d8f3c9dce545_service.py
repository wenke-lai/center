"""service

Revision ID: d8f3c9dce545
Revises: a9a2c6a17b8a
Create Date: 2024-07-22 09:58:53.324235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'd8f3c9dce545'
down_revision: Union[str, None] = 'a9a2c6a17b8a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('status', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('plan', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('currency', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('billing_cycle', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service')
    # ### end Alembic commands ###
