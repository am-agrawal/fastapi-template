"""Autoincrement id in all tables

Revision ID: 49d74b505a0c
Revises: 985d3d4f5d97
Create Date: 2025-09-24 15:54:42.326052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49d74b505a0c'
down_revision: Union[str, Sequence[str], None] = '985d3d4f5d97'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
