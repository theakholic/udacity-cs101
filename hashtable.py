def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable,key)
    w = hashtable_lookup(htable,key)
    if not w:
        bucket.append([key,[value]])
    else:
        for e in w:
            if e[0] == key:
                e[1] = value
    return htable

def hashtable_lookup(htable, keyword):
    bucket = hashtable_get_bucket(htable,keyword)
    for e in bucket:
        if e[0] == keyword:
            return e[1]
    return None
def hashtable_get_bucket(htable,keyword):
    size = len(htable)
    pos = hash_string(keyword,size)
    return htable[pos]

def hash_string(keyword, buckets):
    ans = 0
    for c in keyword:
        ans = ans + ord(c)
        ans = ans%buckets
    return ans

def test_hash_string(hash_func, keys, buckets):
    results = [0]*buckets
    keys_used = []
    for key in keys:
        if key not in keys_used:
            n = hash_func(key,buckets)
            results[n] += 1
            keys_used.append(key)
    return results

def make_hashtable(buckets):
    res = []
    for i in range(buckets):
        res.append([])
    return res