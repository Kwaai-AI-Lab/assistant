"""added file table
Revision ID: 29df33c77244
Revises: f5235ab5e888
Create Date: 2024-07-24 12:49:56.947274
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '29df33c77244'
down_revision: Union[str, None] = 'f5235ab5e888'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('file',
    sa.Column('id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),    
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('assistant_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),    
    sa.Column('indexing_status', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file')