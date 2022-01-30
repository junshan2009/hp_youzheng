# Scrapy settings for ugirlsfile project

BOT_NAME = 'ugirlsfile'

SPIDER_MODULES = ['ugirlsfile.spiders']
NEWSPIDER_MODULE = 'ugirlsfile.spiders'

ROBOTSTXT_OBEY = True

SPIDER_MODULES=['ugirlsfile.spiders']
NEWSPIDER_MODULE='ugirlsfile.spiders'

ITEM_PIPELINES={
'ugirlsfile.pipelines.JiandanPipeline':1,
}

IMAGES_STORE='D://ugl'

DOWNLOAD_DELAY=0.3

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

