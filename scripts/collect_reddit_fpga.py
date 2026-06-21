import csv
import time
import requests
from datetime import datetime, timezone


SUBREDDIT = "FPGA"
LIMIT = 40
OUTPUT_FILE = "dataset/fpga_sample_40.csv"


def clean_text(text):
    if text is None:
        return ""
    return " ".join(text.replace("\n", " ").replace("\r", " ").split())


def collect_posts():
    url = f"https://www.reddit.com/r/{SUBREDDIT}/hot.json?limit={LIMIT}"

    headers = {
        "User-Agent": "AI201TakeMeterFPGACollector/1.0"
    }

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    data = response.json()
    posts = []

    for item in data["data"]["children"]:
        post = item["data"]

        title = clean_text(post.get("title", ""))
        body = clean_text(post.get("selftext", ""))

        combined_text = title
        if body:
            combined_text = f"{title} {body}"

        created_utc = datetime.fromtimestamp(
            post.get("created_utc", 0),
            tz=timezone.utc
        ).strftime("%Y-%m-%d %H:%M:%S")

        posts.append({
            "post_id": post.get("id", ""),
            "title": title,
            "body": body,
            "text": combined_text,
            "subreddit": SUBREDDIT,
            "score": post.get("score", 0),
            "num_comments": post.get("num_comments", 0),
            "created_utc": created_utc,
            "url": "https://www.reddit.com" + post.get("permalink", ""),
            "observed_discussion_type": "",
            "main_topic": "",
            "borderline": "",
            "notes": ""
        })

    return posts


def save_csv(posts):
    fieldnames = [
        "post_id",
        "title",
        "body",
        "text",
        "subreddit",
        "score",
        "num_comments",
        "created_utc",
        "url",
        "observed_discussion_type",
        "main_topic",
        "borderline",
        "notes"
    ]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(posts)


if __name__ == "__main__":
    print(f"Collecting {LIMIT} posts from r/{SUBREDDIT}...")
    posts = collect_posts()
    save_csv(posts)
    print(f"Saved {len(posts)} posts to {OUTPUT_FILE}")
    time.sleep(1)