"""empty message

Revision ID: 5db2f37b75ca
Revises: cc2b2a8efebc
Create Date: 2023-07-27 16:54:37.003842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5db2f37b75ca'
down_revision = 'cc2b2a8efebc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_publish', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('category', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.drop_column('category')
        batch_op.drop_column('date_publish')

    # ### end Alembic commands ###