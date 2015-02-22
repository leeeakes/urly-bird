"""empty message

Revision ID: 5b0f3342a9
Revises: 4583dc0a6fe
Create Date: 2015-02-22 14:38:46.949568

"""

# revision identifiers, used by Alembic.
revision = '5b0f3342a9'
down_revision = '4583dc0a6fe'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('shortlink', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('shortlink'),
    sa.UniqueConstraint('url')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('links')
    ### end Alembic commands ###
