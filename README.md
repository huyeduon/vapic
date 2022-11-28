# Cisco virtual apic deployment automation.
## Introduction
The repo contains multiple script file that help you to deploy single virtual apic, multiple virtual apic in single ansible workflow, automate vapic cluster bring up.\n

vapic cluster is built up in Layer 3 mode that allow vapic to run in different subnets. Make sure you already had proper routing in your IPN network.\n

For the lab enviroment, IPN can be virtual router such as Cisco CSR1000V or Catalyst8000. It is recommended to have high throughput license for virtual router such as 1Gbps.

## Requirement
Here is content of requirement file, the main requirement are python3, pvmomi, and ansible.\n

ansible==6.6.0\
ansible-core==2.13.6\
certifi==2022.9.24\
cffi==1.15.1\
charset-normalizer==2.1.1\
cryptography==38.0.3\
idna==3.4\
Jinja2==3.1.2\
MarkupSafe==2.1.1\
packaging==21.3\
pycparser==2.21\
pyparsing==3.0.9\
pyvmomi==7.0.3\
PyYAML==6.0\
requests==2.28.1\
resolvelib==0.8.1\
six==1.16.0\
urllib3==1.26.12\

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
