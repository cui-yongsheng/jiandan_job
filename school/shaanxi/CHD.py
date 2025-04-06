
import tomxin.getInfo

def getCHD():
#长安大学
# if __name__ == '__main__':
    url = "http://jyzx.chd.edu.cn/website/news_list.aspx?category_id=13"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'class="trStyle1">','pageDiv')
    title = tomxin.getInfo.get_content(info,'href.+?>','<')
    url = tomxin.getInfo.get_content(info,"href='","'")
    i=0
    for u in url[:]:
        r_city="陕西"
        r_school="长安大学"
        r_title=title[i]
        r_trait = "CHD" + u[-5:]#这里要自己写提取规则
        r_url = "http://jyzx.chd.edu.cn/website/" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '<div class="nei_border"></div>', '<div class="both"></div>')
        print(r_title + "\n" + r_url)

