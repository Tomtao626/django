内置中间件放置的顺序：
1.SecurityMiddleware：应该放到最前面。因为这个中间件并不需要依赖任何其他的中间件。如果你的网站同时支持http协议和https协议，并且你想让用户在使用http协议的时候重定向到https协议，那么就没有必要让他执行下面一大串中间件再重定向，这样效率更高。
2.UpdateCacheMiddleware：应该在SessionMiddleware, GZipMiddleware, LocaleMiddleware之前。
3.GZipMiddleware。
4.ConditionalGetMiddleware。
5.SessionMiddleware。
6.LocaleMiddleware。
7.CommonMiddleware。
8.CsrfViewMiddleware。
9.AuthenticationMiddleware。
10.MessageMiddleware。
11.FetchFromCacheMiddleware。
12.FlatpageFallbackMiddleware。
13.RedirectFallbackMiddleware。