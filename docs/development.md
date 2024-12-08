# Developing

This playbook is being created for exploring if Forgejo is a suitable gitlab-ce replacement. It's a bit
'rough and ready' as we're figuring out how we want to put the tools we want to use together.

The current way we're using this playbook is to run:

```
ansible-galaxy collection install fossgalaxy/forge
```

Assuming that the path to the collection is `fossgalaxy/forge`. Please note that this playbook currently
isn't suitable for production use - we've deployed test infrastructure using it already though (based 
on earlier work).


