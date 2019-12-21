import pinyin
# 输入name
last_name =u"王李张刘杨陈赵黄周吴徐郑马朱胡郭何高林罗孙梁谢宋唐许韩邓曹彭曾萧田董潘袁于蒋蔡余杜叶程苏魏吕丁任沈姚卢姜崔钟谭陆汪范金石廖贾夏韦傅方白邹孟熊秦邱江尹薛阎段雷侯龙史陶黎贺顾毛郝龚邵万钱严覃河戴莫孔向汤"
last_pinyin =u"wlzlyczhzwxzmzhghgllslxstxhdcpcxtdpyyjcydycswldrsyljcztlwfjsljxwffbzmxqqjyxydlhlstlhgmhgswqythdmkxt"
first_name =u"筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊勤珍贞莉兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥"
first_pinyin ="yrzanxhxfyfhyyykjsylzslxjyhhqmnjshzcyzyphelffyccjqzzllfjmlsylzhxràmxxyyyyrfjjqgdyblyqjyqqssjdqqtjwxjylyycybwyhdrmjqrwjmlyjxyyyryyyqclcyyzbswmyxnxpyyf"
list_ln =[]
list_fn =[]
list_last_name = list(last_name)
list_last_pinyin = list(last_pinyin)

list_first_name = list(first_name)
list_first_pinyin = list(first_pinyin)
# the last name in chinese sorted by population desc
for (i, l_name,py_name) in zip(range(100,0,-1),list_last_name,list_last_pinyin):
    dict_last_name ={}
    dict_last_name['last_name']= l_name
    dict_last_name['pinyin'] = py_name
    dict_last_name['qz'] = i
    list_ln.append(dict_last_name)
# print(list_ln)
# common girl first name
for (qz_py, l_name_first,py_name_first) in zip(range(1,len(first_name)),list_first_name,list_first_pinyin):
    dict_first_name ={}
    dict_first_name['first_name']= l_name_first
    dict_first_name['pinyin'] = py_name_first
    dict_first_name['qz'] = qz_py
    list_fn.append(dict_first_name)
# print(list_fn)
def get_pinyin_first_alpha(name):
    return "".join([i[0] for i in pinyin.get(name, " ").split(" ")])

def guessWhat(FullName):
    Result =[]
    xingshi =[]
    mingzi =[]
    mingzi2 =[]
    #姓氏 last_name
    for l_line_row in list_ln:
        if FullName[0]== l_line_row['pinyin'] :
            xingshi.append(l_line_row['last_name'])
    print(xingshi)
    #名字第一个字firstname
    for l_line_row in list_fn:
        if FullName[1]== l_line_row['pinyin'] :
            mingzi.append(l_line_row['first_name'])
    print(mingzi)
    #名字第二个字second name
    for l_line_row in list_fn:
        if FullName[2]== l_line_row['pinyin'] :
            mingzi2.append(l_line_row['first_name'])
    print(mingzi)
    for last in xingshi:
        for first in mingzi:
            for second in mingzi2:
            # print(last+'宏'+second)
                print(last + first + second)
# data = get_pinyin_first_alpha(first_name)
guessWhat('lyf')
# print(data)
# print(data)
