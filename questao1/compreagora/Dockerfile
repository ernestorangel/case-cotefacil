FROM python:3.12

ADD compreagora/spiders/__init__.py .
ADD compreagora/spiders/products.py .
ADD compreagora/__init__.py .
ADD compreagora/items.py .
ADD compreagora/middlewares.py .
ADD compreagora/pipelines.py .
ADD compreagora/items.py .
ADD scrapy.cfg .

RUN pip install scrapy

CMD ["scrapy", "crawl", "products"]