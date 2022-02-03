# Takes string input
words= input("What string would you like to convert to morse code?\n")

# Surely a dictionary is the best way to do this
morse={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".",
"f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-",
"l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-",
"r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--",
"x":"-..-","y":"-.--","z":"--..","1":".----","2":"..---",
"3":"...--","4":"....-","5":".....","6":"-....","7":"--...",
"8":"---..","9":"----.","0":"-----",".":".","!":"!",",":","," ":" "}

# Empty list to append results of the following loop
result=[]

# String converted to lowercase to match dictionary, each letter converted to morse and appended to the list "result"
for x in words.lower():
        result.append(morse[x])

# printing joined result!
print("".join(result))
