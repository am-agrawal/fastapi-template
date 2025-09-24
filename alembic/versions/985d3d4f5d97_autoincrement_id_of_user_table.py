"""Autoincrement id of user table

Revision ID: 985d3d4f5d97
Revises: 3cb76989cb7a
Create Date: 2025-09-24 15:49:10.840351

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '985d3d4f5d97'
down_revision: Union[str, Sequence[str], None] = '3cb76989cb7a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
