# vapic deployment

Requirement:
ansible==6.6.0
ansible-core==2.13.6
certifi==2022.9.24
cffi==1.15.1
charset-normalizer==2.1.1
cryptography==38.0.3
idna==3.4
Jinja2==3.1.2
MarkupSafe==2.1.1
packaging==21.3
pycparser==2.21
pyparsing==3.0.9
pyvmomi==7.0.3
PyYAML==6.0
requests==2.28.1
resolvelib==0.8.1
six==1.16.0
urllib3==1.26.12

The out of band IP address of each vapic is hard-coded in the yaml script. 

To deploy a single vapic for example vapic1:
./deploy1.sh

To destroy vapic vm for exaple vapic1:
./destroy1.sh

To deploy multiple vapic in single ansible workflow, first edit the vapic.yaml file then run:
./deploy.sh

Once at least 3 vapic were deployed, you can bring up vapic cluster by running boostrap script, bootstrap.py has parameters for the first 3 vapic: vapic1, vapic2, vapic3. If you have more vapic, please edit the file to match your environment. Once the boostrap.py file is good with your enviroment, you can bootstrap vapic cluster:

python3 vapic.py
