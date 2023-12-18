"""Initial migration

Revision ID: 0cc03752867d
Revises: 7ea1a3fbb524
Create Date: 2023-12-16 02:01:32.958254

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0cc03752867d'
down_revision: Union[str, None] = '7ea1a3fbb524'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('rooms_quantity', sa.Integer(), nullable=False))
    op.drop_column('hotels', 'rooms_quanity')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('rooms_quanity', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('hotels', 'rooms_quantity')
    # ### end Alembic commands ###
