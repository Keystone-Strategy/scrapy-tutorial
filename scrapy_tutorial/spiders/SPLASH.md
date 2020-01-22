## This is taken directly from https://github.com/scrapy-plugins/scrapy-splash/blob/master/README.rst This are the previous steps to configure the usage of splash intoon the project, just changed the URL to use the splash server from kslabs.

Configuration
=============

1. Add the Splash server address to ``settings.py`` of your Scrapy project
   like this::

      SPLASH_URL = 'https://kslabs-scrapy-splash.herokuapp.com/'

2. Enable the Splash middleware by adding it to ``DOWNLOADER_MIDDLEWARES``
   in your ``settings.py`` file and changing HttpCompressionMiddleware
   priority::

      DOWNLOADER_MIDDLEWARES = {
          'scrapy_splash.SplashCookiesMiddleware': 723,
          'scrapy_splash.SplashMiddleware': 725,
          'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
      }

   Order `723` is just before `HttpProxyMiddleware` (750) in default
   scrapy settings.

   HttpCompressionMiddleware priority should be changed in order to allow
   advanced response processing; see https://github.com/scrapy/scrapy/issues/1895
   for details.

3. Enable ``SplashDeduplicateArgsMiddleware`` by adding it to
   ``SPIDER_MIDDLEWARES`` in your ``settings.py``::

      SPIDER_MIDDLEWARES = {
          'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
      }

   This middleware is needed to support ``cache_args`` feature; it allows
   to save disk space by not storing duplicate Splash arguments multiple
   times in a disk request queue. If Splash 2.1+ is used the middleware
   also allows to save network traffic by not sending these duplicate
   arguments to Splash server multiple times.

4. Set a custom ``DUPEFILTER_CLASS``::

      DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

5. If you use Scrapy HTTP cache then a custom cache storage backend
   is required. scrapy-splash provides a subclass of
   ``scrapy.contrib.httpcache.FilesystemCacheStorage``::

      HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

   If you use other cache storage then it is necesary to subclass it and
   replace all ``scrapy.util.request.request_fingerprint`` calls with
   ``scrapy_splash.splash_request_fingerprint``.

.. note::

    Steps (4) and (5) are necessary because Scrapy doesn't provide a way
    to override request fingerprints calculation algorithm globally; this
    could change in future.


There are also some additional options available.
Put them into your ``settings.py`` if you want to change the defaults:

* ``SPLASH_COOKIES_DEBUG`` is ``False`` by default.
  Set to ``True`` to enable debugging cookies in the ``SplashCookiesMiddleware``.
  This option is similar to ``COOKIES_DEBUG``
  for the built-in scarpy cookies middleware: it logs sent and received cookies
  for all requests.
* ``SPLASH_LOG_400`` is ``True`` by default - it instructs to log all 400 errors
  from Splash. They are important because they show errors occurred
  when executing the Splash script. Set it to ``False`` to disable this logging.
* ``SPLASH_SLOT_POLICY`` is ``scrapy_splash.SlotPolicy.PER_DOMAIN`` (as object, not just a string) by default.
  It specifies how concurrency & politeness are maintained for Splash requests,
  and specify the default value for ``slot_policy`` argument for
  ``SplashRequest``, which is described below.