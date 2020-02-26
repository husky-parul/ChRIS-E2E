# Delete a pman job
import os
import configparser
import test_setup
import time
import pfurl
import json

class OpenShiftMgr:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('moc-health-check/config.cfg')

        self.RANGE = config.get('ConfigInfo', 'MAX_ATTEMPTS')
        self.SIZE = config.get('ConfigInfo', 'SIZE')
        self.TIMEOUT = config.get('ConfigInfo', 'TIMEOUT')
        self.THRESHOLD = config.get('ConfigInfo', 'FAILURE_THRESHOLD')
        self.PATH = os.getcwd()
        self.WAIT = int(config.get('ConfigInfo', 'INITIAL_WAIT'))
        self.PMAN_URL = config.get('ConfigInfo', 'PMAN_URL')
        self.PFIOH_URL = config.get('ConfigInfo', 'PFIOH_URL')
        self.JID = config.get('ConfigInfo', 'JID')
        self.attempts = 0
        self.DIR = 'files'
        self.password = config.get('ConfigInfo', 'PASSWORD')


    def job_delete(self):
        post_request = {"action": "delete",
            "meta":  {
                "key": "jid",
                "value": '"' + self.JID + '"'
            }
        }

        dataComs = pfurl.Pfurl(
                    msg                         = json.dumps(post_request),
                    verb                        = 'POST',
                    http                        = '%s/%s' % (self.PMAN_URL, "api/v1/cmd"),
                    b_quiet                     = False,
                    b_raw                       = True,
                    b_httpResponseBodyParse     = True,
                    jsonwrapper                 = '',
                    authToken                   = self.password
        )

        return (json.loads(dataComs()))

    # Upload data to swift 
    def run_pfioh_push(self):
        post_request = { "action": "pushPath",
        "meta": {
            "remote": {
                "key": self.JID 
                },
            "local": {
                "path":        "/tmp/" + self.DIR
                },
            "transport": {
                "mechanism":   "compress",
                "compress": {
                    "archive": "zip",
                    "unpack":   True,
                    "cleanup":  True
                    }
                }
            }
        }
        dataComs = pfurl.Pfurl(
                    msg                         = json.dumps(post_request),
                    verb                        = 'POST',
                    http                        = '%s/%s' % (str(self.PFIOH_URL), "api/v1/cmd"),
                    b_quiet                     = False,
                    b_raw                       = True,
                    b_httpResponseBodyParse     = True,
                    jsonwrapper                 = '',
                    authToken                   = self.password
        )
        return (json.loads(dataComs()))

    # Run a job in Pman
    def pman_run(self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$ run pman called?")
        post_request = {   "action": "run",
            "meta":  {
                "cmd": "simpledsapp.py --prefix test- --sleepLength 0 /share/incoming /share/outgoing",
                "auid": "mochealthcheck",
                "jid": '"' + self.JID + '"',
                "threaded": True,
                "container": {
                        "target": {
                            "image" : "fnndsc/pl-simpledsapp"
                        }
                }
            }
        }

        dataComs = pfurl.Pfurl(
                    msg                         = json.dumps(post_request),
                    verb                        = 'POST',
                    http                        = '%s/%s' % (self.PMAN_URL, "api/v1/cmd"),
                    b_quiet                     = False,
                    b_raw                       = True,
                    b_httpResponseBodyParse     = False,
                    jsonwrapper                 = 'payload',
                    authToken                   = self.password
        )
        return (json.loads(dataComs()))

    def run_pman_status(self):
        post_request = {"action": "status",
                        "meta":  {
                            "key": "jid",
                            "value": '"' + self.JID + '"'
                            }
                        }


        dataComs = pfurl.Pfurl(
                    msg                         = json.dumps(post_request),
                    verb                        = 'POST',
                    http                        = '%s/%s' % (self.PMAN_URL, "api/v1/cmd"),
                    b_quiet                     = False,
                    b_raw                       = True,
                    b_httpResponseBodyParse     = False,
                    jsonwrapper                 = 'payload',
                    authToken                   = self.password
        )

        return (json.loads(dataComs()))

    # Downlad data from swift
    def run_pfioh_pull(self):
        post_request = {"action": "pullPath",
                        "meta": {
                            "remote": {
                                "key":  '"' + self.JID + '"'
                            },
                            "local": {
                                "path":         "/tmp/" + self.DIR,
                                "createDir":    True
                            },
                            "transport": {
                                "mechanism":    "compress",
                                "compress": {
                                    "archive":  "zip",
                                    "unpack":   True,
                                    "cleanup":  True
                                }
                            }
                        }
                    }

        dataComs = pfurl.Pfurl(
                    msg                         = json.dumps(post_request),
                    verb                        = 'POST',
                    http                        = '%s/%s' % (self.PFIOH_URL, "api/v1/cmd"),
                    b_quiet                     = False,
                    b_raw                       = True,
                    b_httpResponseBodyParse     = True,
                    jsonwrapper                 = '',
                    authToken                   = self.password
        )
        print(dataComs())

        return (json.loads(dataComs()))