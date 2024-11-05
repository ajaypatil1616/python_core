#what is 
#why :simplifies search
#where :
#1. find a matching pattern(String) in a string(para)
#2. mobile number and email verification
#3. web scraping : to get particular data from url 

import re 

#RegEx can be used to check if a string contains the specified search pattern.

#methods
#1.findall:	Returns a list containing all matches
#2.search : Returns a Match object if there is a match anywhere in the string
#3.split  : Returns a list where the string has been split at each match
#4.sub	: Replaces one or many matches with a string
#5.match(): Determine if the RE matches at the beginning of the string.
#6.finditer() :Find all substrings where the RE matches, and returns them as an iterator.
#              function to find all matches in a string and return an iterator that yields match objects.
#7.re.compile() : Regular expressions are compiled into pattern objects

s = 'Readability counts.'
pattern = r'[aeoui]'

matches = re.finditer(pattern, s)
# print(matches)# returns a object of finditer
for match in matches:
    print(match)


pattern = "the"
text = """
The sun rose lazily over the horizon, casting a warm golden hue across the tranquil countryside. Birds chirped melodiously, their songs echoing through the crisp morning air. As dawn broke, the sleepy village began to stir to life, its narrow cobblestone streets gradually filling with bustling activity. Farmers emerged from their quaint cottages, ready to tend to their fields and livestock, while the aroma of freshly baked bread wafted from the local bakery, enticing passersby with its irresistible scent. Children laughed and played in the meadows, their innocent joy a testament to the simple pleasures of rural life. In the distance, the majestic peaks of towering mountains loomed, their snow-capped summits glistening in the early light. It was a scene of serenity and tranquility, a picturesque tableau untouched by the chaos of the modern world.
However, beneath the idyllic surface lay a community grappling with its own trials and tribulations. For years, the village had relied on agriculture as its primary source of livelihood, but changing weather patterns and erratic rainfall had begun to take their toll on the crops, leaving many families struggling to make ends meet. The younger generation, lured by the promise of better opportunities in the bustling cities, were leaving in droves, leaving behind aging parents and dwindling hopes for the future. Despite their resilience and unwavering spirit, the villagers knew that their way of life was under threat, and they faced an uncertain future with a mixture of trepidation and determination.
Amidst the challenges, however, there were glimmers of hope and resilience. The community had come together to explore alternative sources of income, from eco-tourism to artisanal crafts, breathing new life into age-old traditions and fostering a sense of pride in their cultural heritage. Local leaders worked tirelessly to advocate for government support and investment in infrastructure, hoping to create new opportunities for growth and development. And in the face of adversity, the villagers leaned on each other for support, drawing strength from their shared history and collective determination to overcome whatever obstacles lay in their path.
As the day wore on and the sun climbed higher in the sky, the village buzzed with activity, its streets alive with the sounds of commerce and camaraderie. Farmers exchanged stories and tips at the bustling market square, while children frolicked in the cool shade of ancient oak trees. Elderly couples sat on weathered benches, watching the world go by with a mixture of nostalgia and quiet contentment. It was a scene of resilience and hope, a testament to the indomitable spirit of a community bound together by tradition, hardship, and an unwavering belief in the power of human connection.
As the sun dipped below the horizon and darkness descended upon the village, a sense of peace settled over the landscape, a reminder that even in the face of adversity, there was beauty to be found, and hope to be cherished. And as the stars twinkled overhead, casting their gentle glow upon the earth below, the villagers knew that no matter what challenges lay ahead, they would face them together, with courage, resilience, and a steadfast determination to preserve the way of life they held dear.
"""

# match = re.search(pattern, text)
# print(match)

# match = re.split(pattern, text)
# print(match[0])
# print(match[1])

# match = re.findall(pattern, text)
# print(match)

# match = re.sub("\s","a",text) # substitues the space with "a"
# print(match)
 

##
#MetaCharacters
#1. \ : used to drop special meaning of character following it
#2. [] : represent a character class/set
#3. ^ :(caret) Matches the beginning #caret
#4. $ : Matches the end 
#5. . : matches any character except newline
#6. | : means OR 
#7. ? : Matches zero or one occurrence
#8. * : Any number of occurences(including 0 occurrences)
#9. + : One or more occurrences
#10. {} : Indicates the number of occurrences of preceding regex to match
#11. () : Enclose a group of regex


a = "charlie and the aj.z ay1z adsz chaocolatez fchactzory"
b = "ayushi.jain@gmail.com"
c = "hello"
d = "xyz,yz,xyyz,xxzzy,zyz, xxyyzz, xyzxyz xxxxxxxyyz"

# match = re.findall(r"(x|z)yz",d)
# print(match)

# match = re.findall(r"x{2,4}",d)
# print(match)


# match = re.findall(r"xy+z",d) # occurence of y does not matter here
# print(match)

# match = re.findall(r"ch*a",a) 
# print(match)

# match = re.findall(r"ch?a",a)
# print(match)

# match = re.findall(r"ch|fact|a",a)
# print(match)

# match = re.findall(r"a..z",a)
# print(match)

# match = re.search(r"llo$",c)
# print(match)

# match = re.search(r"^ayui",b)
# print(match)

# match = re.search(r"[@]",b)
# print(match)

# match = re.search(r"\.",b)
# print(match)


## SETS
# \{n,\} :Quantifies the preceding character or group and matches at least n occurrences.
#[012345] : matches the specified digits(012345)
#[^arn] :matches any character except a,r,n
# [arn] : matches the specified chara (a,r,n)
# \d : matches any digit(0-9)
# \D : matches any non digit character
# \w : matches any word character 
# \W : matches any character ie not word char(digit matches)
# [0-5][0-9] :matches any two number from 00 to 59
# \w : matches any alhpanumeric character {a-z,A-Z,0-9 or _}
# [a-n] :matches any lower case alphabet between a to n
# [a-z][A-Z] : matches any character between a to z OR A to Z


# solve the examples of 
# 2aplhha + 3beta + 4 gyamma


#examples :
html = """
<html>
<head>
<title>Sample HTML Document</title>
</head>
<body>
<h1>Welcome to my HTML Document</h1>
<p>This is a paragraph.</p>
<div class="container">
    <p>This is another paragraph inside a div.</p>
    <a href="https://example.com">Link</a>
</div>
</body>
</html>"""

match = re.findall(r'<[^>]+>',html)
print(match)


