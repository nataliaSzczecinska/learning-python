import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="./module_4/logfile.log")
def print_maturity(age):
    if age >= 18:
        logging.info("You are an adult")
    else:
        logging.info("You are a kiddo!")

if __name__ == "__main__":
    logging.debug(f"The program was called with this parameters {sys.argv[1:]}")
    logging.debug(f"First parameter is {sys.argv[1]}")
    age = int(sys.argv[1])
    print_maturity(age)
