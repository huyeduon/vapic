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
  user                 = "Administrator@vsphere.local"
  password             = "C1sc0123!"
  vsphere_server       = "10.138.159.106"
  allow_unverified_ssl = true
}


data "vsphere_datacenter" "datacenter" {
  name = "HXDC"
}

data "vsphere_datastore" "datastore" {
  name          = "HX-DATA"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_compute_cluster" "cluster" {
  name          = "HX-Cluster"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_resource_pool" "default" {
  name          = format("%s%s", data.vsphere_compute_cluster.cluster.name, "/Resources")
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_host" "host" {
  name          = "10.138.159.74"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_network" "oob" {
  name          = "HUYEN-VLAB-60"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_network" "infra" {
  name          = "trunking"
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
    remote_ovf_url            = "http://10.138.159.102/downloads/vapic152.ova"
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
