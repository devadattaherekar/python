import logging
import arithmetic as ar

logging.basicConfig(
                        filename="storage_logs.txt",
                        level=logging.INFO,
                        datefmt='%d-%m-%Y %H:%M:%S',
                        format='%(asctime)s %(levelname)s %(lineno)d %(filename)10s %(message)s'
                    )
logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")

var1=100
var2=200
logging.info(f"Addition {var1}  and {var2} is {ar.add(var1,var2)}")
