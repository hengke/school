"""empty message

Revision ID: 21faca184eb4
Revises: 99e0a65ba0ba
Create Date: 2018-03-03 15:32:10.136410

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '21faca184eb4'
down_revision = '99e0a65ba0ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('charge_teacher', 'users',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('classesd', 'charge_teachers',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('classesd', 'grades',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('classesd', 'students',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('doorkeepers', 'users',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('grades', 'schools',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('students', 'users',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.drop_constraint(u'users_ibfk_1', 'users', type_='foreignkey')
    op.drop_column('users', 'role')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.create_foreign_key(u'users_ibfk_1', 'users', 'roles', ['role'], ['id'])
    op.alter_column('students', 'users',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('grades', 'schools',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('doorkeepers', 'users',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('classesd', 'students',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('classesd', 'grades',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('classesd', 'charge_teachers',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('charge_teacher', 'users',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    # ### end Alembic commands ###
