import logging
import os
from datetime import datetime
LOGFILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"
log_path =os.path.join(os.getcwd(),"logs",LOGFILE)
os.makedirs(log_path,exist_ok=True)
LOGFILEPATH=os.path.join(log_path,LOGFILE)

logging.basicConfig(
    filename=LOGFILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)


