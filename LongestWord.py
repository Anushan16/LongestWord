import re
def LongestWord(sen):
  #use RegEx to remove all special characters from string 
  newString = re.sub('[^a-zA-Z0-9 \n\.]', '', sen) # 0(n)
  #use the split method to turn sen into a array, called nArray
  nArray = newString.split() # 0(n)
  # initiate a variable to keep the element with the longest length
  highV = "" # o(1)
  #loop through each element in nArray 
  for e in nArray: # 0(n)
    #if current element is greater that the len of highV... highV = e (current element)
    if len(e) > len(highV): # 0(1)
      highV = e # 0(1)
  # at the end of the for loop return highV
  return highV # 0(1)
  
  


# keep this function call here 
print(LongestWord("Hell%$#%$$o Worl#@#()d I !@!Am A Progr%&()ammer"))