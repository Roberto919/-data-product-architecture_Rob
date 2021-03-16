## EXAMPLE OF RUNNING STRINGED TASKS WITH LUIGI (TASK 2)
#### The pipeline should complete the following:
###### 1. Create a file with content given in the parameters
###### 2. Save that file in a specified location in s3 <--





"----------------------------------------------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Standard library imports

import pickle


## Third party imports

import luigi

import luigi.contrib.s3

import boto3


## Local application imports

from rob_luigi_test_task1 import RobTask1





"----------------------------------------------------------------------------------------------------------------------"
################
## Parameters ##
################

path = "/Users/rp_mbp/Documents/ReposRob_RobPer/ITAMmcd/semestre_2/Arquitectura_Prod_Dat/Venv_ArqPD/repos/data-product-architecture/scripts/luigi/rob_test_output.pkl"
task_name = "rob_demo"





"----------------------------------------------------------------------------------------------------------------------"
####################
## Luigi pipeline ##
####################


## Creating file with operation
class RobTask2(luigi.Task):

    ## Parameters
    x = luigi.IntParameter()
    y = luigi.IntParameter()
    bucket = luigi.Parameter()
    root_path = luigi.Parameter()


    ## Requires
    def requires(self):
        return RobTask1(self.x, self.y)


    ## Run
    def run(self):

        ## Creating session for AWS
        ses = boto3.session.Session(profile_name='robper_dpa', region_name='us-west-2')
        s3_resource = ses.resource('s3')

        ## Open file that will be stored
        s3_key = str(self.root_path) + "/" + str(task_name) + "/" + "rob_test_output.pkl"
        s3_resource.meta.client.upload_file(Filename=path, Bucket=self.bucket, Key=s3_key)


    ## Output
    def output(self):

        ## Path in s3 where file will be stored
        output_path = "s3://{}/{}/{}/rob_luigi_test.pkl".format(
            self.bucket,
            self.root_path,
            task_name,
        )

        return luigi.contrib.s3.S3Target(path=output_path)