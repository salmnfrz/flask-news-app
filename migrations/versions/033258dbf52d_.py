"""empty message

Revision ID: 033258dbf52d
Revises: b29c75bc4b74
Create Date: 2023-07-27 20:13:26.151474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '033258dbf52d'
down_revision = 'b29c75bc4b74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_publish', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.drop_column('date_publish')

    # ### end Alembic commands ###
