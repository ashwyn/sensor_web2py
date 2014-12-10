def send():

    sendemail(from_addr    = 'piscriptip@gmail.com',
          to_addr_list = ['ashwyn1092@gmail.com'],
          cc_addr_list = [],
          subject      = 'Howdy',
          message      = 'Howdy from a python function',
          login        = 'piscriptip@gmail.com',
          password     = 'piscriptip14')

    return "sending...."


def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):

    import smtplib

    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems