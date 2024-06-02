# frolunda-torg-quiz-bot
Bots the frolunda torg quiz game at https://ft-quizwebclient.vercel.app/ . 
Includes both python code and tampermonkey bot to scrape and solve all the questions in the quiz (some questions even included spelling errors). 
The API enpoints that were used: 
https://pear-vast-fish.cyclic.app/highscore (contains the 10 highest scores of all time)
https://pear-vast-fish.cyclic.app/weeklyhighscore (contains the 5 highest scores of the week or the scores of the previous week the last week)
https://pear-vast-fish.cyclic.app/questions (gives 10 random questions from 1 of 19 questiongroups and one of five challenge questions (stored in utslagning.json))
https://pear-vast-fish.cyclic.app/validate (the endpoint was used to calculate the score and questions that was right)
https://pear-vast-fish.cyclic.app/adduser (the endpoint that is used to send all contact details to the server along with the score)
(the christmasrhyme bot which used the chatgpt API was also deployed on cyclic)

The actual game was an vercel app iframed inside of https://frolundatorg.se/quiz : https://ft-quizwebclient.vercel.app/ 
The weekly score wasn't shown the last week, but the weeklyhighscore still returned last weeks highscores. All solutions to the questions are stored in solutions.json. 

The game sends you an email to the given mail address with a link to verify in the format of https://quiz.frolundatorg.se/approve/* with * representing a 96 char long hexadecimal string (this only works once per email, so you can't enter the same mail twice). The format of the mails are written in the file mailformat.txt. You get redirected to https://ft-quizwebclient.vercel.app/tack when you get a high score. 

The scores as of 2024/04/28 22:00 are stored inside 22.json and the weekly scores of 2024/04/28 are stored in weekly.json. 
Edit 22:20: getting this now: Error error: remaining connection slots are reserved for non-replication superuser connections
