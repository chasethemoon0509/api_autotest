import pytest


if __name__ == '__main__':
    which = pytest.mark.usefixtures('get_runwhich')
    if which == 'systema':
        pytest.main(['/testcase/systemea'])
    elif which == 'systemb':
        pytest.main(['/testcase/systemeb'])
    elif which == 'all':
        pytest.main()





