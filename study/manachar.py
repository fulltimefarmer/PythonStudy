

def st(strs):
    length=len(strs)
    if length<2:
        return strs    #如果字符串是空或只有1个，那么返回这个字符串就好
    res = strs[0]    #如果写在if判断前面，当出现空字符串时候，会报错，
    maxlen=1
    for i in range(length-1):
        odd=centerspace(strs,i,i)          #当字符串长度是奇数的时候的判断方法
        even=centerspace(strs,i,i+1)       #当字符串长度是偶数时候的判断方法
        maxstr=odd if len(odd)>len(even)else even   #谁返回的字符串长度大，把返回的字符串赋值给maxstr
        if len(maxstr)>maxlen:      #如果最长长度小，那么把长的赋值给最长长度
            maxlen=len(maxstr)
            res=maxstr
    return res

def centerspace(strs,left,right):
    length=len(strs)
    i=left
    j=right
    while i>=0 and j<length:              #如果找到对称位置，能保证遍历完整个字符串
        if strs[i]==strs[j]:
            i-=1                       #往两边扩散，正好与对撞指针的思想相反
            j+=1
        else:
            break
    return strs[i+1:j]

s=st('dabcbaa')
print(s)