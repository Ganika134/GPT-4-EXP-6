
def print_heading(title):
    print("\n" + "=" * 45)
    print(title)
    print("=" * 45)


def format_profile(profile):
    return "\n".join(
        f"{key}: {value}" for key, value in profile.items()
    )
