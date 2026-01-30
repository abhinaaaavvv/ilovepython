from wordfreq import top_n_list

words = [w for w in top_n_list("en", 5000) if w.isalpha() and 3 <= len(w) <= 10]

print(len(words))
