import os


FILE_NAME = os.getenv('FILE_NAME', 'index')
PAGE = os.getenv('PAGE', '')
FORMAT = os.getenv('FORMAT', 'json')


def before_scenario(context, scenario):
    if 'stdout-all' in context.tags:
        # Set to immediately out rather than keep for fail
        stdout_capture = False


def after_scenario(context, scenario):
    if 'stdout-all' in context.tags:
        stdout_capture = True
