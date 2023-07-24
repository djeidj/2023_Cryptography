#  该程序针对输入文本带空格的情况进行编写
import re


#  hzsrngc klyy wqc flo mflwf ol zqdn nsoznj wskn lj xzsrbjnf, wzsxz gqv zqhhnf ol ozn glco zlfnco hnihrn; nsoznj jnrqosdnclj fnqj kjsnfbc, wzSxz sc xnjoqsfrv gljn efeceqr. zn rsdnbqrlfn sf zsc zlecn sf cqdsrrn jlw, wzsoznj flfn hnfnojgonb. q csfyrn blgncosx cekksxnb ol cnjdn zsg. zn pjngmkqconb qfbbsfnb qo ozn xrep, qo zlejc gqoznggosxqrrv ksanb, sf ozn cqgnjllg, qo ozn cqgn oqprn, fndnj oqmsfy zsc gnqrc wsoz loznjgngpnjc, gexz rncc pjsfysfy q yenco wsoz zsg; qfb wnfo zlgnqo naqxorv gsbfsyzo, lfrv ol jnosjn qo lfxn ol pnb. zn fndnjecnb ozn xlcv xzqgpnjc wzsxz ozn jnkljg hjldsbnc klj soc kqdlejnb gngpnjc. zn hqccnb onf zlejc leo lk ozn ownfov-klejsf cqdsrrn jlw, nsoznj sf crnnhsfy lj gqmsfy zsc olsrno.


#  对一个字典按照值大小降序排序，需要返回
def sort_dict_value(my_dict):
    sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    my_dict = dict(sorted_dict)
    return my_dict

#  对一个字典按照键大小降序排序，需要返回
def sort_dict_key(my_dict):
    sorted_dict = sorted(my_dict.items(), key=lambda x: x[0], reverse=False)
    my_dict = dict(sorted_dict)
    return my_dict

#  打印一个字典
def print_dict(my_dict):
    for i in my_dict:
        print(i + ":", my_dict[i])





#  先对文本中的单词做统计，返回单词出现次数
def get_frequence_word(encode_text):

    #  按照空格对文本进行切片，并且去掉标点符号
    encode_text = encode_text.lower()
    encode_text = encode_text.replace('\n', ' ')
    encode_text = re.sub(r'[^\w\s]', ' ', encode_text)

    word_list = filter(lambda w: re.match('^[a-z]+$', w), encode_text.split())

    return list(word_list)

#  统计一个单词中双字母组合个数
def count_bigrams(word):
    bigram_pattern = re.compile(r'(?=(\w\w))')
    bigrams = bigram_pattern.findall(word)
    return bigrams
    
#  统计一个单词中的三字母组合个数
def count_thgrams(word):
    thgram_pattern = re.compile(r'(?=(\w\w\w))')
    thgrams = thgram_pattern.findall(word)
    return thgrams




#  更新代换表，只更换部分
def update_part_table(pre_image, image, mapping_table):
    temp_table = mapping_table.copy()

    length = len(pre_image)
    for key in mapping_table:
        if mapping_table[key] in image:
            del temp_table[key]
    
    for i in range(length):
        temp_table[pre_image[i]] = image[i]
    
    mapping_table = temp_table.copy()
    return mapping_table

#  更新代换表，完整的表
def update_all_table(char_dict, mapping_table):
    temp_table = mapping_table.copy()
    #  先要将mapping_table中的映射在frequence_chr_list与char_dict中删除，这样才方便建立映射，最后对代换表进行优化

    #  删除统计表与已知概率表中已知的映射对
    new_list = frequence_chr_list.copy()

    for i in list(mapping_table.keys()):
        if i in new_list:
            new_list.remove(i)

    for i in list(mapping_table.values()):
        if i in char_dict:
            del char_dict[i]
    
    #  将处理后的统计表与概率表结合起来，建立映射
    for i in range(len(new_list)):
        temp_table[new_list[i]] = list(char_dict.keys())[i]

    temp_table = sort_dict_key(temp_table)
    return temp_table




#  26个英文字母出现频率
frequence_chr_list = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'x', 'q', 'j', 'z']

#  统计文本中单个字母出现频率
def get_frequence_chr(word_list):

    #  统计各个字母的频率
    char_dict = {}
    for i in word_list:
        for j in i.lower():
            if j not in char_dict:
                char_dict[j] = 1
            else:
                char_dict[j] += 1
    char_dict = sort_dict_value(char_dict)

    return char_dict

    


#  最常见的双字母组合出现频率
frequence_twochr_list = ['th', 'he', 'in', 'er', 'an', 're', 'ed', 'on', 'es', 'st', 'en', 'at', 'to', 'nt']

#  然后再统计文本中的双字母组合出现频率
def get_frequence_twochr(word_list):

    #  统计各双字母组合频率
    twochar_dict = {}
    for word in word_list:
        bigrams = count_bigrams(word)
        for bigram in bigrams:
            if bigram in twochar_dict:
                twochar_dict[bigram] += 1
            else:
                twochar_dict[bigram] = 1
    twochar_dict = sort_dict_value(twochar_dict)

    return twochar_dict




#  最常见的三字母组合
frequence_thrchr_list = ['the', 'ing', 'and', 'her', 'ere', 'ent', 'tha', 'nth']

#  然后再统计文本中的三字母组合出现频率
def get_frequence_thrchr(word_list):

    #  统计各双字母组合频率
    thrchar_dict = {}
    for word in word_list:
        bigrams = count_thgrams(word)
        for bigram in bigrams:
            if bigram in thrchar_dict:
                thrchar_dict[bigram] += 1
            else:
                thrchar_dict[bigram] = 1
    thrchar_dict = sort_dict_value(thrchar_dict)

    return thrchar_dict



def decode(encode_text, ori_table):
    la_table = {ori_table[i]: i for i in ori_table}

    decode_text = ''
    for i in encode_text:
        if i in la_table:
            decode_text+=la_table[i]
        else:
            decode_text+=i
    
    return decode_text