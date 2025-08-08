import syslog

syslog.openlog(ident="myapp", logoption=syslog.LOG_PID, facility=syslog.LOG_USER)

def log_info(message):
    syslog.syslog(syslog.LOG_INFO, message)

def log_warning(message):
    syslog.syslog(syslog.LOG_WARNING, message)

def log_error(message):
    syslog.syslog(syslog.LOG_ERR, message)

log_info("This is an info message.")
log_warning("This is a warning message.")
log_error("This is an error message.")