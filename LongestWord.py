import re
highV = "" # o(1)
def LongestWord(sen):
  newString = re.sub('[^a-zA-Z0-9 \n\.]', '', sen) # 0(n)
  nArray = newString.split() # 0(n)
  for e in nArray: # 0(n)
    if len(e) > len(highV): # 0(1)
      highV = e # 0(1)
  return highV # 0(1)
  
  


# keep this function call here 
print(LongestWord("Hell%$#%$$o Worl#@#()d I !@!Am A Progr%&()ammer"))