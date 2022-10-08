# TODO: add autopep8 here.
autopep8 --exclude=simpbbs_env --in-place -r -a  ./

# TODO: add autoflake here.
autoflake --exclude=simpbbs_env --in-place -r --remove-unused-variables ./

# TODO: add isort here.
isort --sg=simpbbs_env ./

# TODO: add flake8 here.
flake8 .