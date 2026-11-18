#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
ht = (ROOT / "wordpress/.htaccess").read_text(encoding="utf-8")
robots = (ROOT / "wordpress/robots.txt").read_text(encoding="utf-8")
compose = (ROOT / "docker-compose.yml").read_text(encoding="utf-8")
checks = {
    "Apache 2.4 blocks wp-config.php": bool(re.search(r'<FilesMatch[^>]*>\\s*Require all denied\\s*</FilesMatch>', ht, re.S) and "wp-config" in ht),
    "WordPress front controller rewrite exists": "RewriteRule . /index.php [L]" in ht,
    "real files and directories are excluded from rewrite": "!-f" in ht and "!-d" in ht,
    "robots blocks wp-admin": "Disallow: /wp-admin/" in robots,
    "robots allows admin-ajax": "Allow: /wp-admin/admin-ajax.php" in robots,
    "debug enabled, log enabled and display disabled": "WORDPRESS_DEBUG" in compose and "WP_DEBUG_LOG', true" in compose and "WP_DEBUG_DISPLAY', false" in compose,
    "file editor disabled": "DISALLOW_FILE_EDIT', true" in compose,
    "DB password is environment-driven": "WORDPRESS_DB_PASSWORD" in compose and ".env" in (ROOT/".gitignore").read_text(),
    "optional HTTPS redirect documented separately": (ROOT/"deploy/https-redirect.conf.example").exists(),
}
failed = [name for name, ok in checks.items() if not ok]
for name, ok in checks.items():
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
print(f"\\nResult: {len(checks)-len(failed)}/{len(checks)} checks passed")
sys.exit(1 if failed else 0)
