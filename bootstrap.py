vapic1SerialNumber = ''
vapic2SerialNumber = ''
vapic3SerialNumber = ''

vapic1Oob = "10.138.159.215"
vapic2Oob = "10.138.159.216"
vapic3Oob = "10.138.159.217"

vapic1OobIp = "10.138.159.215/28"
vapic2OobIp = "10.138.159.216/28"
vapic3OobIp = "10.138.159.217/28"

vapic1OobGw = "10.138.159.209"
vapic2OobGw = "10.138.159.209"
vapic3OobGw = "10.138.159.209"

vapic1InfraIp = "172.16.0.31/24"
vapic1InfraGw = "172.16.0.30"

vapic2InfraIp = "172.16.0.32/24"
vapic2InfraGw = "172.16.0.30"

vapic3InfraIp = "172.16.0.33/24"
vapic3InfraGw = "172.16.0.30"

vapic1Vlan = "60"
vapic2Vlan = "60"
vapic3Vlan = "60"

infraVlan = "4093"

adminpassword = "C1sc0123!"

bootstrapConfig = {
    "cluster": {
        "fabricName": "vapic",
        "fabricId": 1,
        "clusterSize": 3,
        "Layer3": True,
        "gipoPool": "225.0.0.0/15",
        "adminpassword": adminpassword,
        "infraVlan": int(infraVlan)
    },
    "nodes": [
        {
            "nodeName": "vapic1",
            "firstNode": True,
            "platform": "virtual",
            "controllerType": "virtual",
            "serialNumber": vapic1SerialNumber,
            "nodeId": 1,
            "infraNetwork": {
                "enableIPv4": True,
                "address4": vapic1InfraIp,
                "gateway4": vapic1InfraGw,
                "vlan": int(vapic1Vlan)
            },
            "oobNetwork": {
                "address4": vapic1OobIp,
                "gateway4": vapic1OobGw,
                "enableIPv4": True
            }
        },
        {
            "nodeName": "vapic2",
            "firstNode": False,
            "platform": "virtual",
            "controllerType": "virtual",
            "serialNumber": vapic2SerialNumber,
            "nodeId": 2,
            "infraNetwork": {
                "enableIPv4": True,
                "address4": vapic2InfraIp,
                "gateway4": vapic2InfraGw,
                "vlan": int(vapic2Vlan)
            },
            "oobNetwork": {
                "address4": vapic2OobIp,
                "gateway4": vapic2OobGw,
                "enableIPv4": True
            }
        },
        {
            "nodeName": "vapic3",
            "firstNode": False,
            "platform": "virtual",
            "controllerType": "virtual",
            "serialNumber": vapic3SerialNumber,
            "nodeId": 3,
            "infraNetwork": {
                "enableIPv4": True,
                "address4": vapic3InfraIp,
                "gateway4": vapic3InfraGw,
                "vlan": int(vapic3Vlan)
            },
            "oobNetwork": {
                "address4": vapic3OobIp,
                "gateway4": vapic3OobGw,
                "enableIPv4": True
            }
        }
    ]
}