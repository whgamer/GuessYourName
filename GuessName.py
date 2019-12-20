import pinyin


# 输入name
last_name =u"王李张刘杨陈赵黄周吴徐郑马朱胡郭何高林罗孙梁谢宋唐许韩邓曹彭曾萧田董潘袁于蒋蔡余杜叶程苏魏吕丁任沈姚卢姜崔钟谭陆汪范金石廖贾夏韦傅方白邹孟熊秦邱江尹薛阎段雷侯龙史陶黎贺顾毛郝龚邵万钱严覃河戴莫孔向汤"
last_pinyin =u"wlzlyczhzwxzmzhghgllslxstxhdcpcxtdpyyjcydycswldrsyljcztlwfjsljxwffbzmxqqjyxydlhlstlhgmhgswqythdmkxt"
first_name ="筠柔竹霭凝、晓、欢、霄、枫、芸、菲、寒、伊、亚、宜、可、姬、舒、影、荔、枝、思、丽、秀、娟、英、华、慧、巧、美、娜、静、淑、 惠、珠、翠、雅、芝、玉、萍、红、娥、玲、芬、芳、燕、彩、春、菊、勤、珍、贞、莉、兰、凤、洁、梅、琳、素、云、莲、真、环、雪、荣、爱、妹、霞、香、 月、莺、媛、 艳、瑞、凡、佳、嘉、琼、桂、娣、叶、璧、璐、娅、琦、晶、妍、茜、秋、珊、莎、锦、黛、青、倩、婷、姣、婉、娴、瑾、颖、露、瑶、怡、婵、雁、蓓、纨、 仪、荷、丹、蓉、眉、君、琴、蕊、薇、菁、梦、岚、 苑、婕、馨、瑗、琰、韵、融、园、艺、咏、卿、聪、澜、纯、毓、悦、昭、冰、爽、琬、茗、羽、希、宁、欣、飘、育、滢、馥"
list_ln =[]
list_last_name = list(last_name)
list_last_pinyin = list(last_pinyin)
# for l in list(last_name):
#     print(l)
for (i, l_name,py_name) in zip(range(1,100),list_last_name,list_last_pinyin):
    dict_last_name ={}
    dict_last_name['last_name']= l_name
    dict_last_name['pinyin'] = py_name
    dict_last_name['qz'] = i
    list_ln.append(dict_last_name)
print(list_ln)

def get_pinyin_first_alpha(last_name):
    return "".join([[0] for i in pinyin.get(name, " ").split(" ")])


data = get_pinyin_first_alpha(last_name)
# print(data)
