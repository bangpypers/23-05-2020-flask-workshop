import logging
import logging.handlers

def setup_logging(app):
    logger = app.logger
    logger.setLevel(app.config.get("LOG_LEVEL", logging.NOTSET))

    if app.config.get("LOGFILE") is not None:
        log_file = app.config.get("LOGFILE")
        handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=app.config.get("LOG_SIZE", 1024**3),
            backupCount=app.config.get("LOG_BACKUP", 10))
        formatter = logging.Formatter(
            fmt="[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            datefmt="%Y-%m-%d,%H:%M:%S")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
