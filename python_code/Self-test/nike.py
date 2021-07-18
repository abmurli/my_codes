import logging
param = "INFO"
log_level = f'logging.{param}'

logging.basicConfig(level=logging.INFO, filename='test.log',
                    format='Date-Time : %(asctime)s : %(levelname)s :: s%(message)s')
logging.info("hello")
