from models import Student, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create test database engine
engine = create_engine('sqlite:///test.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def test_student_creation():
    student = Student(full_name="Test Student")
    assert student.full_name == "Test Student"

def test_student_table_name():
    assert Student.__tablename__ == 'students'