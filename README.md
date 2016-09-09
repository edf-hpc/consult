Consult
=======

Gives a quick overview of your Consul cluster.

Example of output:

```
admin (10.11.0.1)   passing
cn1 (10.11.0.11)    passing
  - http:           passing   [output snipped (11145)]
  - tftp:           passing   «PROCS OK: 1 process with command name 'in.tftpd' | procs=1;1:;;0;»
cn2 (10.11.0.12)    passing → leader ←
  - http:           passing   ∅
  - tftp:           passing   ∅
cn3 (10.11.0.13)    passing
  - http:           passing   [output snipped (10742)]
  - tftp:           passing   «PROCS OK: 1 process with command name 'in.tftpd' | procs=1;1:;;0;»
```

With ANSI colors that shine in your eyes!
