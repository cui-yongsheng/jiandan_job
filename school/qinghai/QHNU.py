
import tomxin.getInfo

def getQHNU():
#青海师范大学
# if __name__ == '__main__':
    url = "http://jc.qhnu.edu.cn/home-article-index-modnav-10.shtml"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'class="newslist">','pagelist')
    title = tomxin.getInfo.get_content(info,'desc">','<')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:]:
        r_city="青海"
        r_school="青海师范大学"
        r_title=title[i]
        r_trait = "QHNU" + u[-9:-6]#这里要自己写提取规则
        r_url = "http://jc.qhnu.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", 'div class="bottom_left">', '<div class="cont_right right">')
        print(r_title + "\n" + r_url)

