import argparse
import logging


class Coroner:
    """ Main Coroner Class"""

    def __init__(self):
        logging.debug("Coroner Constructed")


if __name__ == "__main__":
    logging.basicConfig(format="[%(levelname)s] %(filename)s:%(lineno)s: %(message)s", level=logging.DEBUG)

    coroner = Coroner()
