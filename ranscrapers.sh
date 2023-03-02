#!/bin/bash
cd scrapingwebsites
scrapy crawl jobweb
sleep 10
scrapy crawl nofluffjobs_java
sleep 10
scrapy crawl nofluffjobs_NET
