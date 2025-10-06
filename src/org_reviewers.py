def count_senior(root, min_level):
    """
    Return how many people in the org tree have level >= min_level.

    Node format:
      {
        "name": str,
        "level": int,
        "reports": [nodes]
      }

    Args:
        root (dict | None): root of the org tree
        min_level (int): minimum level threshold

    Returns:
        int: count of people with level >= min_level
    """
    # Base case: empty or invalid node
    if not isinstance(root, dict):
        return 0

    # Self contribution: 1 if this person's level qualifies
    level = root.get("level", 0)
    count = 1 if level >= min_level else 0

    # Recursive step: sum over all direct reports
    reports = root.get("reports", [])
    for report in reports:
        count += count_senior(report, min_level)

    return count
