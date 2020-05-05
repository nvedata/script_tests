import sched, time
s = sched.scheduler(time.time, time.sleep)
ct = time.time()
t1 = ct + 5
t2 = ct + 10
s.enterabs(t1, 1, print, argument=(ct, t1, 'hello'))
s.enterabs(t2, 1, print, argument=(ct, t2, 'hello'))
s.run()
