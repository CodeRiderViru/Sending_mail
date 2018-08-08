import smtplib
 
server1 = smtplib.SMTP('smtp.gmail.com',587)
server1.ehlo()
server1.starttls()
server1.login('Your Email Here', 'Your Password Here')
 
msg = " Your Msg Here "
server1.sendmail('your email here', 'Reciever email here', msg)
server1.quit()
