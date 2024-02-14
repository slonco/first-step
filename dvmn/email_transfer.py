import smtplib
import os


template = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

sender_email = 'slonco90@yandex.ru'
recipient_email = 'slonco90@yandex.ru'
friend_name = 'Вася'
my_name = 'Сергей'
website = 'https://dvmn.org/referrals/bthgUVCQtH3EstUjWuYSpCH9sqXLGTDbxCOrhGwo/'

template = template.replace('%website%', website)
template = template.replace('%friend_name%', friend_name)
template = template.replace('%my_name%', my_name)

letter = """\
From: {sender_email}
To: {recipient_email}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

{template}""".format(template=template, sender_email=sender_email, recipient_email=recipient_email)

letter = letter.encode("UTF-8")
smtp_login= os.getenv("SMTP_LOGIN") # нужно подключить env с паролями
smtp_password = os.getenv("SMTP_PASSWORD") # нужно подключить env с паролями

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(smtp_login, smtp_password)
server.sendmail(sender_email, recipient_email, letter)
server.quit()