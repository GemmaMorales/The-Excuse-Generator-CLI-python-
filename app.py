import random 

print("hello world")


who = ["the dog", "My brother", "A nail"]
action = ["ate", "ripped", "slashed"]
what = ["my homework", "my rent check", "my tire"]
when = ["yesterday", "two days ago", "when I was on my way to work"]
excuse = who[random.randint(0,2)] + " " + action[random.randint(0,2)] + " " + what[random.randint(0,2)] + " " + when[random.randint(0,2)]
print(excuse)

