from datetime import datetime


def log(message: str) -> None:
    """
    Adds date and time to message that is printed.

    :param message: Any message wanted to log
    :return: None
    """
    print(str(datetime.now()) + " : " + message)

def exception(exception: Exception) -> None:
    """
    Adds date and time to message that is printed.

    :param exception: Any exception wanted to log
    :return: None
    """
    print(str(datetime.now()) + " :      " + exception.__str__())

    # TODO: feature/CONSOLE-LOG
    #  *Save logs somewhere
    #  *Methods to search from the log
    #  *API for the logs
