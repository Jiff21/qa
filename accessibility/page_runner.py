import subprocess
from qa.accessibility.features.environment import FILE_NAME
from qa.environment_variables import PAGES_LIST, BASE_URL, QA_FOLDER_PATH


# Adding home to the page list as it works here.
all_pages = PAGES_LIST
all_pages.append('/')

for page in all_pages:
    generated_command = ''
    if page == '/':
        generated_command = 'docker run \
            -v $PWD/%saccessibility/output/:/lighthouse/output/  \
            -i matthiaswinkelmann/lighthouse-chromium-alpine \
            --output json --output html \
            --output-path=/lighthouse/output/%s %s%s' % (
            QA_FOLDER_PATH,
            FILE_NAME,
            BASE_URL,
            page
        )
        print (generated_command)
    else:
        generated_command = 'docker run \
            -v $PWD/%saccessibility/output/:/lighthouse/output/  \
            -i matthiaswinkelmann/lighthouse-chromium-alpine \
            --output json --output html \
            --output-path=/lighthouse/output%s %s%s' % (
            QA_FOLDER_PATH,
            page,
            BASE_URL,
            page
        )
        print (generated_command)
    process = subprocess.Popen(
        generated_command,
        stderr=subprocess.STDOUT,
        shell=True
    )
    process.wait()

for page in all_pages:
    generated_command = ''
    if page == '/':
        generated_command = 'FILE_NAME=%s behave %saccessibility/features' % (
            'index',
            str(QA_FOLDER_PATH)
        )
    else:
        generated_command = 'FILE_NAME=%s behave %saccessibility/features' % (
            page.replace('/', ''),
            QA_FOLDER_PATH
        )
        print('4 In run behave page' + generated_command)
    process = subprocess.Popen(
        generated_command,
        stderr=subprocess.STDOUT,
        shell=True
    )
    process.wait()
