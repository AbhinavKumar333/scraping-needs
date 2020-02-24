import csv
import json
import re
# file = 'rsagg8'
file = 'science-6'
csvfile = open(file+'.csv', 'r')
jsonfile = open(file+'.json', 'w')

fieldnames = ('question_text','options','solution_text','question_no','book','grade','subject','path','chapter','exercise',)
# fieldnames = ('Book','Grade','Subject','Chapter','Exercise','Question number','Question','Answer','Link')
reader = csv.DictReader( csvfile, fieldnames)
data=[]
con = 1
for row in reader: 
    print con
    # print row['Link']
    grade = str(row['grade'])
    # grade = "Grade "+str(row['Grade'])
    # book = row['Subject']+" Grade "+str(row['Grade'])+" UP BOARD"
    book = row['book']
    if(row['book']=='book'):
        continue
    dic=""
    # dic1 = {"owning_partner_id":10304,"type":"Question","subtype":"SingleChoice","modifier":"Judgemental","status":"Pending Review","author_id":690,
    #         "assigned_to":690,"content":{"question_meta_tags":[{"difficulty_level":"","primary_concept":"","ideal_time":"","secondary_concept":[]}],
    #         "question_details":{"en":{"answers":[{"body":"opt1","is_correct":true,"explanation":"opt"},{"body":"2","is_correct":false,
    #         "explanation":""},{"body":"3","is_correct":false,"explanation":""},{"body":"4","is_correct":false,"explanation":""}],
    #         "question_txt":"hsllo"}},"book_meta_tags":[{"key":"Syllabus"},{"key":"Book"},{"key":"Grade"},{"key":"Edition"},
    #         {"key":"Author"},{"key":"Publication"},{"key":"Subject"},{"key":"Language"},{"key":"Code"},{"key":"Book ID"}]},
    #         "superseded_by":null,"language":"en","wf_info":{"id":70,"comments":[],"wf_step_no":1},"is_atg_ready":false,"created_by":690,
    #         "updated_by":690,"is_prof_approved":false,"content_schema_version":1,"version":1}
    
    dic1 = {"owning_partner_id":10304,"type":"Question","subtype":"Subjective","modifier":"Judgemental","status":"draft",
    "author_id":720,"content":{"question_meta_tags":[{"difficulty_level":"","primary_concept":"","ideal_time":"","secondary_concept":[]}],
    "question_details":{"en":{"answers":[{"body":"","is_correct":True,"explanation":row['solution_text']}],"question_txt":row['question_text']}},
    "book_meta_tags":[{"key":"Syllabus","value":"CBSE"},{"key":"Grade","value":grade},{"key":"Edition","value":"2019"},
    {"key":"Author","value":"NCERT"},{"key":"Publication","value":"NCERT"},{"key":"Subject","value":row['subject']},
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
    {"key":"Author","value":"NCERT"},{"key":"Publication","value":"NCERT"},{"key":"Subject","value":row['subject']},
    {"key":"Language","value":"English"},{"key":"question_number","value":row['question_no']},
    {"key":"Book","value":book},{"key":"Chapter","value":row['chapter']},
    {"key":"Exercise","value":row['exercise']}]},"superseded_by":None,"is_atg_ready":False,"created_by":720,
    "updated_by":720,"is_prof_approved":False,"content_schema_version":1,"version":1}
    options = "".join(row['options'].split())    
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
        if(len(opt)<5):
            print options
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
    global con
    con = con+1
for d in data:
    json.dump(d, jsonfile)
    jsonfile.write('\n')
