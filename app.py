from model import spell_check

title = """
   _____               _  _   _____  _                  _    
  / ____|             | || | / ____|| |                | |   
 | (___   _ __    ___ | || || |     | |__    ___   ___ | | __
  \___ \ | '_ \  / _ \| || || |     | '_ \  / _ \ / __|| |/ /
  ____) || |_) ||  __/| || || |____ | | | ||  __/| (__ |   < 
 |_____/ | .__/  \___||_||_| \_____||_| |_| \___| \___||_|\_\\
         | |                                                 
         |_|                                                 
"""
print(title)
raw = input("Enter text: ")

res = []

for word in raw.split():
    c_word = spell_check(word)
    res.append(c_word)

print(" ".join(res))

