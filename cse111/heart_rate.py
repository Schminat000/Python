"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

user_age = int(input("What is the age? "))
heart_rate = int(220 - user_age)
lower_beat = int(heart_rate * 0.65)
high_beat = int(heart_rate * 0.85)
print(f"When you exercise to strengthen your heart, you should\n"
f"keep your heart rate between {lower_beat} and {high_beat} beats\n"
"per minute.")