s = ["h","e","l","l","o"]

new_s = []
for index in range(0, len(s)):    
    new_s.append(s.pop())
s[:] = new_s
pass