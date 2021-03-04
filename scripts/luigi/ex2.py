# PYTHONPATH='.' luigi --module ex2 LocalFileSystem --local-scheduler
import luigi
import luigi.contrib.s3
import boto3
import os


class LocalFileSystemTask(luigi.Task):

    def run(self):

        with self.output().open('w') as output_file:
            output_file.write("test,luigi,s3")


    def output(self):
        return luigi.local_target.LocalTarget('/home/silil/Documents/itam/metodos_gran_escala/data-product-architecture/luigi/test.csv')
