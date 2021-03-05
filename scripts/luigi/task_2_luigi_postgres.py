from task_1 import Task1

import luigi


class Task2(luigi.Task):
    x = luigi.IntParameter()
    y = luigi.IntParameter(default=45)

    def requires(self):
        return Task1(self.x)

    def run(self):
        z = str(self.x + self.y)
        print("******* ", z)
        with self.output().open('w') as output_file:
            output_file.write(z)

    def output(self):
        return luigi.local_target.LocalTarget('/home/silil/Documents/itam/metodos_gran_escala/data-product-architecture/luigi/pass_parameter_task1.txt')
