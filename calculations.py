import statistics

def calculate_uptime(heartbeats):
    first_heartbeat = heartbeats[0].sent_at
    last_heartbeat = heartbeats[len(heartbeats) -1].sent_at
    sum_heartbeats = len(heartbeats)
    return (sum_heartbeats / ((last_heartbeat-first_heartbeat).total_seconds() / 60)) * 100

def calculate_time_duration(array_of_upload_time_durations):
    mean_nanoseconds =  statistics.mean(array_of_upload_time_durations)
    seconds = mean_nanoseconds / 1_000_000_000
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{int(minutes)}m{remaining_seconds:.9f}s"