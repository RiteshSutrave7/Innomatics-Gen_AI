# 2: Search Query Keyword Analysis
query="Buy mobile phone buy phone online"
# converting query to lower case
lower_query=query.lower()
# ignore common punctuation
#split into words
words=lower_query.replace('"','').replace('.','').replace(',','').split()
# count the frequency of each keyword
word_counts={}
for word in words:
    if word in word_counts:
        word_counts[word]+=1
    else:
        word_counts[word]=1
# 
# Display only keywords searched more than once
result={word:count for word,count in word_counts.items() if count>1}
print(result)