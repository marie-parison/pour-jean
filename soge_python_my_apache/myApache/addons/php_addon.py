from api import Addon, HTTPResponse, parse_php_response
import os
import sys
import subprocess

class php_addon(Addon):
    #def configure(self, configuration):
    #Accepter POST ou GET
    # var dump $_SERVER dans apache
    
    def execute(self, duplex):

        ROOTPATH = os.path.dirname(os.path.abspath(sys.argv[0]))
        
        if duplex.request.uri.endswith(".php") :
            env = dict()
            env["SCRIPT_NAME"] = ROOTPATH + '/www/'
            env["SCRIPT_FILENAME"] = ROOTPATH + '/www/' + duplex.request.uri
            env["GATEWAY_INTERFACE"] = "CGI/1.1"
            env["REDIRECT_STATUS"] = "true"
            
            print(env["SCRIPT_FILENAME"])
            with subprocess.Popen(["php-cgi"], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as process:
                stdout, stderr = process.communicate()
                parsed_stdout = parse_php_response(stdout)

                duplex.response = parsed_stdout

                print(duplex.response)

                duplex.response.version = duplex.request.version
                # .... reference par defaut
        else:
            pass