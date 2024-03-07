from loguru import logger
import sys
# Set up where to output the logs. Here, we are using stdout
logger.remove()
logger.add(sys.stdout, serialize=True)
logger.debug("Starting application")
# Add context to logger by modifying the extra record attribute
ctx_log = logger.bind(service="my_service")
ctx_log.info("Starting my_service")
my_service_err = "my_service is not responding"
ctx_log = ctx_log.bind(err=my_service_err)
ctx_log.error('Fail to start my_service: {my_service_err}')