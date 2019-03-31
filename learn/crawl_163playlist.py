from selenium import webdriver

# 网易云音乐歌单列表第一页地址
URL = 'https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
# Chrome接口创建一个Selenium的Webdriver
browser = webdriver.Chrome()


while URL != 'javascript:void(0)':
    browser.get(URL)
    # 切换至内容的iframe
    browser.switch_to.frame("contentFrame")
    # 定位歌单标签
    data = browser.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
    # 解析当前页所有的歌单详情
    for i in range(len(data)):
        # 获取歌单的播放量
        num  = data[i].find_element_by_class_name("nb").text
        # 歌单播放量大于1000万的
        if '万' in num and int(num.split('万')[0]) > 1000:
            msk = data[i].find_element_by_css_selector("a.msk")
            with open("163playlist.txt", 'a', encoding='utf-8') as f:
                f.write(' '.join([msk.get_attribute('title'), num, msk.get_attribute('href')]) + '\n' + '='*66 + '\n')

    # 通过<a class="zbtn.znxt"></a>
    URL = browser.find_element_by_css_selector("a.zbtn.znxt").get_attribute("href")


browser.close()