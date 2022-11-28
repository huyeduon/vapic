# vapic deployment

Requirement:


The out of band IP address of each vapic is hard-coded in the yaml script. 

To deploy a single vapic for example vapic1:
./deploy1.sh

To destroy vapic vm for exaple vapic1:
./destroy1.sh

To deploy multiple vapic in single ansible workflow, first edit the vapic.yaml file then run:
./deploy.sh

Once at least 3 vapic were deployed, you can bring up vapic cluster by running boostrap script, bootstrap.py has parameters for the first 3 vapic: vapic1, vapic2, vapic3. If you have more vapic, please edit the file to match your environment. Once the boostrap.py file is good with your enviroment, you can bootstrap vapic cluster:

python3 vapic.py
