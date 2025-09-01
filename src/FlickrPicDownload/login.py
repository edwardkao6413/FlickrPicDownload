import requests, random, re, json, time
from bs4 import BeautifulSoup

class loginFlk:
    user_agent_list = ['Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)',
            'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)',
            'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
            'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER']

    photo_sizes = ['Square', 'Large Square', 'Thumbnail', 'Small', 'Small 320', 'Small 400', 'Medium', 'Medium 640', 'Medium 800', 'Large', 'Large 1600', 'Large 2048', 'X-Large 3K', 'X-Large 4K']

    def __init__(self, api_key, file_safe_pos, user_email = None, user_pw = None):
        self.api_key = api_key
        self.file_safe_pos = file_safe_pos
        self.user_email = user_email
        self.user_pw = user_pw

    def download_single_album(self, ind_size = None):
        album_link = input('enter the album\'s link... If finish entering, entering -1')
        link_get_setID = re.compile(r'albums/\d+')
        set_ID = link_get_setID.search(album_link).group()[7:]

        qsp = {
            "method": "flickr.photosets.getPhotos",
            "api_key": self.api_key,
            "photoset_id": set_ID,
            "format": "json",
            "nojsoncallback": "1",
            "user_email":self.user_email, 
            "user_password":self.user_pw
        }

        header = loginFlk.user_agent_list[0]
        flickr_link = 'https://api.flickr.com/services/rest/'
        response = requests.get(flickr_link, params=qsp, headers={'user-agent': header})
        print('status code:', response.status_code)
        response_text = json.loads(response.text)
        
        photo_info = response_text['photoset']['photo']; n_id = len(photo_info)
        for i in range(n_id):
            header = random.choice(loginFlk.user_agent_list)
            photo_id = response_text['photoset']['photo'][i]['id']
            qsp = {
                    "method":"flickr.photos.getSizes",
                    "api_key":self.api_key,
                    "photo_id":photo_id,
                    "format":"json",
                    "nojsoncallback":"1",
                    "user_email":self.user_email,
                    "user_password":self.user_pw
                }
            response2 = requests.get(flickr_link, params = qsp, headers = {'user-agent' : header})
            response2_text = json.loads(response2.text)
            if ind_size == None: 
                try:
                    photo_link = response2_text['sizes']['size'][11]['source']
                    response_img = requests.get(photo_link, headers = {'user-agent' : header}).content
                    with open(self.file_safe_pos + photo_link[37:62] + '.jpg', 'wb') as image:
                        image.write(response_img)
                    print('number ' + str(i + 1) + ' img is successfully downloaded')
                except:
                    try:
                        photo_link = response2_text['sizes']['size'][10]['source']
                        response_img = requests.get(photo_link, headers = {'user-agent' : header}).content
                        with open(self.file_safe_pos + photo_link[37:62] + '.jpg', 'wb') as image:
                            image.write(response_img)
                        print('number ' + str(i + 1) + ' img is successfully downloaded')
                    except:
                        print('number ' + str(i + 1) + ' img failed to be successfully downloaded')
            
            else:
                try: 
                    indic = loginFlk.photo_sizes.index(ind_size)
                    photo_link = response2_text['sizes']['size'][indic]['source']
                    response_img = requests.get(photo_link, headers = {'user-agent' : header}).content
                    with open(self.file_safe_pos + photo_link[37:62] + '.jpg', 'wb') as image:
                        image.write(response_img)
                    print('number ' + str(i + 1) + ' img is successfully downloaded')
                
                except:
                    print('no such size for number ' + str(i + 1) + ' image')
                    try:
                        photo_link = response2_text['sizes']['size'][11]['source']
                        response_img = requests.get(photo_link, headers = {'user-agent' : header}).content
                        with open(self.file_safe_pos + photo_link[37:62] + '.jpg', 'wb') as image:
                            image.write(response_img)
                        print('number ' + str(i + 1) + ' img is successfully downloaded')
        
                    except:
                        print('number ' + str(i + 1) + ' img failed to be successfully downloaded')
                
        print('The whole download process is done')        
        

    def download_multiple_albums(self, ind_size = None):
        album_links = []
        album_link = input("enter the album's link... If finish entering, entering -1")
        while album_link != '-1':
            album_links.append(album_link)
            album_link = input("enter the album's link... If finish entering, entering -1")

        for k in range(len(album_links)):
            try:
                link_get_setID = re.compile(r'albums/\d+')
                set_ID = link_get_setID.search(album_links[k]).group()[7:]
            except:
                print('false link')
                continue

            # 向flickr發出請求，要取得album裡面所有的photo id
            flickr_link = 'https://api.flickr.com/services/rest/'
            
            qsp = {
                "method": "flickr.photosets.getPhotos",
                "api_key": self.api_key,
                "photoset_id": set_ID,
                "format": "json",
                "nojsoncallback": "1",
                "user_email":self.user_email,
                "user_password":self.user_pw
            }
            header = random.choice(loginFlk.user_agent_list)
            response = requests.get(flickr_link, params=qsp, headers={'user-agent': header})
            print('status code:', response.status_code)
            
            response_text = json.loads(response.text)
            photo_info = response_text['photoset']['photo']; n_id = len(photo_info)

            for i in range(n_id):
                header = random.choice(loginFlk.user_agent_list)
                photo_id = response_text['photoset']['photo'][i]['id']
                qsp = {
                        "method":"flickr.photos.getSizes",
                        "api_key":self.api_key,
                        "photo_id":photo_id,
                        "format":"json",
                        "nojsoncallback":"1", 
                        "user_email":self.user_email,
                        "user_password":self.user_pw                      
                    }
                response2 = requests.get(flickr_link, params = qsp, headers = {'user-agent' : header})
                response2_text = json.loads(response2.text)
                try:
                    if ind_size == None: 
                        try:
                            photo_link = response2_text['sizes']['size'][11]['source']
                            response_img = requests.get(photo_link, headers = {'user-agent' : header}).content
                            with open(self.file_safe_pos + photo_link[37:62] + '.jpg', 'wb') as image:
                                image.write(response_img)
                            print('number ' + str(i + 1) + ' img is successfully downloaded')
                        except:
                            try:
                                photo_link = response2_text['sizes']['size'][10]['source']
                                response_img = requests.get(photo_link, headers = {'user-agent' : header}).content
                                with open(self.file_safe_pos + photo_link[37:62] + '.jpg', 'wb') as image:
                                    image.write(response_img)
                                print('number ' + str(i + 1) + ' img is successfully downloaded')
                            except:
                                print('number ' + str(i + 1) + ' img failed to be successfully downloaded')
                        
                    else:
                        try: 
                            indic = loginFlk.photo_sizes.index(ind_size)
                            photo_link = response2_text['sizes']['size'][indic]['source']
                            response_img = requests.get(photo_link, headers = {'user-agent' : header}).content
                            with open(self.file_safe_pos + photo_link[37:62] + '.jpg', 'wb') as image:
                                image.write(response_img)
                            print('number ' + str(i + 1) + ' img is successfully downloaded')
                        
                        except:
                            print('no such size for number ' + str(i + 1) + ' image')
                            try:
                                photo_link = response2_text['sizes']['size'][11]['source']
                                response_img = requests.get(photo_link, headers = {'user-agent' : header}).content
                                with open(self.file_safe_pos + photo_link[37:62] + '.jpg', 'wb') as image:
                                    image.write(response_img)
                                print('number ' + str(i + 1) + ' img is successfully downloaded')
            
                            except:
                                print('number ' + str(i + 1) + ' img failed to be successfully downloaded')
            
                except:
                    print("The photographer probably don't provide users to mine pictures")
                    print("The album's link is {}".format(album_links[k]))
                    continue
            print("number {} album has been downloaded".format(k + 1))
        print('Whole download process has been done')


    

    def download_respective_photo(self, ind_size = None):
        photo_panels = []
        img_link = input('entering the photo\'s link... If finish entering, entering -1')
        while img_link != '-1':
            photo_panels.append(img_link)
            img_link = input()

        n_id = len(photo_panels)
        for i in range(n_id):
            try:
                img_id_search = re.compile(r'(\d+)/in')
                img_id = img_id_search.search(photo_panels[i]).group(0)[:-3]
                url = 'https://www.flickr.com/services/rest/'
                header = random.choice(loginFlk.user_agent_list)
                qsp = {
                    "method":"flickr.photos.getSizes",
                    "api_key":self.api_key,
                    "photo_id":img_id,
                    "format":"json",
                    "nojsoncallback":"1", 
                    "user_email":self.user_email, 
                    "user_password":self.user_pw
                }
                response = requests.get(url, headers = {'user-agent':header}, params = qsp)
                response_text = json.loads(response.text)
                try:
                    if ind_size == None: 
                        try:
                            photo_link = response_text['sizes']['size'][11]['source']
                            response_img = requests.get(photo_link, headers = {'user-agent' : header}).content
                            with open(self.file_safe_pos + photo_link[37:62] + '.jpg', 'wb') as image:
                                image.write(response_img)
                            print('number ' + str(i + 1) + ' img is successfully downloaded')
                        except:
                            try:
                                photo_link = response_text['sizes']['size'][10]['source']
                                response_img = requests.get(photo_link, headers = {'user-agent' : header}).content
                                with open(self.file_safe_pos + photo_link[37:62] + '.jpg', 'wb') as image:
                                    image.write(response_img)
                                print('number ' + str(i + 1) + ' img is successfully downloaded')
                            except:
                                print('number ' + str(i + 1) + ' img failed to be successfully downloaded')
                        
                    else:
                        try: # 下載指定畫素
                            indic = loginFlk.photo_sizes.index(ind_size)
                            photo_link = response_text['sizes']['size'][indic]['source']
                            response_img = requests.get(photo_link, headers = {'user-agent' : header}).content
                            with open(self.file_safe_pos + photo_link[37:62] + '.jpg', 'wb') as image:
                                image.write(response_img)
                            print('number ' + str(i + 1) + ' img is successfully downloaded')
                        
                        except:
                            print('no such size for number ' + str(i + 1) + ' image')
                            try:
                                photo_link = response_text['sizes']['size'][11]['source']
                                response_img = requests.get(photo_link, headers = {'user-agent' : header}).content
                                with open(self.file_safe_pos + photo_link[37:62] + '.jpg', 'wb') as image:
                                    image.write(response_img)
                                print('number ' + str(i + 1) + ' img is successfully downloaded')
            
                            except:
                                print('number ' + str(i + 1) + ' img failed to be successfully downloaded')
            
                except:
                    print("The photographer probably don't provide users to mine pictures")
                    continue        
            
            except:
                print('there are something wrong')
        print('The whole download process is done')

    def violent_crawling(self):
        print('Warning!! Violent crawling may not crawl all of the information on the internet.')
        url = input('entering your album\'s link...')
        header = random.choice(loginFlk.user_agent_list)
        response = requests.get(url, headers={'user-agent': header})
        response_text = response.text
        soup = BeautifulSoup(response_text, 'html.parser')

        html_code = soup.find_all('html')
        html_text = str(html_code)

        url_compile = re.compile(r'live.staticflickr.com\W\W\d+\W\W\d\d\d\d\d\d\d\d\d\d\d_\w\w\w\w\w\w\w\w\w\w_k.jpg')
        url_list_org = url_compile.findall(html_text)
        url_list = []
        for urls in url_list_org:
            if urls[-5] == 'k':
                urls = urls.replace('\\', '/')
                url_list.append(urls)
            elif urls[-5] == 'h':
                urls = urls.replace('\\', '/')
                url_list.append(urls)

        for i in range(len(url_list)):
            img_url = 'https://' + url_list[i]
            if i > 0:
                if url_list[i] == url_list[i - 1]:
                    continue
            try:
                header = random.choice(loginFlk.user_agent_list)
                # header = 'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
                response = requests.get(img_url, headers={'user-agent': header}).content
                with open(self.file_safe_pos + img_url[37:62] + '.jpg', 'wb') as file:
                    file.write(response)
                time.sleep(1)
                print('successfully download {}'.format(i))
            except:
                print('Number {} picture failed to downloaded'.format(i))
        print('If you did not find the images, this may be: 1. Photographer did not provide same size pictures as you indicated, 2. phtographer did not allow people withoit membership to see, 3. other problem')

