# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#来处理spider爬到的内容
import json


class ZimukuPipeline(object):
    def __init__(self):
        self.file = open('info.json','wb')
        self.count = 0

    def process_item(self, item, spider):
        # 只要求简单的话，
        # 我们把爬到的结果打印一下吧
        i=0
        for val in item:
            self.count += 1
            print(i+1,self.count,":",item[i])
            i +=1

        # json
        content = json.dumps(item, ensure_ascii=False) + "\n"
        self.file.write(content.encode("utf-8"))

        return item
    def close_spider(self, spider):
        self.file.close()