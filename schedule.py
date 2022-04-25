from email import sendy
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.combining import AndTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger

scheduler = BackgroundScheduler()
# the two possible triggers for the jobs
def job_function1():
  sendy("pay")
  #transfer the amount of money that we would want 

def job_function2():
  sendy("investment")
  #transfer the amount of money that we would want 

trigger1 = AndTrigger([IntervalTrigger(weeks=1),
                      CronTrigger(day_of_week='sun')])
scheduler.add_job(job_function1, trigger1)
trigger2 = AndTrigger([IntervalTrigger(weeks=4),
                      CronTrigger(day_of_week='sun')])
scheduler.add_job(job_function2, trigger2)

#start()