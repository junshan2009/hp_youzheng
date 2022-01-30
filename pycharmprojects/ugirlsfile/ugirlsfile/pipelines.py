# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
from ugirlsfile import settings

class JiandanPipeline(object):
    def process_item(self, item, spider):
        fold_name = "".join(item['title'])
        header = {
            'USER-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Cookie': 'b963ef2d97e050aaf90fd5fab8e78633',
        }
        images = []
        # 所有图片放在一个文件夹下
        dir_path = '{}'.format(settings.IMAGES_STORE)
        if not os.path.exists(dir_path) and len(item['title']) != 0:
            os.mkdir(dir_path)
        if len(item['title']) == 0:
            with open('check.txt', 'a+') as fp:
                fp.write("".join(item['title']))
                fp.write("\n")

        for jpg_url, num in zip(item['title'], range(0, 100)):
            file_name = str(num)
            file_path = '{}//{}'.format(dir_path, file_name)
            images.append(file_path)
            if os.path.exists(file_path) or os.path.exists(file_name):
                continue

            with open('{}//{}.jpg'.format(dir_path, file_name), 'wb') as f:
                req = requests.get(jpg_url, headers=header)
                f.write(req.content)

        return item

