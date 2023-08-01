from flask import Blueprint,jsonify,request,render_template
from .model import db,Article,ArticleSchema

controller = Blueprint("controller",__name__)

@controller.route("/")
def index():    
    page = request.args.get("page",1,int)
    articles = db.paginate(select=db.select(Article).order_by(Article.date_publish.desc()),page=page,max_per_page=5)
    # articles = Article.query.order_by(Article.date_publish.desc()).limit(15).all()
    return render_template("index.html",articles=articles)

@controller.route("/fetch_news")
def fetch_news():
    articles = Article.query.all()
    article_schema = ArticleSchema()

    articles = article_schema.dump(articles,many=True)

    return jsonify(articles=articles)

