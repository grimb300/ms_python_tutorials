How I finally got this working (requirements.txt contains the list of modules to install via pip):
  % sudo apt install python3-pip python3-setuptools python3.7-venv
  % python3 -m venv venv
  % source venv/bin/activate
  % pip install -r ./requirements.txt
