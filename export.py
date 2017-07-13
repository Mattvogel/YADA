import os
import time
import requests
from datetime import datetime
def __init__(self, context, mandatory_options=['apitoken']):
    self.uri = 'https://export.yammer.com/api/v1/export'
    sef.nextrun = 0

def get_zipfile(self):
    return os.path.join(self.workingdir, 'yammer.zip')

def start_backup_job(self, context):
        '''
        Yammer data export
        '''
        since = 0
        statefile = self.get_statefile()

        if os.path.isfile(statefile):
            with open(statefile, 'r') as f:
                ts = f.read()
                since = datetime.fromtimestamp(float(ts)).isoformat()


        try:
            r = requests.get(self.uri, headers={
                'Authorization':"Bearer %s" % self.options['apitoken']},
                params={'since': since}, stream=True, timeout=(5.0, 7200.0))

            if not r.ok:
            zipfile = self.get_zipfile()
            with open(zipfile, 'w') as fh:
                for chunk in r.iter_content(chunk_size=None):
                    fh.write(chunk)

            self.options['zipfile'] = zipfile
