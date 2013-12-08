
build: lib setup.py
	./setup.py build

install:
	./setup.py install

test:
	nosetests -v

develop: install
	./setup.py develop

clean:
	-rm -rf build
	-sudo rm -rf *.egg-info
	-sudo rm -rf dist 

