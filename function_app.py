import azure.functions as func
import logging

app = func.FunctionApp()


@app.function_name("queue_function")
@app.queue_trigger(arg_name="azqueue", queue_name="test",
                               connection="QueueStorage") 
def queue_trigger(azqueue: func.QueueMessage):
    logging.info('Python Queue trigger processed a message: %s',
                azqueue.get_body().decode('utf-8'))
