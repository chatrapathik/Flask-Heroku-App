import os
import logging
import logging.config

from simpleconfigparser import simpleconfigparser


class Config:
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    config_parser = simpleconfigparser()
    env_var_name = "DATA-CREATION-CONFIG"

    def __init__(self):
        self.configs = self.read_config(self.APP_ROOT + os.sep + "config.ini")
        self.logger = self.configure_logger()

        if self.env_var_name in os.environ:
            self.override_default_config()

    def override_default_config(self):
        custom_config_path = os.environ.get(self.env_var_name)
        self.configs.update(self.read_config(custom_config_path))

    def read_config(self, config_file_path):
        self.config_parser.read(config_file_path)
        return {
            s: dict(self.config_parser.items(s, True))
            for s in self.config_parser.sections()
        }

    def configure_logger(self):
        if "log" in self.configs and "path" in self.configs.get("log"):
            logging.config.fileConfig(
                self.APP_ROOT + os.sep + self.configs.get("log").get("path")
            )
            return logging.getLogger("root")
        else:
            print("Logging configuration failed.")


app_config = Config()
