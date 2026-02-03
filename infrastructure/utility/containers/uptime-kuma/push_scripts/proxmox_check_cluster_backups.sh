PUSH_URL=http://utility-01.home:3001/api/push/4UnaDJC9k9Mb1KkdXSqCE9nCwGS4QBA9
COUNT=$(ssh root@$1 'find /var/lib/vz/cluster_backups -type f -newermt "24 hours ago"' | wc -l); \
[ "$COUNT" -gt 0 ] && \
curl -fsS "${PUSH_URL}?status=up&msg=${COUNT}_files_last_24h" || \
curl -fsS "${PUSH_URL}?status=down&msg=no_files_last_24h"