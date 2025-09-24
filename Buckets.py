from word2number import w2n

def get_number(prompt, allow_zero=True, positive_only=False):
    while True:
        try:
            user_input = input(prompt).strip()
            try:
                num = int(user_input)
            except ValueError:
                num = w2n.word_to_num(user_input)

            if positive_only and num < 0:
                print("❌ Negative number not allowed! Please enter again.")
                continue
            if not allow_zero and num == 0:
                print("❌ Zero not allowed here! Please enter again.")
                continue

            return num
        except:
            print("❌ Invalid input! Please enter a valid number or number in words.")

# Get number of buckets
num_buckets = get_number("Enter the number of buckets: ", allow_zero=False, positive_only=True)

if num_buckets == 0:
    print("⚠ No buckets available. Program will exit.")
    exit()

bucket_sizes = []
water_levels = []

# Get bucket sizes
for i in range(num_buckets):
    size = get_number(f"Enter size of bucket {i+1}: ", allow_zero=False, positive_only=True)
    bucket_sizes.append(size)

# Get water levels with validation
for i in range(num_buckets):
    while True:
        water = get_number(f"Enter water level of bucket {i+1}: ", allow_zero=True, positive_only=True)
        if bucket_sizes[i] == 0 and water > 0:
            print(f"❌ Bucket {i+1} has size 0 but water level > 0! Enter again.")
            continue
        water_levels.append(water)
        break

# Processing
full_buckets = []
empty_buckets = []
partial_buckets = []
remaining_capacity = []
extra_water_distribution = {}
redistribution_log = {f"Bucket {i+1}": 0 for i in range(num_buckets)}  # Track added water

# Step 1: Check for extra water
for i in range(num_buckets):
    if water_levels[i] > bucket_sizes[i]:
        extra = water_levels[i] - bucket_sizes[i]
        extra_water_distribution[f"Bucket {i+1}"] = extra
        water_levels[i] = bucket_sizes[i]  # Cap it to max size

        # Step 2: Redistribute extra water to other buckets
        for j in range(num_buckets):
            if i != j and water_levels[j] < bucket_sizes[j] and extra > 0:
                available_space = bucket_sizes[j] - water_levels[j]
                transfer = min(extra, available_space)
                water_levels[j] += transfer
                redistribution_log[f"Bucket {j+1}"] += transfer
                extra -= transfer

# Step 3: Classify buckets after redistribution
for i in range(num_buckets):
    if water_levels[i] == bucket_sizes[i]:
        full_buckets.append(i+1)
        remaining_capacity.append(0)
    elif water_levels[i] == 0:
        empty_buckets.append(i+1)
        remaining_capacity.append(bucket_sizes[i])
    else:
        partial_buckets.append(i+1)
        remaining_capacity.append(bucket_sizes[i] - water_levels[i])

# Output
print("/n___Summary___")
print(f"Full buckets: {full_buckets}")
print(f"Empty buckets: {empty_buckets}")
print(f"Partially filled buckets: {partial_buckets}")
print(f"Remaining capacity in each bucket: {remaining_capacity}")

if extra_water_distribution:
    print("/n___Initial extra water (before redistribution):___")
    for bucket, extra in extra_water_distribution.items():
        print(f"{bucket}: {extra} litres")

print("/n___Redistribution result (extra water added to each bucket):___")
for bucket, added in redistribution_log.items():
    if added > 0:
        print(f"{bucket}: {added} litres")

# ✅ Final water levels after all redistribution
print("<___Final water level in each bucket:___>")
for i in range(num_buckets):
    print(f"Bucket {i+1}: {water_levels[i]} litres")
