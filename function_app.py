import azure.functions as func
import logging

app = func.FunctionApp()


@app.function_name("queue_function")
@app.queue_trigger(arg_name="azqueue", queue_name="test",
                               connection="QueueStorage") 
def queue_trigger(azqueue: func.QueueMessage):
    logging.info('Python Queue trigger processed a message: %s',
                azqueue.get_body().decode('utf-8'))
    send_email("prashantkumarll@gmail.com", "Pinku123*", "test email", azqueue.get_body().decode('utf-8'))
    

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print "successfully sent the mail"
    except:
        print "failed to send mail"


# AzureWebJobsStorage__accountName       False          testfuncpacificappn9585
# AzureWebJobsStorage__blobServiceUri    False          https://testfuncpacificappn9585.blob.core.windows.net
# AzureWebJobsStorage__credential        False          managedidentity
# AzureWebJobsStorage__queueServiceUri   False          https://testfuncpacificappn9585.queue.core.windows.net
# AzureWebJobsStorage__tableServiceUri   False          https://testfuncpacificappn9585.table.core.windows.net
# QueueStorage__blobServiceUri           False          https://test090890.blob.core.windows.net
# QueueStorage__credential               False          managedidentity
# QueueStorage__queueServiceUri          False          https://test090890.queue.core.windows.net
# QueueStorage__tableServiceUri          False          https://test090890.table.core.windows.net