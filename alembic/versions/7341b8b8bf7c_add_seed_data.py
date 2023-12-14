"""Add seed data

Revision ID: 7341b8b8bf7c
Revises: 329a56d8811f
Create Date: 2023-12-13 18:07:43.534163

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import String, Text


# revision identifiers, used by Alembic.
revision: str = '7341b8b8bf7c'
down_revision: Union[str, None] = '329a56d8811f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ad-hoc table for the insert statement
    users_table = table('users',
                        column('username', String),
                        column('email', String),
                        column('bio', Text),
                        column('hashed_password', String),
                        )

    # insert data
    op.bulk_insert(users_table,
                   [
                       {
                           'username': 'john_doe',
                           'email': 'johndoe@gmail.com',
                           'bio': 'I am a Data Science student looking for new connections!',
                           'hashed_password': 'hashed_password_1'
                       },
                       {
                           'username': 'jane_smith',
                           'email': 'janesmith@example.com',
                           'bio': 'Aspiring web developer and tech enthusiast.',
                           'hashed_password': 'hashed_password_2'
                       },
                       {
                           'username': 'alex_jones',
                           'email': 'alexjones@example.com',
                           'bio': 'Full-stack developer and open-source contributor.',
                           'hashed_password': 'hashed_password_3'
                       },
                       {
                           'username': 'emily_white',
                           'email': 'emilywhite@example.com',
                           'bio': 'UI/UX designer with a passion for user-centric design.',
                           'hashed_password': 'hashed_password_4'
                       },
                       {
                           'username': 'michael_brown',
                           'email': 'michaelbrown@example.com',
                           'bio': 'Tech blogger and hardware reviewer.',
                           'hashed_password': 'hashed_password_5'
                       },
                       {
                           'username': 'sarah_lee',
                           'email': 'sarahlee@example.com',
                           'bio': 'Cloud engineer focusing on AWS solutions.',
                           'hashed_password': 'hashed_password_6'
                       },
                       {
                           'username': 'david_johnson',
                           'email': 'davidjohnson@example.com',
                           'bio': 'Data analyst in a fintech company.',
                           'hashed_password': 'hashed_password_7'
                       }
                   ])


def downgrade() -> None:
    pass
