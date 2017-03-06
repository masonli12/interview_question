from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
import unittest


fmt='%Y-%m-%d'

def next_draw_date(start_date=None, hour=20, draw_weekday=None):
    """
    assume same timezone

    :type start_date: datetime
    :type hour: num
    :type draw_weekday: list
    :rtype: str

    """

    if start_date is None:
        start_date = datetime.now()

    if draw_weekday is None:
        draw_weekday = [WE, SA]
    
    draw_date = [start_date+relativedelta(weekday=w, hour=hour) for w in draw_weekday]
    draw_date.sort()
    
    if start_date < draw_date[0]:
        return draw_date[0].strftime(fmt)
    else:
        return draw_date[1].strftime(fmt)


class TestNextDrawDate(unittest.TestCase):

    def test_expect_today(self):
        d = datetime.now()
        draw_weekday = [d.weekday(), (d.weekday()+3)%6]
        r = next_draw_date(hour=23, draw_weekday=draw_weekday)
        self.assertEqual(d.strftime(fmt), r)

    def test_not_today(self):
        d = datetime.now()
        draw_weekday = [d.weekday(), (d.weekday()+3)%6]
        r = next_draw_date(hour=d.hour-1, draw_weekday=draw_weekday)
        self.assertNotEqual(d.strftime(fmt), r)

    def test_defined_date_wed(self):
        d = datetime.strptime('2017-03-08', fmt)
        r = next_draw_date(d)
        self.assertEqual(d.strftime(fmt), r)

    def test_defined_date_mon(self):
        d = datetime.strptime('2017-03-06', fmt)
        r = next_draw_date(d)
        self.assertEqual('2017-03-08', r)

    def test_defined_date_fri(self):
        d = datetime.strptime('2017-03-10', fmt)
        r = next_draw_date(d)
        self.assertEqual('2017-03-11', r)



if __name__ == '__main__':
    unittest.main()
