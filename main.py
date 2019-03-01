#!/usr/bin/env python3

"""
VMO3 - Main
Author: Clint Mann

Description:


"""
import requests
import json
import os
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, jsonify
from datetime import datetime
from get_token import auth_token
from check_MSgraph import check_activedir_user, check_auto_reply
from mediator_sync import sync_mediator
from mediator_post import post_mediator

tenant = os.environ['TENANT']
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
mediator_ip = os.environ['MEDIATOR_IP']
mediator_port = os.environ['MEDIATOR_PORT']
listener_ip = os.environ['LISTENER_IP']
listener_port = os.environ['LISTENER_PORT']

resource = "https://graph.microsoft.com"
grant_type = "client_credentials"

auth_base_url = "https://login.microsoftonline.com/"
oauth_url_v1 = auth_base_url + tenant + str("/oauth2/token")
graph_users_url = "https://graph.microsoft.com/v1.0/users/"
mediator_url = "http://" + mediator_ip + ":" + mediator_port + "/api/setstatus"
mediator_sync_url = "http://" + mediator_ip + ":" + mediator_port + "/api/setup"
listener_url = "http://" + listener_ip + "/users"
listener_mon_url = "http://" + listener_ip + "/monitor"


app = Flask(__name__)

VMOusers = [{
    "email": "",
    "oooStatus": ""
    }]


@app.route("/")
def main():
    print(str(datetime.now())+": Processing /monitor functionality")
    return jsonify({"result":"True"}), 200


@app.route("/monitor", methods=['POST'])
def monitor_users():
    print(str(datetime.now())+": Processing /monitor functionality")

    if not request.is_json:
        return jsonify({"result": "Not JSON"}), 400

    else:
        req_data = request.get_json(force=True, silent=True)

        data = int(len(req_data))
        print(data)
        return data


def process_users(token, med_url, graph_url):
    # 1 - Check API for POST from MEDIATOR
    mon_user_resp = monitor_users()  # GET user to monitor
    print('GS - GET RESPONSE from Listener', mon_user_resp)  # should be
    # <Response [200]>

    monitor_user = mon_user_resp.json()
    print('GS - GET RESPONSE JSON', monitor_user)

    try:
        # 2 - check if there was anything POSTED from MEDIATOR
        if monitor_user > 0:  # MEDIATOR posted users to be monitored
            email_address = monitor_user['email']
            monitor_status = monitor_user['status']

            # 3 - there is a user - query MS Active Directory
            print('CHECK ACTIVE DIRECTORY FOR EMAIL: ', email_address)
            activedir_check = check_activedir_user(token, graph_url)
            all_users = activedir_check['value']

            # 4 - check MS Graph response - does the user exist
            all_users_str = str(all_users)
            if email_address in all_users_str:  # user has email account
                print("USER {0} FOUND in MS AD".format(email_address))

                # 5 - should this user be monitored
                if monitor_status == "True":  # user supposed to be monitored
                    print(email_address, monitor_status)

                    # 6 - Query MS GRAPH for user OoO status
                    ooo_status, message = check_auto_reply(
                        token, email_address, graph_url)

                    # 7 - if OoO is enabled - POST to MEDIATOR
                    if ooo_status != "disabled":  # autoReply (OoO) is enabled
                        ooo_status = "True"  # normalize status

                        # 8 - add this user to local storage
                        # add ooo_status to vmo_enabled_usrs

                        profile = {
                            "email": email_address,
                            "ooo": ooo_status,
                            "message": message
                        }

                        profile_json = json.dumps(profile)

                        if email_address not in VMOusers:  # usr not in list
                            VMOusers.append(profile)  # add user

                            print('POST OoO Status to Mediator Server...')
                            post_mediator(med_url, profile_json)
                            print('POST complete...')

                    else:  # OoO autoReply is disabled
                        print("User {0} : does not have active Out of Office "
                              "alert".format(email_address))

                else:
                    # monitor is FALSE delete user from VMOusers
                    print("This User {0} is not in the monitor state"
                          .format(email_address))

                    if email_address in VMOusers:  # usr not in list
                        del VMOusers[email_address]

            return '''<h1>You would like to monitor user {} {}</h1>'''.format(
                email_address, monitor_status)

        else:  # NO USERS from MEDIATOR GET REQUEST - CHECK local list
            print('NO users to monitor from MEDIATOR')

            # 1 - check if there are users in vmo_enabled_users list
            if len(VMOusers) != 0:  # there are users in list
                print('USER FOUND IN local list')

                # 2 - parse through list checking ooo status
                for u in VMOusers:
                    # print(u)
                    last_ooo_status = u['ooo']
                    email_address = u['email']
                    # monitor_status = u['monitor']

                    # 3 - if monitor in list is true check OoO status
                    if u['monitor'] == 'True':
                        print('check MS Graph for OOO status')
                        ooo_status, message = check_auto_reply(
                            token, email_address, graph_url)
                        print('ooo status', ooo_status)

                        # 4 - compare last ooo status to current ooo status
                        if last_ooo_status == ooo_status:
                            print('last ooo', last_ooo_status)
                            print('ooo status', ooo_status)
                            print('no change in OOO status')
                        else:

                            # 5 - change detected generate payload for MEDIATOR
                            print('last ooo', last_ooo_status)
                            print('ooo status', ooo_status)
                            print('OOO status has changed...')

                            # update email_address in vmo users with new ooo
                            u['ooo'] = ooo_status
                            u['message'] = ""

                            # normalize OoO status for MEDIATOR
                            if ooo_status != "disabled":  # OoO is enabled
                                ooo_profile_status = "True"  # normalize status
                            else:
                                ooo_profile_status = "False"  # normalize
                                # status

                                profile_payload = {
                                    "email": email_address,
                                    "status": ooo_profile_status,
                                    "message": message
                                }

                                profile_json = json.dumps(profile_payload)

                                print('profile json', profile_json)
                                # 6 - POST ooo status change to MEDIATOR
                                print('POST OoO Status to Mediator Server...')
                                post_mediator(med_url, profile_json)
                                print('POST complete from vmo enabled list...')
                                print('VMO USERS', VMOusers)
    except(KeyError, TypeError, ValueError):
        return jsonify({"result": "Invalid JSON"}), 400


sync_resp = sync_mediator(mediator_sync_url)
resp = sync_resp['result']

if resp == 'True':
    print('Mediator Server sync SUCCESSFUL.')
    #  --- SCHEDULER - ---
    scheduler = BackgroundScheduler(daemon=True)

    # Schedule Authentication Token Refresh - expires every 3600 seconds
    scheduler.add_job(auth_token, 'interval', seconds=3500,
                      args=[client_id, client_secret, resource,
                            grant_type, oauth_url_v1])

    tkn = auth_token(client_id, client_secret, resource,
                     grant_type, oauth_url_v1)

    # Schedule User Status Check
    scheduler.add_job(process_users, 'interval', seconds=1,
                      args=[tkn, mediator_url, graph_users_url])

    process_users(tkn, mediator_url, graph_users_url)

    # Start Scheduler
    scheduler.start()

else:
    print('Was unable to sync with Mediator Server')

if __name__ == '__main__':

    # Start Flask
    app.run(debug=False, host='127.0.0.1', port=5000)

