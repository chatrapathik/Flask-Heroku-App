from heroku import app
from twisted.python import log
from sys import exit as sys_exit

from heroku.configs import app_config


class AppRunner:
    def __init__(self):
        pass

    @staticmethod
    def run_with_twisted(port, mode):
        """
        Import twisted dependencies, set app as WSGIResource and start reactor.
        """
        try:
            from twisted.internet import reactor
            from twisted.web.server import Site
            from twisted.web.wsgi import WSGIResource
            from appoptics_apm.middleware import AppOpticsApmMiddleware

            app.debug = mode
            env = app_config.configs.get("app", {}).get("env", "dev")
            if env == "prod":
                app.wsgi_app = AppOpticsApmMiddleware(app.wsgi_app)

            resource = WSGIResource(reactor, reactor.getThreadPool(), app)
            site = Site(resource)
            observer = log.PythonLoggingObserver(loggerName="logname")
            observer.start()
            reactor.listenTCP(port, site, interface="0.0.0.0")
            reactor.run()

        except ImportError:
            sys_exit(1)

    @staticmethod
    def run_with_builtin(port, mode):
        """
        Run with default builtin flask/klein/bottle app
        """
        app_config.logger.info(
            "Built-in development server on port {port} ...".format(port=port)
        )
        app.run(host="0.0.0.0", port=port, debug=mode)

    def main(self, port, mode, run_method):
        if run_method == "twistd":
            AppRunner.run_with_twisted(port, mode)
        else:
            AppRunner.run_with_builtin(port, mode)


runner = AppRunner()
