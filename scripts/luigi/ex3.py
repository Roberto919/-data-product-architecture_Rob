# existe un bug con bot3 y luigi para pasar las credenciales
# necesitas enviar el parámetro AWS_PROFILE e indicar el profile
# con el que quieres que se corra
# PYTHONPATH='.' AWS_PROFILE=mge luigi --module ex3_luigi S3Task --local-scheduler ...
import luigi
import luigi.contrib.s3
import boto3
import os
import yaml

from luigi.contrib.s3 import S3Client


class S3Task(luigi.Task):
    task_name = "demo"

    bucket = luigi.Parameter()
    root_path = luigi.Parameter()
    etl_path = luigi.Parameter()
    year = luigi.Parameter()
    month = luigi.Parameter()
 
    def run(self):
        #ses = boto3.session.Session(profile_name='mge', region_name='us-west-2')
        #s3_resource = ses.resource('s3')
        #print(ses)

        with self.output().open('w') as output_file:
            output_file.write("test,luigi,s3")


    def output(self):
        with open ("credentials.yaml", 'r') as f:
            config = yaml.safe_load(f)

        s3_creds = config['s3']

        client_s3 = S3Client(aws_access_key_id=s3_creds['aws_access_key_id'],
                             aws_secret_access_key=s3_creds['aws_secret_access_key'])

        output_path = "s3://{}/{}/{}/{}/YEAR={}/MONTH={}/test.csv".\
        format(self.bucket,
        self.root_path,
        self.etl_path,
        self.task_name,
        self.year,
        str(self.month))

        return luigi.contrib.s3.S3Target(path=output_path, client=client_s3)
