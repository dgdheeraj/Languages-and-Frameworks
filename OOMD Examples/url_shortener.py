import uuid

class Url:
    def __init__(self, long_url):
        self.long_url = long_url
        self.access = 0

class UrlShortener:
    def __init__(self):
        # Key: short URL, val: Url Object
        self.all_urls = dict()
        self.short_url_format = "short.url"
        self.counter = 0
    
    def shortenUrl(self, long_url):
        ## Can you do anything better here? Maybe generate some some or unique id?
        self.counter += 1
        ## Alternative: Using UUID instead of counter, maybe take prefixes since uuid is 32 characters long
        unique_id = uuid.uuid4()
        
        short_url = f"{self.short_url_format}/{unique_id}"
        urlObj = Url(long_url)
        urlObj.short_url = short_url
        self.all_urls[short_url] = urlObj
        return short_url

    def accessUrl(self, short_url):
        if short_url not in self.all_urls:
            print("InValid Url!")
            return
        urlObj = self.all_urls[short_url]
        urlObj.access += 1
        return urlObj.long_url

    def getStats(self, short_url):
        if short_url not in self.all_urls:
            print("InValid Url!")
            return
        urlObj = self.all_urls[short_url]
        return urlObj.access
        

service = UrlShortener()
long_url1 = "sample.com/long_dir/long_path"
short_url1 = service.shortenUrl(long_url1)
print(f"{short_url1} is the short url for {long_url1}")
long_access = service.accessUrl(short_url1)
