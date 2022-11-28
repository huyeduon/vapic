# Cisco virtual apic deployment automation.
## Introduction
The repo contains multiple script file that help you to deploy single virtual apic, multiple virtual apic in single ansible workflow, automate vapic cluster bring up.\n

vapic cluster is built up in Layer 3 mode that allow vapic to run in different subnets. Make sure you already had proper routing in your IPN network.\n

For the lab enviroment, IPN can be virtual router such as Cisco CSR1000V or Catalyst8000. It is recommended to have high throughput license for virtual router such as 1Gbps.

![vapic layer 3 mode](https://ninjagoinsbu.s3.ap-southeast-2.amazonaws.com/images/vapic_l3.png)

## Requirement
The main requirement are python3, pvmomi, ansible, vcenter with ESXi 7.0\n
One vapic requires:
16 vCPU, 96GB RAM, 480GB SSD (it may work if HDD has good IOPS)

vapic out-of-band interface is used for management purpose and we need Vmware acccess port-group.\n
vapic infra interface is used for clustering communication between vapics and we need Vmware trunk port-group.\n

Note that the out of band IP address of each vapic is hard-coded in the yaml script. You need to edit it to match your environment.

## To deploy a single vapic for example vapic1
./deploy1.sh

## To destroy vapic vm for example vapic1
./destroy1.sh

## To deploy multiple vapic in single ansible workflow
First, edit the file vapic.yaml to match your environment then run deploy.sh script\n
./deploy.sh

Once at least 3 vapic were deployed, you can bring up vapic cluster by running the vapic.py script. The bootstrap.py has parameters for the first 3 vapic: vapic1, vapic2, vapic3.\n If you have more vapic, please edit the file to match your environment.\n Once the boostrap.py file is good with your enviroment, you can bootstrap vapic cluster:\n

python3 vapic.py
