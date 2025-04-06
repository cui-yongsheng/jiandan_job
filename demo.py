from openai import OpenAI
import tomxin.getInfo

#大学名称
if __name__ == '__main__':
    client = OpenAI(api_key="sk-40e269b18bcc407c8c1f802fd9a195aa", base_url="https://api.deepseek.com")
    url = "http://career.cic.tsinghua.edu.cn/xsglxt/f/jyxt/anony/xxfb"
    my_question = "首先判断招聘信息是否面向2026届毕业生，包括实习。如果是，判断招聘岗位是否包括通信、深度学习、开发等。如果是，仅将招聘信息进行整理输出，主要包含工作地点，招聘岗位等。否则仅输出{cuiys}"

    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'chapter1','pgDiv')
    title = tomxin.getInfo.get_content(info,'fbfw.+?>','</a>')
    url = tomxin.getInfo.get_content(info,'ahref="','"')
    i=0
    for u in url:
        r_city="北京"
        r_school="清华大学"
        r_title=title[i]
        r_trait = "TU" + u[-14:-6]#这里要自己写提取规则
        r_url = "http://career.cic.tsinghua.edu.cn/" + u
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '<!-- 职位描述 -->', '单位简介')
        r_content=r_content+"<br><h6>注意：清华大学部分企业联系方式需要跳转回原网址查看</h6>"
        # print(r_title + "\n" + r_url)
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": f"Hello, my question is: {my_question}. analyse the context: {r_content}"},
            ],
            stream=False,
            timeout = 100
        )
        if '招聘岗位' in response.choices[0].message.content:
            print(response.choices[0].message.content)
        i += 1