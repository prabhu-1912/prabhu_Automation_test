from datetime import datetime


class Common:
    def __init__(self, logger):
        self.logger = logger

    def check_diff_days(self, date_string, days_old) -> int:
        """
        Check two date diff and return integer days
        """
        self.logger.info("In check diff days ")
        fmt_date = datetime.strptime(" ".join(str(date_string).split()), "%m/%d/%Y %H:%MPM")
        now_time = datetime.now()
        delta = fmt_date - now_time
        self.logger.info("Delta days{}".format(delta.days))
        if delta.days <= days_old:
            return True
        else:
            return False
