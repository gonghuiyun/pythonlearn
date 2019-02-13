import logging
import nni
#_logger = logging.getLogger("pytorch_mnist")

RCV_CONFIG = nni.get_next_parameter()
print(RCV_CONFIG)
#_logger.debug(RCV_CONFIG)
