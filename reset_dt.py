from flaskblog import db
from flaskblog.models import Test
db.drop_all()
db.create_all()
Test.query.all()