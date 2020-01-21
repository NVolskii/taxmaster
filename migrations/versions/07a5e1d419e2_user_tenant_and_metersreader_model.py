"""user -> tenant and MetersReader model

Revision ID: 07a5e1d419e2
Revises: aaf2f6f384c2
Create Date: 2020-01-21 21:03:39.037951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07a5e1d419e2'
down_revision = 'aaf2f6f384c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tenant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tenantname', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tenant_email'), 'tenant', ['email'], unique=True)
    op.create_index(op.f('ix_tenant_tenantname'), 'tenant', ['tenantname'], unique=True)
    op.create_table('meters_reader',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('cold_water', sa.Float(), nullable=True),
    sa.Column('hot_water', sa.Float(), nullable=True),
    sa.Column('electricity', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['tenant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=1)
    op.create_index('ix_user_email', 'user', ['email'], unique=1)
    op.drop_table('meters_reader')
    op.drop_index(op.f('ix_tenant_tenantname'), table_name='tenant')
    op.drop_index(op.f('ix_tenant_email'), table_name='tenant')
    op.drop_table('tenant')
    # ### end Alembic commands ###