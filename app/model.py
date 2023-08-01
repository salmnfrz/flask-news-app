from . import db
from . import marshmallow

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50),nullable=False,default="")
    source = db.Column(db.String(50),nullable=False)
    url = db.Column(db.String(5000),nullable=False)
    image_url = db.Column(db.String(5000),nullable=False)
    date_publish = db.Column(db.DateTime)
    category = db.Column(db.String(50),default="")
    description = db.Column(db.String(50),nullable=False)

    def __init__(self,title,source,url,image_url,description="",date_publish="",category=""):
        self.title = title
        self.source = source
        self.url = url
        self.image_url = image_url
        self.description = description
        self.date_publish = date_publish
        self.category = category

    def add(self):
        db.session.add(self)
        db.session.commit()

class ArticleSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Article
        include_fk = True














