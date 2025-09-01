# FlickrPicDownload: Useful tools for downloading image off different resolution from Flickr
Made by Edward Kao, *First version is published on Sep 2025 on PyPi*

## installation and requirements
### 1. installation
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
### 1. 







