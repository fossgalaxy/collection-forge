# Justfile for fossgalaxy Ansible collections
# Requires: just, ansible-core, ansible-lint, yamllint

set shell := ["bash", "-cu"]

# Default target
default: lint

# ------------------------------------------------------------
# Setup
# ------------------------------------------------------------

# Install development dependencies (inside a venv ideally)
install:
    python3 -m pip install --upgrade pip
    python3 -m pip install \
        ansible-core \
        ansible-lint \
        yamllint \
        molecule \
        pytest \
        pytest-ansible

# ------------------------------------------------------------
# Linting
# ------------------------------------------------------------

lint: yamllint ansible-lint

yamllint:
    yamllint .

ansible-lint:
    ansible-lint

# ------------------------------------------------------------
# Ansible sanity tests (collection-aware)
# ------------------------------------------------------------

sanity:
    ansible-test sanity --docker

# If running locally without docker:
sanity-local:
    ansible-test sanity

# ------------------------------------------------------------
# Molecule (if roles use it)
# ------------------------------------------------------------

molecule:
    molecule test

molecule-destroy:
    molecule destroy

# ------------------------------------------------------------
# Formatting helpers
# ------------------------------------------------------------

# Auto-fix ansible-lint issues where possible
lint-fix:
    ansible-lint --fix .

#
# Development Install
#
dev-install:
    ansible-galaxy collection install . --force -p ~/.local/ansible-dev

# ------------------------------------------------------------
# Clean
# ------------------------------------------------------------

clean:
    find . -name "__pycache__" -type d -exec rm -rf {} +
    find . -name ".molecule" -type d -exec rm -rf {} +
