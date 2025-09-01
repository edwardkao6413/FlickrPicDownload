# FlickrPicDownload: Useful tools for downloading image off different resolution from Flickr
Made by Edward Kao, *First version is published on Sep 2025 on PyPi*

## installation and requirements
### 1. Installation
```bash
pip install FlickrPicDownload
```

### 2. Required packages
Several basic packages are required for running this script, including:
1. Python 3.x (Python >= 3.7 would be better)
2. requests, bs4: For making query toward internet
3. random
4. re: For regular expression, identifying either photo id or photobook id within url.
5. json
6. flickrapi: For plugin user's flickrapi, User can apply for api token from flickr,
Here's the function telling you which packages that users should install before using.
```python
from FlickrPicDownload import packages
packages()
```

## Usage
### 0. Before downloading, api_token and img saving position is required
-- login only by api_key and saving position, replaced your_api_key with your api token
```python
from FlickrPicDownload import loginFlk
bot = loginFlk(api_key = u"your_api_key", file_safe_pos = "C:\\users\\xxxx\\target_folder\\")
```
-- login by api_key, saving position, user_email, and password, where user_email and password is optional
```python
from FlickrPicDownload import loginFlk
bot = loginFlk(api_key = u"your_api_key", file_safe_pos = "C:\\users\\xxxx\\target_folder\\", user_email = "your_flickr_account_email", user_pw = "your_flickr_password")
```
-- Different resolutions for img
Sizes contain: 'Square', 'Large Square', 'Thumbnail', 'Small', 'Small 320', 'Small 400', 'Medium', 'Medium 640', 'Medium 800', 'Large', 'Large 1600', 'Large 2048', 'X-Large 3K', 'X-Large 4K'. *Default size is set as "Large 2048", if users do not plugin any choice to ind_size parameter.*
Users can see img size list by using command below
```python
from FlickrPicDownload import figuresizes
figuresizes()
```
### 1. Function 1-- Download all images in a single album
Intuitive as the words above, when users implement this command, just put album's link into input.
```python
bot.download_single_album()
```
Supposed users want to specify the img resolution: (all imgs from this album are downloaded in specified resolution
```python
bot.download_single_album(ind_size = "X-Large 4K")
```

### 2. Function 2-- Download images in multiple albums
Just keep entering the album's link into input, each input only allows one link, which means supposed users want to enter the second album's link, they should press 'enter' first. **When finishing entering the links, type -1 in input**
```python
bot.download_multiple_albums()
```
Supposed users want to specify the img resolution: (all imgs from this album are downloaded in specified resolution
```python
bot.download_multiple_albums(ind_size = "X-Large 4K")
```

### 3. Function 3-- Download single or multiple individual images
Go to the image url (example url: https://www.flickr.com/photos/dionisioyang/14825239237/in/photolist-oA4e84-2cBRC6H-9nNeyQ-2fyJNFq-2m5v4Mu-JnxBXq-26v1rc6-oA3JCG-56WhcN-PLv7oo-aoxTh3-Niyx5Y-26uzmvm-oA4P89-259mtMV-2fyJLpb-VxHkGA-CyuQ7Q-2fyJMJ5-PLveBG-6YWdPQ-235LBY5-YaqiwJ-9yPWMn-oZgrAR-oEzdjg-pGcaJq-rucYzZ-2fFVtMj-256VZqp-frZZSV-2qQkqcK-48GkrM-Dtotff-25SjksF-poR8nF-ExLyGQ-W5NfKu-poUef4-2qQmq2y-ru6DTt-2fyJNY9-oRYFve-j1H8Es-ru6EtX-6CKWu8-oShWic-2qQjiWc-DB1Htb-2crzetE), and copy and paste this img link to input. Same as downloading multiple albums, links must be entered one by one. **When finishing entering the links, type -1 in input**
```python
bot.download_respective_photo()
```
Supposed users want to specify the img resolution: (all imgs are downloaded in specified resolution
```python
bot.download_respective_photo(ind_size = "X-Large 4K")
```

## Important notices
1. **Flickr has brought forward a policy on May 2025 that photo owners can select whether they are willing to allow free accounts to download the photos with resolutions higher than 2048. Hence, some photos are not allowed to be downloaded.**
2. **Some photo owners turn their albums into not allowing to use api download. This issue cause unsuccessful download as well.**
3. **Supposed there's no error occurred but end up nothing being downloaded, this means the photos' resolution did not reach 2048.**




