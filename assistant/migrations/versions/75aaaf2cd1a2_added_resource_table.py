"""Added resource table

Revision ID: 75aaaf2cd1a2
Revises: 56a640fb45b2
Create Date: 2024-05-07 21:48:08.883504

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '75aaaf2cd1a2'
down_revision: Union[str, None] = '56a640fb45b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('resource',
    sa.Column('id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('uri', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('resource_llm_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('persona_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('status', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('allow_edit', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('kind', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('icon', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('active', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('user_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),    
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('resource')
