install-venv:
	python3.11 -m venv .

install-requirements:
	venv/bin/pip3 install -r requirements.txt
