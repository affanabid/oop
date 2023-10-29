from lab3 import TimeSpan, TimeSpan2

time_span = TimeSpan(2, 30)
time_span.show()

print()

time_span.add_hours(2)

print()

time_span.add_minutes(40)

print()
time_span = TimeSpan(2, 30)
ts = TimeSpan(7, 45)
time_span.change(ts)

print('---------------------')

time = TimeSpan2(150)
time.show()

print()

time.add_hours(2)

print()

time.add_minutes(40)

print()

time = TimeSpan2(150)
ts = TimeSpan2(465)
time.change(ts)