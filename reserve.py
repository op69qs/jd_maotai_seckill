from apscheduler.schedulers.blocking import BlockingScheduler
from jd_spider_requests import JdSeckill


def reserve():
    jd_seckill = JdSeckill()
    jd_seckill.reserve()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(reserve, 'cron', hour=11, minute=17)
    scheduler.start()