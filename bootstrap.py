vapic1SerialNumber = ''
vapic2SerialNumber = ''
vapic3SerialNumber = ''

vapic1Oob = "10.138.159.215"
vapic2Oob = "10.138.159.216"
vapic3Oob = "10.138.159.217"

bootstrapConfig = {
    "cluster": {
        "fabricName": "vapic",
        "fabricId": 1,
        "clusterSize": 3,
        "Layer3": True,
        "gipoPool": "225.0.0.0/15",
        "adminpassword": "C1sc0123!",
        "infraVlan": 4093
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
                "address4": "172.16.0.31/24",
                "gateway4": "172.16.0.30",
                "vlan": 60
            },
            "oobNetwork": {
                "address4": "10.138.159.215/28",
                "gateway4": "10.138.159.209",
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
                "address4": "172.16.0.32/24",
                "gateway4": "172.16.0.30",
                "vlan": 60
            },
            "oobNetwork": {
                "address4": "10.138.159.216/28",
                "gateway4": "10.138.159.209",
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
                "address4": "172.16.0.33/24",
                "gateway4": "172.16.0.30",
                "vlan": 60
            },
            "oobNetwork": {
                "address4": "10.138.159.217/28",
                "gateway4": "10.138.159.209",
                "enableIPv4": True
            }
        }
    ]
}
