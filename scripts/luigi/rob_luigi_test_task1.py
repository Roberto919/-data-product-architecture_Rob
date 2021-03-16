## EXAMPLE OF RUNNING STRINGED TASKS WITH LUIGI (TASK 1)
#### The pipeline should complete the following:
###### 1. Create a file with content given in the parameters <--
###### 2. Save that file in a specified location in s3





"----------------------------------------------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Standard library imports

import pickle


## Third party imports

import luigi


## Local application imports





"----------------------------------------------------------------------------------------------------------------------"
################
## Parameters ##
################

path = "/Users/rp_mbp/Documents/ReposRob_RobPer/ITAMmcd/semestre_2/Arquitectura_Prod_Dat/Venv_ArqPD/repos/data-product-architecture/scripts/luigi/rob_test_output.pkl"





"----------------------------------------------------------------------------------------------------------------------"
####################
## Luigi pipeline ##
####################


## Creating file with operation
class RobTask1(luigi.Task):

    ## Parameters
    x = luigi.IntParameter()
    y = luigi.IntParameter()

    ## Run
    def run(self):
        res = "El resultado de la operación es: {}".format(self.x + self.y)
        pickle.dump(res, open(path, "wb"))

    ## Output
    def output(self):
        return luigi.local_target.LocalTarget(path)