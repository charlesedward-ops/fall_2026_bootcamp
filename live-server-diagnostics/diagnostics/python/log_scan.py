

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp (orchestration-tool)
$ cd live-server-diagnostics/

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp/live-server-diagnostics (orchestration-tool)
$ ls -l
total 0
drwxr-xr-x 1 cdela 197609 0 Sep 25 19:43 diagnostics/
drwxr-xr-x 1 cdela 197609 0 Sep 25 19:43 logs/
drwxr-xr-x 1 cdela 197609 0 Sep 25 19:43 reports/

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp/live-server-diagnostics (orchestration-tool)
$ ^[[200~cat << 'EOF' > logs/server.log
> 2026-09-25T09:00:01 INFO server started
> 2026-09-25T09:01:14 INFO health check passed
> 2026-09-25T09:02:18 WARN disk usage above 70 percent
> 2026-09-25T09:03:42 ERROR database connection timeout
> 2026-09-25T09:04:15 INFO retrying database connection
> 2026-09-25T09:05:22 ERROR failed login attempt detected
> 2026-09-25T09:06:30 CRITICAL payment service unavailable
> 2026-09-25T09:07:40 INFO server diagnostic complete
> EOF
bash: $'\E[200~cat': command not found

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp/live-server-diagnostics (orchestration-tool)
$ cat << 'EOF' > logs/server.log
2026-09-25T09:00:01 INFO server started
2026-09-25T09:01:14 INFO health check passed
2026-09-25T09:02:18 WARN disk usage above 70 percent
2026-09-25T09:03:42 ERROR database connection timeout
2026-09-25T09:04:15 INFO retrying database connection
2026-09-25T09:05:22 ERROR failed login attempt detected
2026-09-25T09:06:30 CRITICAL payment service unavailable
2026-09-25T09:07:40 INFO server diagnostic complete
EOF

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp/live-server-diagnostics (orchestration-tool)
$ ls -l
total 0
drwxr-xr-x 1 cdela 197609 0 Sep 25 19:43 diagnostics/
drwxr-xr-x 1 cdela 197609 0 Sep 25 19:51 logs/
drwxr-xr-x 1 cdela 197609 0 Sep 25 19:43 reports/

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp/live-server-diagnostics (orchestration-tool)
$ ^C

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp/live-server-diagnostics (orchestration-tool)
$ touch logs/server.log

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp/live-server-diagnostics (orchestration-tool)
$ vi logs/server.log

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp/live-server-diagnostics (orchestration-tool)
$ cat << 'EOF' > logs/server.log
2026-09-25T09:00:01 INFO server started
2026-09-25T09:01:14 INFO health check passed
2026-09-25T09:02:18 WARN disk usage above 70 percent
2026-09-25T09:03:42 ERROR database connection timeout
2026-09-25T09:04:15 INFO retrying database connection
2026-09-25T09:05:22 ERROR failed login attempt detected
2026-09-25T09:06:30 CRITICAL payment service unavailable
2026-09-25T09:07:40 INFO server diagnostic complete
EOF

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp/live-server-diagnostics (orchestration-tool)
$ cat << 'EOF' > logs/server.log
2026-09-25T09:00:01 INFO server started
2026-09-25T09:01:14 INFO health check passed
2026-09-25T09:02:18 WARN disk usage above 70 percent
2026-09-25T09:03:42 ERROR database connection timeout
2026-09-25T09:04:15 INFO retrying database connection
2026-09-25T09:05:22 ERROR failed login attempt detected
2026-09-25T09:06:30 CRITICAL payment service unavailable
2026-09-25T09:07:40 INFO server diagnostic complete
E
>
> pwd
>
> ^C

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp/live-server-diagnostics (orchestration-tool)
$ ^C

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp/live-server-diagnostics (orchestration-tool)
$ 2026-09-25T09:00:01 INFO server started
2026-09-25T09:01:14 INFO health check passed
2026-09-25T09:02:18 WARN disk usage above 70 percent
2026-09-25T09:03:42 ERROR database connection timeout
2026-09-25T09:04:15 INFO retrying database connection
2026-09-25T09:05:22 ERROR failed login attempt detected
2026-09-25T09:06:30 CRITICAL payment service unavailable
2026-09-25T09:07:40 INFO server diagnostic complete
bash: 2026-09-25T09:00:01: command not found
bash: 2026-09-25T09:01:14: command not found
bash: 2026-09-25T09:02:18: command not found
bash: 2026-09-25T09:03:42: command not found
bash: 2026-09-25T09:04:15: command not found
bash: 2026-09-25T09:05:22: command not found
bash: 2026-09-25T09:06:30: command not found
bash: 2026-09-25T09:07:40: command not found

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp/live-server-diagnostics (orchestration-tool)
$ touch logs/server.log

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp/live-server-diagnostics (orchestration-tool)
$ vi logs/server.log

cdela@Abundance1536 MINGW64 ~/Documents/TheoWAF/cpg/cloudfundamentals/fall_2026_bootcamp/live-server-diagnostics (orchestration-tool)
$


