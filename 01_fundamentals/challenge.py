# ==========================================
#  Student Profile Generator
# ==========================================

# 1. Inputs / Variables (Deliberately storing age as string to practice type conversion)
full_name = "   Muhammad Hassan   "
age_input = "21"
city = "rawalpindi"
course = "Python Core"
current_year = 2026
study_year = 1

# 2. String Manipulation & Cleaning
clean_name = full_name.strip()
clean_city = city.strip().title()

# Username generation: lowercase, replace spaces with underscores
username = clean_name.lower().replace(" ", "_")

#Type Conversion
age = int(age_input)

birth_year = int(current_year-age)

if age>18 :
    is_adult=True


# 5. Formatted Output Display
print("=" * 36)
print("       STUDENT PROFILE")
print("=" * 36)
print(f"Name:       {clean_name}")
print(f"Age:        {age} (Born: ~{birth_year})")
print(f"Adult:      {is_adult}")
print(f"City:       {clean_city}")
print(f"Course:     {course}")
print(f"Year:       {study_year}")
print("-" * 36)
print(f"Username:   {username}")
print("=" * 36)