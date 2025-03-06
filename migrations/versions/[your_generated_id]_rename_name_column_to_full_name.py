def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='full_name')

def downgrade() -> None:
    op.alter_column('students', 'full_name', new_column_name='name')