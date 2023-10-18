# FROM python:3.12

# ADD pedidoeletronico/spiders/__init__.py .
# ADD pedidoeletronico/spiders/pedidoeletronico.py .
# ADD pedidoeletronico/__init__.py .
# ADD pedidoeletronico/items.py .
# ADD pedidoeletronico/middlewares.py .
# ADD pedidoeletronico/pipelines.py .
# ADD pedidoeletronico/items.py .
# ADD scrapy.cfg .

# RUN pip install scrapy

# CMD ["scrapy", "crawl", "pedidoeletronico"]

# Use an appropriate base image with Scrapy pre-installed
FROM python:3.12

# Set the working directory to your Scrapy project directory
WORKDIR /pedidoeletronico/pedidoeletronico

# Copy your Scrapy project into the container
COPY . .

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh

# Make the script executable
RUN chmod +x /entrypoint.sh

# Install any additional dependencies, if needed
RUN pip install scrapy

# Define the entrypoint script as the command to run
ENTRYPOINT ["/entrypoint.sh"]