from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval', hours=1)
def timed_job():
    from request import get_newest_json

sched.start()
