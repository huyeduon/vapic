terraform {
  required_providers {
    vsphere = {
      source = "hashicorp/vsphere"
      version = "2.2.0"
    }
  }
}

provider "vsphere" {
  # Configuration options
  user                 = "Administrator@dmz.cisco.demo"
  password             = "C1scoUC$"
  vsphere_server       = "192.168.20.4"
  allow_unverified_ssl = true
}


data "vsphere_datacenter" "datacenter" {
  name = "SGP"
}

data "vsphere_datastore" "datastore" {
  name          = "Day2Ops2"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_compute_cluster" "cluster" {
  name          = "HX-2"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_resource_pool" "default" {
  name          = format("%s%s", data.vsphere_compute_cluster.cluster.name, "/Resources")
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_host" "host" {
  name          = "hx-2-compute5.cisco.demo"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_network" "oob" {
  name          = "common|default|vmConsole"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_network" "infra" {
  name          = "vapic"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

## Deployment of VM from Local OVF
resource "vsphere_virtual_machine" "vmFromLocalOvf" {
  name                 = "vapic1-tf"
  datacenter_id        = data.vsphere_datacenter.datacenter.id
  datastore_id         = data.vsphere_datastore.datastore.id
  host_system_id       = data.vsphere_host.host.id
  resource_pool_id     = data.vsphere_resource_pool.default.id

  wait_for_guest_net_timeout = 0
  wait_for_guest_ip_timeout  = 0

  ovf_deploy {
    allow_unverified_ssl_cert = true
    remote_ovf_url            = "http://192.168.20.248/downloads/aci-apic-dk9.6.0.1.141d.ova"
    disk_provisioning         = "thin"
    ip_protocol               = "IPV4"
    ip_allocation_policy      = "STATIC_MANUAL"
    ovf_network_map = {
      "OOB Network" = data.vsphere_network.oob.id
      "Infra Network" = data.vsphere_network.infra.id
    }
  }
  vapp {
    properties = {
      "oobip"    = "172.16.11.101/24",
      "oobgw"      = "172.16.11.1",
      "adminpassword"     = "C1sc0123!",  
    }
  }
}