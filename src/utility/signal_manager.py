from signal import signal, SIGINT
import sys

def signal_handler(self, sig, frame):
    """This method is used to define how the script handle the interruption.
    May use to stop some thread or destroy objects.
    Parameters
    ----------
    sig :
        The type of the signal
    frame :
        The frame argument is the stack frame, also known as execution frame. It point to the frame that was interrupted by the signal.
        The parameter is required because any thread might be interrupted by a signal, but the signal is only received in the main thread.
    Returns
    -------
    None
    """
    print("\nExit!")
    sys.exit(0)


