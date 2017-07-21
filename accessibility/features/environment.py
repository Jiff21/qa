import os

FILE_NAME = os.getenv('FILE_NAME', 'index')


def before_scenario(context, scenario):
    # Not working
    if 'stdout-all' in context.tags:
        # Capture means keep for fail
        stdout_capture = False


def after_scenario(context, scenario):
    if 'stdout-all' in context.tags:
        stdout_capture = True
