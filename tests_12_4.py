import unittest
from unittest import TestCase
import logging
from run import Runner


class RunnerTest:
    def test_walk(self):
        try:
            num_run = Runner('obj1', speed=-3)
            for _ in range(10):
                num_run.walk()
                #self.assertEquals(num_run.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning(f'Неверная скорость для Runner')
    def test_run(self):
        try:
            new_run = Runner(5)
            for _ in range(10):
                new_run.run()
            #self.assertEquals(new_run.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_challenge(self):
        ch1 = Runner('challenge1')
        ch2 = Runner('challenge2')
        for _ in range(10):
            ch1.run()
            ch2.walk()
            #self.assertEquals(ch1.distance, ch2.distance)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log',
                        format='%(asctime)s |%(levelname)s | %(message)s', encoding='utf-8')
    my_run_test = RunnerTest()
    my_run_test.test_walk()
    my_run_test.test_run()
    my_run_test.test_challenge()
    #unittest.main()