with open('./Text Files/p79_keylog.txt', 'r') as p79:
    keylog = p79.read()

logins = keylog.split('\n')[:-1] # string value of each login
seq = [[int(d) for d in l] for l in logins] # array of the integers in each login
checked = [False for _ in logins] # checked[n - 1] returns boolean for if n has been checked

def hasSubseq(arr, subseq):
    if len(arr) < len(subseq): return False

    end = len(subseq)
    while end <= len(arr):
        if arr[:end] == subseq: return True
        del arr[0]
