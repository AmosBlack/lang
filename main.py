from fnmatch import translate
from textblob import TextBlob as tb

str = tb("funy things arr not funny")
str_cr = str.correct()

print(str_cr, str_cr.translate(from_lang="en", to ="hi"))


