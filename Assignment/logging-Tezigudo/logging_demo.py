"""
Examples of using Python's logging facility.

Run this file in Python and observe:
Which messages are actually printed on the console or to a file?
What information is in the message?

For details, see: https://docs.python.org/3/library/logging.html
"""
import logging


def log_demo(logger: logging.Logger):
    """Log messages using each of the standard logging levels.
       :param logger: a logging.Logger object for log messages.
    """

    # debug
    logger.debug("some bug happen")
    # info
    logger.info("process finished")
    # warning
    logger.warning("something is wrong but can work")
    # error
    logger.error("error occured during the process")
    # critical or fatal
    logger.fatal('Oh shXt program is going to down and fXck off')


def console_config():
    """Configure logging for messages sent to the console.

    You should call this before creating any logging objects.
    You can call basicConfig only once.   Subsequent calls have no effect.

    named attributes you can set using basicConfig are:

    filename = name of a file to send log messages to
    filemode = 'a' (append), 'w' (truncate & open for writing)
    format = a string describing format of log messages
    stream = name of a StreamHandler to use, cannot use with filename attribute
    level = the threshold level for log messages

    See:  help(logging.basicConfig)
    Ref:  https://docs.python.org/3/library/logging.html#logging.basicConfig
    """
    # define a custom format for log messages (use it in your
    # call to basicConfig)
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.WARNING)


def file_config():
    """Configure logging to a file."""
    #      and append mode so log files are not overwritten
    # Format should be "(asctime) (logger_name) (levelname) (funcName): (message)"
    # don't actually print the parenthesis in log messages!
    #
    # See: https://docs.python.org/3/library/logging.html#logrecord-attributes
    logging_format = "%(asctime)s %(name)s %(levelname)s %(funcName)s: %(message)s"

    # logging.LogRecord(filename="demo.log", filemode="a", format=logging_format, level=logging.DEBUG)
    logging.basicConfig(filename="demo.log", filemode="a",
                        format=logging_format, level=logging.DEBUG)


if __name__ == "__main__":
    # Call basicConfig with the default settings
    # logging.basicConfig()

    # Call basicConfig with a threshold logging level
    # logging.basicConfig(level=logging.ERROR)  -- fix this

    # Instead of the above, call your own config function:
    # console_config()
    #
    # or:
    file_config()
    # After configuring logging,
    # Log some messages to the root logger & observe the output.
    logger = logging.getLogger("demo")
    print("Logging to ", str(logger))
    log_demo(logger)

    # of the root logger.
