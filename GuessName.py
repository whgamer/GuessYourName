import pinyin
# 输入name

def get_pinyin_first_alpha(name):
    return "".join([i[0] for i in pinyin.get(name, " ").split(" ")])

def guessWhat(sex,FullName):
    list_ln = get_last_name_data(list_last_name, list_last_name_pinyin)
    if sex=='boy':
        list_fn= girl_boy_data(name_boy, list_name_boy, list_boy_pinyin)
    else:
        list_fn= girl_boy_data(name_girl, list_name_girl, list_girl_pinyin)

    Result =[]
    xingshi =[]
    mingzi =[]
    mingzi2 =[]
    Name_Guess =[]
    #姓氏 last_name
    if len(FullName[0])>= 1 :
        for l_line_row in list_ln:
            if FullName[0]== l_line_row['pinyin'] :
                xingshi.append(l_line_row['last_name'])
                # print(xingshi)
    #名字第一个字firstname
    if len(FullName)>=2:
        for l_line_row in list_fn:
            if FullName[1]== l_line_row['pinyin'] :
                mingzi.append(l_line_row['first_name'])
        # print(mingzi)
    #名字第二个字second name
    if len(FullName)>=3:
        for l_line_row in list_fn:
            if FullName[2]== l_line_row['pinyin'] :
                mingzi2.append(l_line_row['first_name'])
        # print(mingzi)
    for last in xingshi:
        if mingzi :
            for first in mingzi:
                if mingzi2 :
                    for second in mingzi2:
                    # print(last+'宏'+second)
                        result = last + first + second
                        Name_Guess.append(result)

                # 处理姓名两个字的情况
                else:
                    result = last + first
                    Name_Guess.append(result)
    return Name_Guess
last_name =u"王李张刘杨陈赵黄周吴徐郑马朱胡郭何高林罗孙梁谢宋唐许韩邓曹彭曾萧田董潘袁于蒋蔡余杜叶程苏魏吕丁任沈姚卢姜崔钟谭陆汪范金石廖贾夏韦傅方白邹孟熊秦邱江尹薛阎段雷侯龙史陶黎贺顾毛郝龚邵万钱严覃河戴莫孔向安汤艾"# 添加安艾
last_pinyin =u"wlzlyczhzwxzmzhghgllslxstxhdcpcxtdpyyjcydycswldrsyljcztlwfjsljxwffbzmxqqjyxydlhlstlhgmhgswqythdmkxata"
print(len(last_name))
name_girl =u"筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊勤珍贞莉兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥"

girl_pinyin = get_pinyin_first_alpha(name_girl)
# 添加男孩子常用名字版本
name_boy ="泽朗伯昮晋晟诚先敬震振壮会思群豪心邦承乐宏言旲旻昊天达安岩中茂进林有坚和彪博泰盛振挺明永健世广志义兴良海山仁波宁行时志忠思绍功松善厚庆磊"
boy_pinyin = get_pinyin_first_alpha(name_boy)
list_ln =[]
list_fn =[]
list_last_name = list(last_name)
list_last_name_pinyin = list(last_pinyin)

list_name_boy = list(name_boy)
list_boy_pinyin = list(boy_pinyin)

list_name_girl = list(name_girl)
list_girl_pinyin = list(girl_pinyin)
# the last name in chinese sorted by population desc
def get_last_name_data(list_last_name,list_last_name_pinyin):
    for (i, l_name,py_name) in zip(range(len(last_name),0,-1),list_last_name,list_last_name_pinyin):
        dict_last_name ={}
        dict_last_name['last_name']= l_name
        dict_last_name['pinyin'] = py_name
        dict_last_name['qz'] = i
        list_ln.append(dict_last_name)
    return list_ln
# print(list_ln)
# common girl first name store data  as  list consists of dict
def girl_boy_data(str_name,list_name,list_name_pinyin):
    for (qz_py, l_name_first,py_name_first) in zip(range(1,len(str_name)),list_name,list_name_pinyin):
        dict_first_name ={}
        dict_first_name['first_name']= l_name_first
        dict_first_name['pinyin'] = py_name_first
        dict_first_name['qz'] = qz_py
        list_fn.append(dict_first_name)
    return list_fn
# common girl boy name
# print(list_fn)

def main():
    abbr = 'yzy'
    sex = 'girl'
    result = guessWhat(sex, abbr)
    # result.sort()
    print('您输入简称是' + abbr + '性别是' + sex + '可能结果' + ':\n', result)

if __name__ == "__main__":
    main()

# print(data)
# print(data)
# EGW7N9TFHBTG7O54OVMYJ3I