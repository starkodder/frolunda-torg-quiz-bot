import requests,json,random
s=requests.Session()
all_questions=[]
while(len(all_questions)<19):
  questions=s.get("https://pear-vast-fish.cyclic.app/questions").json()
  if(not questions["questions"][0]["id"] in [x["questions"][0]["id"] for x in all_questions]):
    all_questions.append(questions)
  print(len(all_questions))
print(all_questions)

solutions={}
for questions in all_questions:
  for answer in range(0,10):
    print(str(answer),questions["questions"][answer])
    for i in range(0,3):
      r=s.post('https://pear-vast-fish.cyclic.app//validate', json={
          'session_id': s.get("https://pear-vast-fish.cyclic.app/questions").json()["session_id"],
          'answer'+str(answer+1): questions["questions"][answer]["answers"][i],
          'answer'+str(answer+1)+'_time':0,
          'quiz_challenge_answers': None,
          'quiz_challenge_id': 4,
          'question_batch_id': questions["questions"][0]["id"],
      })
      if(r.json()["correctAnswers"]==1):
        solutions[questions["questions"][answer]["id"]]=questions["questions"][answer]["answers"][i]
        break
print(solutions)

with open("solutions.json","w",encoding="utf8")as f:
  json.dump(solutions,f)

batch_id=s.get("https://pear-vast-fish.cyclic.app/questions").json()["session_id"]
json_data={
          'session_id': batch_id,
          'quiz_challenge_answers': None,
          'quiz_challenge_id': 4,
          'question_batch_id': all_questions[0]["questions"][0]["id"],
}
for i in range(0,10):
  json_data['answer'+str(i+1)]=solutions[all_questions[0]["questions"][0]["id"]+i]
  json_data["answer"+str(i+1)+"_time"]=30000#random.randint(29990,99500)#999999999
r=s.post('https://pear-vast-fish.cyclic.app//validate', json=json_data)
print(r.json())

json_data = {
    'nickname': "yourusername",##MAXLENGTH==30 åäö not allowed numbers allowed but not only numbers
    'email': "your@mail",#needs to be verified
    'phone': "0700000000",#your phn nr
    'sessionId': batch_id,
    'score': {
        'score': r.json()["score"],
        'correctAnswers': 10,
        'answerTime': r.json()["answerTime"],
    },
}

r=s.post('https://pear-vast-fish.cyclic.app//adduser', json=json_data)
print(r.json())
