PUSH_URL=http://utility-01.home:3001/api/push/enD4BR8MnUBjfoZA8uAfdtP5TjBUMe9y
COUNT=$(find backups -type f -newermt "24 hours ago" | wc -l); \
[ "$COUNT" -gt 0 ] && \
curl -fsS "${PUSH_URL}?status=up&msg=${COUNT}_files_last_24h" || \
curl -fsS "${PUSH_URL}?status=down&msg=no_files_last_24h"
