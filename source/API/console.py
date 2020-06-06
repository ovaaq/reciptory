from datetime import datetime


def log(message: str) -> None:
    """
    Adds date and time to message that is printed.

    :param message: Any message wanted to log
    :return: None
    """
    # TODO: feature/CONSOLE-LOG
    #  *Save logs somewhere
    #  *Methods to search from the log
    #  *API for the logs
    print(str(datetime.now()) + " : " + message)
