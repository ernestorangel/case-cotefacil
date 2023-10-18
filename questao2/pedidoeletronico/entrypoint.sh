#!/bin/sh
ARG_VALUE="$1"
scrapy crawl pedidoeletronico -a order=$ARG_VALUE