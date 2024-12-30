"""added chunk table

Revision ID: 5a1a6050b8f0
Revises: c189fb6eda90
Create Date: 2024-09-26 15:28:51.352477

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '5a1a6050b8f0'
down_revision: Union[str, None] = 'c189fb6eda90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('chunk',
        sa.Column('id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),    
        sa.Column('page_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('file_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('assistant_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),    
        sa.PrimaryKeyConstraint('id')
        )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chunk')
    # ### end Alembic commands ###