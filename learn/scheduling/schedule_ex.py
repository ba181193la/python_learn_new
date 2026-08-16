import schedule
import time


def cancel_expired_orders():
    print("Checking expired orders...")
    print("Expired orders cancelled")


schedule.every(10).seconds.do(cancel_expired_orders)


while True:
    schedule.run_pending()
    time.sleep(1)