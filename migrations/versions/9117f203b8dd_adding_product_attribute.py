"""adding product attribute

Revision ID: 9117f203b8dd
Revises: 70055e3854da
Create Date: 2024-04-12 06:46:29.680042

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9117f203b8dd'
down_revision: Union[str, None] = '70055e3854da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attribute_value',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('attribute_value', sa.String(length=100), nullable=False),
    sa.Column('attribute_id', sa.Integer(), nullable=True),
    sa.CheckConstraint('LENGTH(attribute_value) > 0', name='attribute_value_name_length_check'),
    sa.ForeignKeyConstraint(['attribute_id'], ['attribute.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('attribute_value', 'attribute_id', name='uq_attribute_value_attribute_id')
    )
    op.drop_constraint('uq_category_name_level', 'category', type_='unique')
    op.create_unique_constraint('uq_category_name_level', 'category', ['slug'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_category_name_level', 'category', type_='unique')
    op.create_unique_constraint('uq_category_name_level', 'category', ['name', 'level'])
    op.drop_table('attribute_value')
    # ### end Alembic commands ###