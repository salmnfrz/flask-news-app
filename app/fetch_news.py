from bs4 import BeautifulSoup
from datetime import datetime
from . import app
from .source import SOURCE_LINKS
from .model import db,Article
import requests

@app.cli.command("fetch")
def fetch_news():
    """fetching news data"""

    article_arr = []
    article_dict = {}
    articles = []
 
    for link in SOURCE_LINKS:
        try:
            # print(link["source_url"])
            content = requests.get(link["source_url"])
        except requests.exceptions.ConnectionError:
            print("connection error")
        except Exception as e:
            print(e)
        else:
            html = BeautifulSoup(content.text, 'html.parser')   
            title_link_class = link["title_link_class"]
            articles = html.select(title_link_class)      
        print(articles)
 
        for article in articles:
            # print(article)
            article_dict["url"] = article["href"]
            article_dict["source"] = link["name"]
            article_dict["title"] = article.text.strip()
 
            try:            
                article = requests.get(article["href"])
            except requests.exceptions.ConnectionError:
                 print("connection error")
            except Exception as e:
                print("error,{e}")
 
            article_soup = BeautifulSoup(article.text,"html.parser")
 
            if link.get("image_wrapper_class",None):
                article_dict["image_url"] = article_soup.select_one(link["image_wrapper_class"]).img["src"]
                # print(type(article_soup.select_one(link["image_wrapper_class"]).img["src"]))
                 
            if link.get("newscategory_meta_name",None):
                category = link["newscategory_meta_name"]
                article_dict["category"] = article_soup.select_one(f"meta[name='{category}']")["content"]
 
            if link.get("publishdate_meta_name",None):
                publish_date = link["publishdate_meta_name"]
                publish_date = article_soup.select_one(f"meta[name='{publish_date}']")["content"]
                try:
                    article_dict["publish_date"] = datetime.strptime(publish_date,"%Y-%m-%d %H:%M:%S")
                except Exception as e:
                    print(e)
                    pass
 
            article_dict["description"] = article_soup.select_one("meta[name='description']")["content"]

            check_article = Article.query.filter_by(url=article_dict["url"]).first()

            if not check_article:
                _article = Article(title=article_dict["title"],source=article_dict["source"],url=article_dict["url"],image_url=article_dict["image_url"],description=article_dict.get("description"),date_publish=article_dict["publish_date"],category=article_dict["category"])
            
                try:
                    _article.add()
                except Exception as e:
                    print(e)
                    db.session.rollback()
                else:
                    print("article added")
            print("Article already added")
            # print(article_dict)
