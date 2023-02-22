

utc_dt = datetime.datetime.now(datetime.timezone.utc)
print("local time {}", format(utc_dt.astimezone().))