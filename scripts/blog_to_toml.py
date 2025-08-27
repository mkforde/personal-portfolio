"""
Ghost Export → TOML Blog Converter

This script converts Ghost CMS exported content (ghost-export.json)
into a TOML file (blogs.toml) for use in static sites or other tooling.

How it works:
1. Loads the Ghost export JSON (from Ghost Admin → Settings → Export).
2. Filters only posts with status == "published".
3. Extracts fields:
   - title → `title`
   - published_at → `date` (YYYY-MM-DD format)
   - custom_excerpt → `summary` (if present), otherwise first 60 words of plaintext
   - slug + BASE_URL → `link`
   - tags → matched via posts_tags + tags tables
4. Outputs results in the following TOML format:

   [[blogs]]
   title = "Example Post"
   date = "2025-01-01"
   summary = "Short summary or first 50 words..."
   tags = ["tag1", "tag2"]
   link = "https://yourblog.com/example-post"

Usage:
- Update BASE_URL to your blog's domain.
- Run: `python ghost_to_toml.py`
- Result: blogs.toml will contain all published posts.

Notes:
- Only published posts are included (drafts/scheduled are skipped).
- Summaries are forced into one line (no newlines).
- Extendable: you can add more fields (feature_image, uuid, etc.) if needed.
"""

import json
from datetime import datetime

BASE_URL = "https://blog.michaelforde.com"

with open("ghost-export.json") as f:
    data = json.load(f)

db = data["db"][0]["data"]
posts = db["posts"]
tags = {t["id"]: t["name"] for t in db["tags"]}
posts_tags = db["posts_tags"]

# Build a lookup: post_id -> [tag names]
post_tags = {}
for pt in posts_tags:
    post_id = pt["post_id"]
    tag_id = pt["tag_id"]
    if post_id not in post_tags:
        post_tags[post_id] = []
    if tag_id in tags:
        post_tags[post_id].append(tags[tag_id])

# Collect all TOML blocks with their date for sorting
entries = []

for post in posts:
    if post.get("status") != "published":
        continue

    title = post["title"]
    date_obj = datetime.fromisoformat(
        post["published_at"].replace("Z", "+00:00")
    )
    date = date_obj.strftime("%Y-%m-%d")
    slug = post["slug"]
    link = f"{BASE_URL}/{slug}"

    # Summary logic
    if post.get("custom_excerpt"):
        summary = post["custom_excerpt"]
    else:
        words = post.get("plaintext", "").split()
        summary = " ".join(words[:60]) + ("..." if len(words) > 60 else "")

    # Tags
    tags_list = post_tags.get(post["id"], [])

    block = f'''[[blogs]]
title = "{title}"
date = "{date}"
summary = "{summary}"
tags = {tags_list}
link = "{link}"
'''

    entries.append((date_obj, block))

# Sort by date (newest first)
entries.sort(key=lambda x: x[0], reverse=True)

# Write out
with open("blogs.toml", "w") as f:
    f.write("\n".join(block for _, block in entries))
