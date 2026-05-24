import argparse
import sys

BADGES = {
    "starstruck": {
        "name": "Starstruck",
        "description": "Created a repository that has 16 stars.",
        "tiers": {
            "Default": "16 stars",
            "Bronze": "128 stars",
            "Silver": "512 stars",
            "Gold": "4096 stars"
        },
        "tips": [
            "Create high-quality, useful projects.",
            "Write a clear and attractive README.",
            "Share your project on social media or developer communities.",
            "Add relevant tags/topics to your repository."
        ]
    },
    "galaxy-brain": {
        "name": "Galaxy Brain",
        "description": "Have your answers marked as accepted in GitHub Discussions.",
        "tiers": {
            "Default": "2 accepted answers",
            "Bronze": "8 accepted answers",
            "Silver": "16 accepted answers",
            "Gold": "32 accepted answers"
        },
        "tips": [
            "Find repositories with Discussions enabled.",
            "Provide helpful, accurate, and well-formatted answers.",
            "Focus on active communities where people ask questions regularly.",
            "Note: Discussions in the 'GitHub Community' repo usually don't count towards this badge."
        ]
    },
    "heart-on-your-sleeve": {
        "name": "Heart On Your Sleeve",
        "description": "React to issues, pull requests, or comments with the ❤️ emoji.",
        "tiers": {
            "Default": "Often reported around 1-2 reactions",
            "Note": "Precise numbers for higher tiers are not publicly released by GitHub."
        },
        "tips": [
            "Be active in the community.",
            "Show appreciation for others' work by using the heart reaction.",
            "This badge is often considered 'in testing' or 'hidden', so consistent activity is key."
        ]
    },
    "open-sourcerer": {
        "name": "Open Sourcerer",
        "description": "Contribute to multiple public repositories.",
        "tiers": {
            "Default": "Contribution to a public repo (Merged PR)",
            "Note": "Precise numbers for tiers and exact repo count requirements are not fully public."
        },
        "tips": [
            "Make pull requests to various open-source projects.",
            "Focus on quality contributions rather than just volume.",
            "It generally involves having merged PRs across different public repositories."
        ]
    }
}

def display_badge(badge_key):
    badge = BADGES.get(badge_key.lower())
    if not badge:
        # Try to match by replacing hyphens with spaces or vice versa
        normalized_key = badge_key.lower().replace(" ", "-")
        badge = BADGES.get(normalized_key)

    if not badge:
        print(f"Error: Badge '{badge_key}' not found.")
        return

    print(f"\n{'='*40}")
    print(f"Badge: {badge['name']}")
    print(f"{'='*40}")
    print(f"Description: {badge['description']}")
    print("\nTiers:")
    for tier, req in badge['tiers'].items():
        print(f"  - {tier}: {req}")
    print("\nTips for Unlocking:")
    for tip in badge['tips']:
        print(f"  * {tip}")
    print(f"{'='*40}\n")

def main():
    parser = argparse.ArgumentParser(description="GitHub Achievement Badge Info Tool")
    parser.add_argument("badge", nargs="?", help="The name of the badge to look up (e.g., starstruck, galaxy-brain, heart-on-your-sleeve, open-sourcerer)")
    parser.add_argument("--list", action="store_true", help="List all available badges")

    args = parser.parse_args()

    if args.list:
        print("Available Badges:")
        for key in BADGES:
            print(f"  - {key}")
        return

    if args.badge:
        display_badge(args.badge)
    else:
        parser.print_help()
        print("\nExample usage:")
        print("  python badge_info.py starstruck")
        print("  python badge_info.py --list")

if __name__ == "__main__":
    main()
