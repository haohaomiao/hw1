# TODO: add autopep8 here.
autopep8 --in-place -r -a  ./

# TODO: add autoflake here.
autoflake --in-place -r --remove-unused-variables ./

# TODO: add isort here.
isort ./

# TODO: add flake8 here.
flake8 .