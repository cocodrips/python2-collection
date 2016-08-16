import xmlrpclib

def send_simple_mail(send_from, send_to, send_cc, subject, body):
    proxy = xmlrpclib.ServerProxy('mail_server')
    proxy.send(send_from, send_to, send_cc, '', subject, body)
