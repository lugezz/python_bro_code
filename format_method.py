# Format method Insert the price inside the placeholder, 
# the price should be in fixed point, two-decimal format:

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
print(txt1)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
print(txt2)
txt3 = "My name is {}, I'm {}".format("John", 36)
print(txt2)


import random

nouns = ("puppy", "car", "rabbit", "girl", "monkey")
verbs = ("runs", "hits", "jumps", "drives", "barfs") 
adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
adj = ("adorable", "clueless", "dirty", "odd", "stupid")

funny_sentence = "The {} {} {} {}".format(random.choice(nouns), random.choice(verbs), random.choice(adj), random.choice(adv))
print(funny_sentence)
