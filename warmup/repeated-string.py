# Runtime Error
def repeatedString(s, n):
    num_str = len(s)
    mutiple_num = n//num_str
    merge_str = s*mutiple_num + s[:n%num_str]
    return merge_str.count('a')
    
    
# OK
def repeatedString(s, n):
    num_a = s.count('a')
    ans = num_a*(n//len(s)) + s[:n%len(s)].count('a')
    return ans 
