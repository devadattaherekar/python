import logging
import arithmetic as ar

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create stream handler and set level to debug
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

# create file handler and set level to debug
fh = logging.FileHandler("storage_logs.txt")
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s;%(name)s;%(levelname)s;%(message)s","%d/%m/%Y %H:%M:%S")

# add formatter to stream handler
sh.setFormatter(formatter)
# add formatter to file handler
fh.setFormatter(formatter)

# add stream handler to logger
logger.addHandler(sh)
# add file handler to logger
logger.addHandler(fh)

# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")

var1=100
var2=200
logging.info(f"Addition {var1}  and {var2} is {ar.add(var1,var2)}")