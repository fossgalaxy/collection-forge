

test:
    molecule test --all

lint:
    ansible-lint

install:
	ansible-galaxy collection install . --force
