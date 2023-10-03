"""Initial migration.

Revision ID: 745463ee6de5
Revises: 
Create Date: 2023-10-03 10:35:08.957682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '745463ee6de5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('productions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('budget', sa.Float(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('director', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('ongoing', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productions')
    # ### end Alembic commands ###
