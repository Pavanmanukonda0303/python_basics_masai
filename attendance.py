# Sample input (already filled in for you)
scans = ["S104", "S221", "S104", "S387", "S221", "S150", "S104"]


def attendance_summary(scans):
    unique_badges = sorted(set(scans))
    return {
        "total_scans": len(scans),
        "unique_count": len(unique_badges),
        "repeat_scans": len(scans) - len(unique_badges),
        "present": unique_badges,
    }


# Print harness (already filled in for you)
summary = attendance_summary(scans)
print("Total scans:", summary["total_scans"])
print("Unique learners:", summary["unique_count"])
print("Repeat scans:", summary["repeat_scans"])
print("Present:", summary["present"])
for badge in summary["present"]:
    print("-", badge)