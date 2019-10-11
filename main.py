import argparse
import converters

TEMPERATURE_UNITS = ['k', 'c', 'f', 'r']
VOLUME_UNITS = ['li', 'ts', 'ci', 'cu', 'cf', 'ga']
ROUND_DECIMAL = 1



CONVERTORS = {
    'k2c' : converters.k2c,
    'k2f' : converters.k2f,
    'k2r' : converters.k2r,
    'c2k' : converters.c2k,
    'c2f' : converters.c2f,
    'c2r' : converters.c2f,
    'f2k' : converters.f2k,
    'f2c' : converters.f2k,
    'f2r' : converters.f2r,
    'r2k' : converters.r2k,
    'r2c' : converters.r2c,
    'r2f' : converters.r2f,
    'li2ts' : converters.li2ts,
    'li2ci' : converters.li2ci,
    'li2cu' : converters.li2cu,
    'li2cf' : converters.li2cf,
    'li2ga' : converters.li2ga,
    'ts2li' : converters.ts2li,
    'ts2ci' : converters.ts2ci,
    'ts2cu' : converters.ts2cu,
    'ts2cf' : converters.ts2cf,
    'ts2ga' : converters.ts2ga,
    'ci2li' : converters.ci2li,
    'ci2ts' : converters.ci2ts,
    'ci2cu' : converters.ci2cu,
    'ci2cf' : converters.ci2cf,
    'ci2ga' : converters.ci2ga,
    'cu2li' : converters.cu2li,
    'cu2ts' : converters.cu2ts,
    'cu2ci' : converters.cu2ci,
    'cu2cf' : converters.cu2cf,
    'cu2ga' : converters.cu2ga,
    'cf2cu' : converters.cf2cu,
    'cf2ga' : converters.cf2ga,
    'ga2li' : converters.ga2li,
    'ga2ts' : converters.ga2ts,
    'ga2ci' : converters.ga2ci,
    'ga2cu' : converters.ga2cu,
    'ga2cf' : converters.ga2cf,
}

def unit_convertor(input_value, input_uom, target_uom):
    '''
        Converts from one UOM to other
        Returns float. converted value
    '''
    key = "{0}2{1}".format(input_uom, target_uom)
    if key in CONVERTORS:
        return CONVERTORS[key](input_value)
    else:
        raise NotImplementedError("Unit conversion {0} not support".format(key))


if __name__ == '__main__':
    '''
        1. The teacher must be able to provide an input numerical value, an input
        unit of measure, a target unit of measure, and a student’s numeric
        response.
        2. The system indicates that the response is correct, incorrect, or invalid.
        To be considered correct, the student’s response must match an authoritative
        answer after both the student’s response and authoritative answer are
        ounded to the tenths place.
        3. Optional Challenge: Implement a basic continuous integration/continuous
        deployment (CI/CD) pipeline for your code using your solution of
        choice (cloud solutions are acceptable). What you provide should
        support a peer code review process and seamless app deployment
        when a commit is merged to trunk.
    '''

    parser = argparse.ArgumentParser(description='Unit Conversion.')
    parser.add_argument('-i', '--input_value', type=float, help='Input numerical value')
    parser.add_argument('-u', '--input_uom', type=str, help='Input unit of measure', choices=TEMPERATURE_UNITS + VOLUME_UNITS)
    parser.add_argument('-t', '--target_uom', type=str, help='Target unit of measure,', choices=TEMPERATURE_UNITS + VOLUME_UNITS)
    parser.add_argument('-s', '--student_value', type=float, help='Student’s numeric response')

    args = parser.parse_args()

    # Validate units are of same type
    if not (set([args.input_uom, args.target_uom]).issubset(set(TEMPERATURE_UNITS)) or set([args.input_uom, args.target_uom]).issubset(set(VOLUME_UNITS))):
        msg = 'input_uom {0} and target_uom {1} should be of same type'.format(args.input_uom, args.target_uom)
        raise ValueError(msg)

    if round(unit_convertor(args.input_value, args.input_uom, args.target_uom), 1) == round(args.student_value, 1):
        print('correct')
    else:
        print('incorrect')
