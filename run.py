import optparse

from heroku import runner


def main():
    """
    Parse the options to get WSGi container of choice, the debug mode, and the port number"
    """
    parser = optparse.OptionParser(usage="%prog [options]  or type %prog -h (--help)")

    parser.add_option(
        "-p",
        "--port",
        help="Port on which to run service, defaults to 5050",
        dest="app_port",
        type="int",
        default=5050,
    )

    parser.add_option(
        "--debug",
        help="When passed, sets app in debug mode",
        dest="debug_mode",
        action="store_true",
        default=False,
    )

    parser.add_option(
        "-w",
        "--with",
        type="choice",
        action="store",
        dest="app_container",
        choices=["builtin", "twistd"],
        default="builtin",
        help="WSGI container to be used to wrap and run the app. "
        "Valid options - builtin/tornado/twistd. Defaults to builtin",
    )
    (options, args) = parser.parse_args()
    runner.main(
        port=options.app_port, mode=options.debug_mode, run_method=options.app_container
    )


if __name__ == "__main__":
    main()
