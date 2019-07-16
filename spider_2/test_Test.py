from urllib.request import urlopen, urljoin

import pymysql
from bs4 import BeautifulSoup
import re


def main():
    f = open ('wanzheng.txt', 'r')
    for i in f:
        html = urlopen(i).read().decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')

        # 狗的名字 - dog_vari_name
        dog_vari_name = soup.span.get_text()
        print(dog_vari_name)

        # 头像 - dog_vari_img
        dog_vari_img = soup.find("img", {"src": re.compile('http.*?')})['src']
        print(dog_vari_img)

        # 别名 - alias
        j = soup.findAll('p',{'style':re.compile('.*')})[1].get_text()
        alias = re.findall(re.compile('别名：(.*?)生源'), j)
        print(alias)

        # 英文名 - en_name
        all_name = soup.find_all('p')[1].get_text ()
        en_name = re.findall(re.compile ('英文名：(.*) '), all_name)
        print(en_name)

        # 原产地- origin
        origin = re.findall(re.compile('原产地：(.*) '), all_name)
        print(origin)

        # 体型 - shape
        shape = re.findall(re.compile('体型：(.*) '), all_name)
        print(shape)

        # 价格 - price
        price = re.findall(re.compile('价格：(.*) '), all_name)
        print(price)

        # 体重 - weight
        weight = re.findall(re.compile('体重：(.*) '), all_name)
        print(weight)

        # 粘人程度 - sti_degree
        all_degree = soup.find_all('p')
        sti_degree = str(re.findall(re.compile('粘人程度：<i class="star-\d'), str(all_degree)))[-3]
        print(sti_degree)

        # 喜叫程度 - bar_degree
        bar_degree = str(re.findall(re.compile('喜叫程度：<i class="star-\d'), str(all_degree)))[-3]
        print(bar_degree)

        # 掉毛程度 - hairloss_degree
        hairloss_degree = str(re.findall(re.compile('掉毛程度：<i class="star-\d'), str(all_degree)))[-3]
        print(hairloss_degree)

        # 友善程度 - fri_degree
        fri_degree = str(re.findall(re.compile('友善程度：<i class="star-\d'), str(all_degree)))[-3]
        print(fri_degree)

        # 运动量 - stranger_frii_degree
        stranger_frii_degree = str(re.findall(re.compile('运动量：<i class="star-\d'), str(all_degree)))[-3]
        print(stranger_frii_degree)

        # 可训程度 - compliance
        compliance = str(re.findall(re.compile('可训程度：<i class="star-\d'), str(all_degree)))[-3]
        print(compliance)

        # 护家程度 - home_degree
        home_degree = str(re.findall(re.compile('护家程度：<i class="star-\d'), str(all_degree)))[-3]
        print(home_degree)

        # 形态特征 - feature
        j = soup.get_text()
        feature = re.findall(re.compile('鉴别(.*)性格特点', re.S), j)
        print(feature)

        # 注意事项 - attention
        attention = re.findall(re.compile('常见问题(.*)', re.S), j)
        print(attention)

        # 养护知识 - nurturing_knowledge
        nurturing_knowledge = re.findall(re.compile('驯养知识(.*)', re.S), j)
        print(nurturing_knowledge)


        conn = pymysql.Connect(host='47.103.12.202', port=3306,
                               user='root', password='123456',
                               database='pethome', charset='utf8')
        cursor = conn.cursor()
        sql = 'insert into {} (dog_vari_name, dog_vari_img, en_name, alias, weight, shape, origin, price, sti_degree, bar_degree, hairloss_degree, fri_degree, stranger_fri_degree, compliance, home_degree, feature, attention, nurturing_knowledge) values ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", {}, {}, {}, {}, {}, {}, {}, "{}", "{}", "{}");'.format (
            'dog_vari', dog_vari_name, dog_vari_img, en_name, alias, weight, shape, origin, price, sti_degree, bar_degree, hairloss_degree, fri_degree, stranger_frii_degree, compliance, home_degree, feature, attention, nurturing_knowledge
        )
        cursor.execute(sql)
        conn.commit()
        conn.close()

if __name__ == '__main__':
    main()
