def append_update_log(prospect, log_message):
    if prospect.update_logs:
        prospect.update_logs += f"\n{log_message}"
    else:
        prospect.update_logs = log_message