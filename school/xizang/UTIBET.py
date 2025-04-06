
import tomxin.getInfo

def getUTIBET():
#西藏大学
# if __name__ == '__main__':
    url = "http://www.utibet.edu.cn/news/article_38_58_0.html"#高校就业网的网址
    html = tomxin.getInfo.get_source_head(url)
    info = tomxin.getInfo.get_info(html,'class="text">',' id="page">')
    title = tomxin.getInfo.get_content(info,'href.+?>','<')
    url = tomxin.getInfo.get_content(info,'href="..','"')
    i=0
    for u in url[:7]:
        r_city="西藏"
        r_school="西藏大学"
        r_title=title[i].strip()
        r_trait = "UTIBET" + u[-10:-5]#这里要自己写提取规则
        r_url = "http://www.utibet.edu.cn" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content_head(r_url, '<div style="margin:0 10px;">', '<div class=cle>')
        print(r_title + "\n" + r_url)

