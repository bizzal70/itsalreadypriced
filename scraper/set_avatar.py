"""
One-shot: set the @ItsAlreadyPrice avatar via the X API v1.1 (account/update_profile_image),
using the OAuth1 credentials already stored as repo secrets. This bypasses the website's
Premium photo-review flow and may apply the avatar directly.

Env: X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
"""

import os
import sys
from pathlib import Path
import tweepy

IMG = Path(__file__).resolve().parent.parent / "assets" / "brand" / "iap-x-avatar.png"


def main():
    if not IMG.exists():
        sys.exit(f"Avatar file not found: {IMG}")
    print(f"Avatar file: {IMG} ({IMG.stat().st_size} bytes)")

    auth = tweepy.OAuth1UserHandler(
        os.environ["X_API_KEY"],
        os.environ["X_API_SECRET"],
        os.environ["X_ACCESS_TOKEN"],
        os.environ["X_ACCESS_TOKEN_SECRET"],
    )
    api = tweepy.API(auth)

    try:
        me = api.verify_credentials()
        print(f"v1.1 auth OK as @{me.screen_name}")
    except Exception as e:
        print(f"verify_credentials (v1.1) failed: {type(e).__name__}: {e}")
        print("(continuing to update_profile_image anyway to surface its exact error)")

    try:
        resp = api.update_profile_image(filename=str(IMG))
        url = getattr(resp, "profile_image_url_https", None) or getattr(resp, "profile_image_url", "?")
        print("SUCCESS: update_profile_image accepted.")
        print(f"profile_image_url: {url}")
    except Exception as e:
        print(f"FAILED: update_profile_image error: {type(e).__name__}: {e}")
        raise


if __name__ == "__main__":
    main()
