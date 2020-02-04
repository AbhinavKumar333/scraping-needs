import csv
import json
import re
# file = 'rsagg8'
file = 'maths_8'
csvfile = open(file+'.csv', 'r')
jsonfile = open(file+'.json', 'w')

fieldnames = ('question_text','options','solution_text','book','subject','grade','link','chapter','exercise','question_no')
# fieldnames = ('Book','Grade','Subject','Chapter','Exercise','Question number','Question','Answer','Link')
reader = csv.DictReader( csvfile, fieldnames)
data=[]
for row in reader:
    # print row['Link']
    grade = str(row['grade'])
    # grade = "Grade "+str(row['Grade'])
    # book = row['Subject']+" Grade "+str(row['Grade'])+" UP BOARD"
    book = 'RS Agarwal Class 11 Mathematics'
    if(row['book']=='book'):
        continue
    dic=""
    dic1 = {"owning_partner_id":10304,"type":"Question","subtype":"Subjective","modifier":"Judgemental","status":"draft",
    "author_id":720,"content":{"question_meta_tags":[{"difficulty_level":"","primary_concept":"","ideal_time":"","secondary_concept":[]}],
    "question_details":{"en":{"answers":[{"body":"","is_correct":True,"explanation":row['solution_text']}],"question_txt":row['question_text']}},
    "book_meta_tags":[{"key":"Syllabus","value":"CBSE"},{"key":"Grade","value":grade},{"key":"Edition","value":"2019"},
    {"key":"Author","value":"RS Aggarwal"},{"key":"Publication","value":"Bharti Bhawan"},{"key":"Subject","value":row['subject']},
    {"key":"Language","value":"English"},{"key":"question_number","value":row['question_no']},
    {"key":"Book","value":book},{"key":"Chapter","value":row['chapter']},
    {"key":"Exercise","value":row['exercise']}]},"superseded_by":None,"is_atg_ready":False,"created_by":720,
    "updated_by":720,"is_prof_approved":False,"content_schema_version":1,"version":1}

    dic2 = {"owning_partner_id":10304,"type":"Question","subtype":"SingleChoice","modifier":"Judgemental","status":"draft",
    "author_id":720,"content":{"question_meta_tags":[{"difficulty_level":"","primary_concept":"","ideal_time":"","secondary_concept":[]}],
    "question_details":{"en":{"answers":[{"body":"1st option","is_correct":True,"explanation":row['solution_text']},
    {"body":"2nd option","is_correct":False,"explanation":""},{"body":"3rd option","is_correct":False,"explanation":""},
    {"body":"4th option","is_correct":False,"explanation":""}],"question_txt":"Question Body"}},
    "book_meta_tags":[{"key":"Syllabus","value":"CBSE"},{"key":"Grade","value":grade},{"key":"Edition","value":"2019"},
    {"key":"Author","value":"RS Aggarwal"},{"key":"Publication","value":"Bharati Bhawan"},{"key":"Subject","value":row['subject']},
    {"key":"Language","value":"English"},{"key":"question_number","value":row['question_no']},
    {"key":"Book","value":book},{"key":"Chapter","value":row['chapter']},
    {"key":"Exercise","value":row['exercise']}]},"superseded_by":None,"is_atg_ready":False,"created_by":720,
    "updated_by":720,"is_prof_approved":False,"content_schema_version":1,"version":1}
    options = row['options']
    if(options=="NA"):
        dic = dic1
    elif(options==""):
        continue
    else:
        dic = dic2
        opt = re.split('[A-D]\.\s*',options)
        # print "------------------------------------------"
        a = opt[1]
        b = opt[2]
        c = opt[3]
        d = opt[4]
        # if(len(opt)!=4):
        #     print options
    # dic = {"owning_partner_id":10304,"type":"Question","subtype":"Subjective","modifier":"Judgemental","status":"draft",
    # "author_id":720,"content":{"question_meta_tags":[{"difficulty_level":"","primary_concept":"","ideal_time":"","secondary_concept":[]}],
    # "question_details":{"en":{"answers":[{"body":"","is_correct":True,"explanation":row['Answer']}],"question_txt":row['Question']}},
    # "book_meta_tags":[{"key":"Syllabus","value":"UP BOARD"},{"key":"Grade","value":grade},{"key":"Edition","value":"2019"},
    # {"key":"Author","value":"UP BOARD"},{"key":"Publication","value":"UP BOARD"},{"key":"Subject","value":row['Subject']},
    # {"key":"Language","value":"Hindi"},{"key":"question_number","value":row['Question number']},
    # {"key":"Book","value":book},{"key":"Chapter","value":row['Chapter']},
    # {"key":"Exercise","value":row['Exercise']}]},"superseded_by":None,"is_atg_ready":False,"created_by":720,
    # "updated_by":720,"is_prof_approved":False,"content_schema_version":1,"version":1}

#
    # break
    data.append(dic)
#     # print dic
for d in data:
    json.dump(d, jsonfile)
    jsonfile.write('\n')
