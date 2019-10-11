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
incorrect
incorrect
usage: main.py [-h] [-i INPUT_VALUE] [-u {k,c,f,r,li,ts,ci,cu,cf,ga}]
               [-t {k,c,f,r,li,ts,ci,cu,cf,ga}] [-s STUDENT_VALUE]
main.py: error: argument -s/--student_value: invalid float value: 'dog'
```

## Run unit tests
```bash
$ python -m unittest discover -s ./ -p "*_test.py"
............
----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
```