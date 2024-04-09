"""tb

Revision ID: dc04b9c23728
Revises: 
Create Date: 2024-04-09 06:50:18.215170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc04b9c23728'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('slug', sa.String(length=220), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('is_digital', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('update_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('stock_status', sa.Enum('oos', 'is', 'obo', name='status_enum'), server_default='oos', nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.CheckConstraint('LENGTH(name) > 0', name='product_name_length_check'),
    sa.CheckConstraint('LENGTH(slug) > 0', name='product_slug_length_check'),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='unq_product_name_level'),
    sa.UniqueConstraint('slug', name='unq_product_name_slug')
    )
    op.alter_column('category', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('category', 'slug',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('category', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('category', 'level',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_unique_constraint('unq_category_name_level', 'category', ['slug'])
    op.create_foreign_key(None, 'category', 'category', ['parent_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'category', type_='foreignkey')
    op.drop_constraint('unq_category_name_level', 'category', type_='unique')
    op.alter_column('category', 'level',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('category', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('category', 'slug',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('category', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.drop_table('product')
    # ### end Alembic commands ###