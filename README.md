# FOSS Galaxy Forge collection

FOSS Galaxy has been running a software forge instance for a long time (Gitlab). We're looking at replacing
this 'single source of truth' with a truely Free and Open Source option rather than Open Core. This playbook
is designed to integrate with our other playbooks to deploy such a solution.

## Requirements

1. Code Hosting
2. Code Review
3. CI/CD deployments
4. Documentation/Pages hosting
5. Issue tracking
6. Translations

### Collection Design

This playbook is designed to be composible: it's meant to be used and extended rather than be a 'one-size
fits all' approaches. The 'layer 1' playbook is the [infrastructure roles](https://github.com/fossgalaxy/collection-infra), which this playbook relies on.
You can see this also applied to our [self hosting roles](https://github.com/fossgalaxy/collection-selfhosted).
