from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from the_emailsend import *


def job_function():
    sendy("pay")

trest = BlockingScheduler()
# Schedule job_function to be called every two hours
trest.add_job(job_function, 'interval', minutes=1, id="jim")
trest.start()