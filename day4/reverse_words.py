s = "Let's take LeetCode contest"
new_s = ''
words = s.split()
for word in words:
    word_l = list(word)
    for letter in range(0, len(word)):
        new_s += word_l.pop()
    new_s += ' '
new_s = new_s.strip()
print(new_s)