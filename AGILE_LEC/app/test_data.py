from app import db
from app.model import *

# Delete any existing students with these uwa_id values
uwa_ids = ['12345678', '87654321', '12348765', '87654323']
Student.query.filter(Student.uwa_id.in_(uwa_ids)).delete(synchronize_session=False)

group1 = Group()

tom = Student(uwa_id='12345678', name='Tom')
jerry = Student(uwa_id='87654321', name='Jerry')
cardi = Student(uwa_id='12348765', name='Cardi')
talor = Student(uwa_id='87654323', name='Talor')

db.session.add_all([group1, tom, jerry, cardi, talor])
db.session.commit()