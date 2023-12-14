"""Seed tags table

Revision ID: 32824b306005
Revises: 9b913603a42c
Create Date: 2023-12-14 20:28:31.842605

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import String
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision: str = '32824b306005'
down_revision: Union[str, None] = '9b913603a42c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ad-hoc table for the insert statement
    tags_table = table('tags',
                        column('title', String),
                        )

    # insert data
    op.bulk_insert(tags_table,
                   [
                       {"title": "Software Development"},
                       {"title": "Computer Science"},
                       {"title": "Bioengineering"},
                       {"title": "Medicine"},
                       {"title": "Law"},
                       {"title": "Machine Learning"},
                       {"title": "Data Science"},
                       {"title": "Cloud Computing"},
                       {"title": "DevOps"},
                       {"title": "USMLE"},
                       {"title": "AWS"},
                   ])


def downgrade() -> None:
    pass
