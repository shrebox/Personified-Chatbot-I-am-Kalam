import json
import re
from rake_nltk import Rake

def cleantext(text):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', text)
  return cleantext

r = Rake() 

with open('final_qna.json', 'r') as f:
    qadict = json.load(f)    
    for index in qadict:	
	qadict[index]['ques']=cleantext(qadict[index]['ques'].strip())
	qadict[index]['ans']=cleantext(qadict[index]['ans'].strip())

    	tag=r.extract_keywords_from_text(qadict[index]['ques'])
	ranked_tags=r.get_ranked_phrases()
	if 'tag' not in qadict[index]:
		qadict[index]['tag']=ranked_tags

    data=json.dumps(qadict)
    with open("ques_ans2.json","w") as f:
            f.write(data) 

