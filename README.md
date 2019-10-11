# Requirements
## Ensure python 3 (any version) is in the path
```bash
$ which python
/Users/fd98279/.virtualenvs/python3.6/bin/python

$ python --version
Python 3.6.5
```

# Test
## Get help
```bash
$ python main.py -h
usage: main.py [-h] [-i INPUT_VALUE] [-u {k,c,f,r,li,ts,ci,cu,cf,ga}]
               [-t {k,c,f,r,li,ts,ci,cu,cf,ga}] [-s STUDENT_VALUE]

Unit Conversion.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_VALUE, --input_value INPUT_VALUE
                        Input numerical value
  -u {k,c,f,r,li,ts,ci,cu,cf,ga}, --input_uom {k,c,f,r,li,ts,ci,cu,cf,ga}
                        Input unit of measure
  -t {k,c,f,r,li,ts,ci,cu,cf,ga}, --target_uom {k,c,f,r,li,ts,ci,cu,cf,ga}
                        Target unit of measure,
  -s STUDENT_VALUE, --student_value STUDENT_VALUE
```

## Test provided example scenarios
```bash
$ ./test.sh
correct
incorrect
correct
Traceback (most recent call last):
  File "main.py", line 91, in <module>
    raise ValueError(msg)
ValueError: input_uom ga and target_uom k should be of same type
usage: main.py [-h] [-i INPUT_VALUE] [-u {k,c,f,r,li,ts,ci,cu,cf,ga}]
               [-t {k,c,f,r,li,ts,ci,cu,cf,ga}] [-s STUDENT_VALUE]
main.py: error: argument -s/--student_value: invalid float value: 'dog'
usage: main.py [-h] [-i INPUT_VALUE] [-u {k,c,f,r,li,ts,ci,cu,cf,ga}]
               [-t {k,c,f,r,li,ts,ci,cu,cf,ga}] [-s STUDENT_VALUE]
main.py: error: unrecognized arguments: dog
```

## Run unit tests
```bash
$ python -m unittest discover -s ./ -p "*_test.py"
............
----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
```

# CI/CD

## Travis integration

The repo is intergrated with travis, at the commits page: https://github.com/fd98279/test_f/commits/master travis should display build status
