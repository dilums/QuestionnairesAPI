import json

with open('api/data/data.json') as json_file:  
    data = json.load(json_file)

def get_set_by_qusetion_id(question_id):
        question_id = str(question_id)
        try:
            if len(data['qusestions'][question_id]['anwsers']) == 0:
                return {'finish':True, 
                        'message': data['qusestions'][question_id]['text']}
            else:
                return {'qusestion':data['qusestions'][question_id]['text'], 
                        'anwsers':[{'text':data['anwsers'][i]['text'], 'id':i} 
                    for i in data['qusestions'][question_id]['anwsers']]}
        except Exception as e:
            return {'finish':True, 'message': 'error occured ( question id)'}

def get_set_by_anwser_id(anwser_id):
    try:
        anwser_id = str(anwser_id)
        return get_set_by_qusetion_id(data['anwsers'][anwser_id]['next'])
    except Exception as e:
        return {'finish':True, 'message': 'error occured (anwser id)'}
        
def get_question_text_by_id(question_id):
    return data['qusestions'][question_id]['text']

def get_anwser_text_by_id(anwser_id):
    return data['anwsers'][anwser_id]['text']

def get_question_list():
    return [ {'category':category['category'],
            'questions':[{
                'id':question, 
                'text':get_question_text_by_id(question)} 
                for question in category['questions']]
            } for category in data['lists']]
            
def get_text(item):
    if (item['type'] == 'anwser'):
        return get_anwser_text_by_id(item['id'])
    else:
        return get_question_text_by_id(item['id'])

def create_log(data):
    return ' -> '.join([get_text(item) for item in data])