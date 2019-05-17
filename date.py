from datetime import date, timedelta
team = ["ATD-B", "Architecture", "ATD-A", "Config", "Data", "M&M"]
delta = [timedelta(days=2), timedelta(days=5)]

start_date = date(2017,11, 1)
for i in xrange(5):
    idx = 0
    for t in team:
        print '|| %s || %s ||' %  (start_date, t)
        start_date += delta[idx]
        idx = (idx + 1) % 2
