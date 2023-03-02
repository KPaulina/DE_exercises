#!/bin/bash
cd scrapingwebsites
scrapy crawl nofluffjobs_python
sleep 10
scrapy crawl nofluffjobs_java
sleep 10
scrapy crawl nofluffjobs_NET
