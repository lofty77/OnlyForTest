# coding=utf-8
import sys

PYTHON_3 = True

cities = {
    'bj': '北京',
    'sh': '上海',
    'tj': '天津',
    'wh': '武汉',
}


# lianjia_cities = cities
# beike_cities = cities


def create_prompt_text():
    """
    根据已有城市中英文对照表拼接选择提示信息
    :return: 拼接好的字串
    """
    city_info = list()
    count = 0
    for en_name, ch_name in cities.items():
        count += 1
        city_info.append(en_name)
        city_info.append(": ")
        city_info.append(ch_name)
        if count % 4 == 0:
            city_info.append("\n")
        else:
            city_info.append(", ")
    return 'Which city do you want to crawl?\n' + ''.join(city_info) + '\n' + 'input : '


def get_chinese_city(en):
    """
    拼音拼音名转中文城市名
    :param en: 拼音
    :return: 中文
    """
    return cities.get(en, None)


def get_city():
    city = None
    # 允许用户通过命令直接指定
    if len(sys.argv) < 2:
        print("Wait for your choice.")
        # 让用户选择爬取哪个城市的二手房小区价格数据
        prompt = create_prompt_text()

        city = input(prompt)

    elif len(sys.argv) == 2:
        city = str(sys.argv[1])
        print("City is: {0}".format(city))
    else:
        print("At most accept one parameter.")
        exit(1)

    chinese_city = get_chinese_city(city)
    if chinese_city is not None:
        message = 'OK, start to crawl ' + get_chinese_city(city)
        print(message)
    else:
        print("No such city, please check your input.")
        exit(1)
    return city


if __name__ == '__main__':
    # print(get_chinese_city("sh"))
    # city = get_city()
    city = get_chinese_city("tj")

    city_gbk = repr(city.encode('gbk')).replace("\\x", "%")

    print(city_gbk)
