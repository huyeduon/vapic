from bootstrap import bootstrapConfig, vapic1SerialNumber, vapic2SerialNumber, vapic3SerialNumber, vapic1Oob, vapic2Oob, vapic3Oob
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# verify vAPIC and return serial number
def verify(vapic_ipaddress):
    url = "https://" + str(vapic_ipaddress) + "/api/bootx/v1/node/verify"
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'AuthCookie=dummytoken'
    }

    payload = json.dumps({
        "username": "admin",
        "password": "C1sc0123!",
        "controllerType": "virtual",
        "address": str(vapic_ipaddress)
    })

    response = requests.request(
        "POST", url, headers=headers, data=payload, verify=False)

    response_json = json.loads(response.text)

    return response_json['serialNumber']

# return cluster boostrap config in json format
def bootstrapConfigJson():
    vapic1SerialNumber = verify(vapic1Oob)
    vapic2SerialNumber = verify(vapic2Oob)
    vapic3SerialNumber = verify(vapic3Oob)
    bootstrapConfig["nodes"][0]["serialNumber"] = vapic1SerialNumber
    bootstrapConfig["nodes"][1]["serialNumber"] = vapic2SerialNumber
    bootstrapConfig["nodes"][2]["serialNumber"] = vapic3SerialNumber

    json_bootstrapConfig = json.dumps(bootstrapConfig)

    return json_bootstrapConfig


def createCluster(payload):
    url = "https://" + vapic1Oob + "/api/bootx/v1/cluster/bootstrap"
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'AuthCookie=dummytoken'
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload, verify=False)


def main():
    json_bootstrapConfig = bootstrapConfigJson()
    createCluster(json_bootstrapConfig)

if __name__ == '__main__':
    main()