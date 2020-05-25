
'''
Summary:
    读取保存了 wav文件名:音符 对应的字典
Return
    music_dic - 字典
'''

import pickle
def GetMusicDic():
    with open('music_dic.pkl', 'rb') as file:
        music_dic = pickle.load(file)
    return music_dic


print(GetMusicDic())
for x in GetMusicDic().keys():
    print(x)
