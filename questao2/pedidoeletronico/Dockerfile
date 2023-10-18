FROM python:3.12

ADD pedidoeletronico/spiders/__init__.py .
ADD pedidoeletronico/spiders/pedidoeletronico.py .
ADD pedidoeletronico/__init__.py .
ADD pedidoeletronico/items.py .
ADD pedidoeletronico/middlewares.py .
ADD pedidoeletronico/pipelines.py .
ADD pedidoeletronico/items.py .
ADD scrapy.cfg .

RUN pip install scrapy

CMD ["scrapy", "crawl", "pedidoeletronico", "-a", sys.argv[1]]