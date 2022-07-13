def function(s):    
    hash_map = {}
    if len(s) > 0:
        ans = 1
        for index in range(len(s)):        
            if s[index] not in hash_map:
                hash_map[s[index]] = index
            else:
                keys = list(hash_map.keys())
                repeated_index = hash_map[s[index]]
                for key in keys:
                    if hash_map[key] <= repeated_index:
                        del hash_map[key]
                    else:
                        break
                hash_map[s[index]] = index
            ans = max(ans, len(hash_map))    
    else:
        ans = 0
    return ans


s = "ckilbkd"
print(function(s))
