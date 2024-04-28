# frolunda-torg-quiz-bot
Bots the frolunda torg quiz game at https://ft-quizwebclient.vercel.app/
Includes both python code and tampermonkey bot to scrape and solve all the questions in the quiz (some questions even included spell errors). 
The API enpoints that they used: 
https://pear-vast-fish.cyclic.app/highscore
https://pear-vast-fish.cyclic.app/weeklyhighscore
https://pear-vast-fish.cyclic.app/questions
https://pear-vast-fish.cyclic.app/validate

The actual game was an iframe inside https://frolundatorg.se/quiz : https://ft-quizwebclient.vercel.app/ 
The weekly score wasn't shown the last week, but the weeklyhighscore still returned last weeks highscores. 

The game sends you an email to the given mail address with a link to verify in the format of https://quiz.frolundatorg.se/approve/* with * representing a 96 char long hexadecimal string (this only works once per email, so you can't enter the same mail twice). The format of the mails are written in the file mailformat.txt. 

The scores as of 2024/04/28 22:00 are stored inside 22.json . 
