Note for myself

# Operating Environment
- macOS Mojave 10.14
- Python 3.6.8
- flickapi 2.4

# Preparation
Get flickr API key & install library(flickapi) [Link](http://ykubot.com/2017/11/05/flickr-api/)

# code
```python:download.py
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os, time, sys

# Set API Key and Secret Key acquired in "Preparation"
key = "XXXXXXXXXX"
secret = "XXXXXXXXXX"

# Get data at 1 second intervals (because server side is tight)
wait_time = 1

# Search keyword (specified after the file name at runtime)
keyword = sys.argv[1]
# Save directory
savedir = "./" + keyword

# Create connection client and execute search
flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = keyword,           # search key
    per_page = 100,           # number of acquired data
    media = 'photos',         # collect photos
    sort = 'relevance',       # get latest
    safe_search = 1,          # avoid violent images
    extras = 'url_q, license' # extra information (download URL, license)
)

# Fetch and store results
photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
```

# Execution method
- Before execution, create a save directory for "search keyword" in a folder in the same hierarchy as "download.py"
- Execution is "python download.py [search keyword](=save directory)"

# in Japanese
