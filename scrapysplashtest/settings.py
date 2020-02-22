BOT_NAME = 'scrapysplashtest'

SPIDER_MODULES = ['scrapysplashtest.spiders']
NEWSPIDER_MODULE = 'scrapysplashtest.spiders'

#Splash服务器地址
SPLASH_URL = 'http://192.168.3.40:8050'

#开启Splash的两个下载中间件并调整HttpCompressionMiddleware的次序
DOWNLOADER_MIDDLEWARES = {
    'scrapysplashtest.middlewares.RandomUserAgent':345,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
#设置去重过滤器
DUPEFILTER_CLASS='scrapy_splash.SplashAwareDupeFilter'

#用来支持cache_args
SPIDER_MIDDLEWARES ={
    'scrapy_splash.SplashDeduplicateArgsMiddleware':100,
}
# 使用Splash的Http缓存
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

COOKIES_ENABLED = False
DOWNLOAD_DELAY = 3
LOG_LEVEL = "WARNING"
ITEM_PIPELINES = {
    # 'splash_examples.pipelines.SplashExamplesPipeline':400,
    # 'splash_examples.pipelines.MysqlPipeline':543,
}

# MYSQL_HOST = 'localhost'
# MYSQL_DATABASE = 'pybooks'
# MYSQL_PORT = 3306
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = 'root'
