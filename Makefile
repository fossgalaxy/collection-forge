
.PHONY: install

install:
	ansible-galaxy collection install . --force
