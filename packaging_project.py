
import csv

print("FLEXIBLE PACKAGING QUALITY PROJECT")
print("----------------------------------")

production_records = []

# Enter production details for three batches

for i in range(3):

    print("\nBatch", i + 1)

    total_production = float(input("Enter production in kg: "))
    waste = float(input("Enter waste in kg: "))

    if total_production <= 0 or waste < 0 or waste > total_production:
        print("Invalid production or waste value. Please enter again.")
        break

    material = input("Enter material type (LDPE/HDPE/BOPP): ")

    good_production = total_production - waste
    waste_percentage = (waste / total_production) * 100

    record = [total_production, waste, good_production, waste_percentage, material]

    production_records.append(record)

if len(production_records) == 0:
    print("No valid production records to report.")
    quit()

# Display production report

print("\nPRODUCTION REPORT")
print("-----------------")

for record in production_records:

    print("Production:", record[0], "kg")
    print("Waste:", record[1], "kg")
    print("Good production:", record[2], "kg")
    print("Waste percentage:", round(record[3], 2), "%")
    print("Material:", record[4])
    print("-----------------")

# Calculate overall production statistics

total_production = 0
total_waste = 0
total_good_production = 0

for record in production_records:

    total_production = total_production + record[0]
    total_waste = total_waste + record[1]
    total_good_production = total_good_production + record[2]

average_waste_percentage = (total_waste / total_production) * 100

print("\nOVERALL PRODUCTION SUMMARY")
print("--------------------------")

print("Total production:", total_production, "kg")
print("Total waste:", total_waste, "kg")
print("Total good production:", total_good_production, "kg")
print("Overall waste percentage:", round(average_waste_percentage, 2), "%")

# Evaluate production efficiency

if average_waste_percentage < 3:
    print("Production efficiency: Excellent")

elif average_waste_percentage <= 5:
    print("Production efficiency: Good")

else:
    print("Production efficiency: Needs Improvement")

# Find the batch with the highest and lowest waste percentage

highest_waste = production_records[0]
lowest_waste = production_records[0]

for record in production_records:

    if record[3] > highest_waste[3]:
        highest_waste = record

    if record[3] < lowest_waste[3]:
        lowest_waste = record

print("\nBATCH PERFORMANCE")
print("-----------------")

print("Highest waste batch:", round(highest_waste[3], 2), "%")
print("Lowest waste batch:", round(lowest_waste[3], 2), "%")

# Find the batch with the highest waste quantity

most_waste = production_records[0]

for record in production_records:

    if record[1] > most_waste[1]:
        most_waste = record

print("\nWASTE COMPARISON")
print("----------------")

print("Highest waste quantity:", most_waste[1], "kg")
print("Production of that batch:", most_waste[0], "kg")

# Save production records to a CSV file

with open("production_report.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Batch", "Production", "Waste", "Good Production", "Waste Percentage", "Material"])

    batch_number = 1

    for record in production_records:

        writer.writerow([batch_number] + record)

        batch_number = batch_number + 1

print("\nProduction records saved successfully!")

# Compare waste percentages for different materials

print("\nMATERIAL WASTE COMPARISON")
print("------------------------")

for record in production_records:
    print(record[4], ":", round(record[3], 2), "% waste")

highest_material_waste = production_records[0]

for record in production_records:

    if record[3] > highest_material_waste[3]:
        highest_material_waste = record

print("------------------------")
print("Highest waste material:", highest_material_waste[4])
print("Waste percentage:", round(highest_material_waste[3], 2), "%")

# Calculate production totals for each material

print("\nMATERIAL PRODUCTION SUMMARY")
print("---------------------------")

ldpe_total = 0
hdpe_total = 0
bopp_total = 0

for record in production_records:

    if record[4] == "LDPE":
        ldpe_total = ldpe_total + record[0]

    elif record[4] == "HDPE":
        hdpe_total = hdpe_total + record[0]

    elif record[4] == "BOPP":
        bopp_total = bopp_total + record[0]

print("Total LDPE production:", ldpe_total, "kg")
print("Total HDPE production:", hdpe_total, "kg")
print("Total BOPP production:", bopp_total, "kg")

# Calculate waste totals for each material

ldpe_waste = 0
hdpe_waste = 0
bopp_waste = 0

for record in production_records:

    if record[4] == "LDPE":
        ldpe_waste = ldpe_waste + record[1]

    elif record[4] == "HDPE":
        hdpe_waste = hdpe_waste + record[1]

    elif record[4] == "BOPP":
        bopp_waste = bopp_waste + record[1]

print("\nMATERIAL WASTE SUMMARY")
print("----------------------")

print("Total LDPE waste:", ldpe_waste, "kg")
print("Total HDPE waste:", hdpe_waste, "kg")
print("Total BOPP waste:", bopp_waste, "kg")

# Calculate waste percentage for each material

print("\nMATERIAL EFFICIENCY SUMMARY")
print("--------------------------")

if ldpe_total > 0:
    print("LDPE waste percentage:", round((ldpe_waste / ldpe_total) * 100, 2), "%")

if hdpe_total > 0:
    print("HDPE waste percentage:", round((hdpe_waste / hdpe_total) * 100, 2), "%")

if bopp_total > 0:
    print("BOPP waste percentage:", round((bopp_waste / bopp_total) * 100, 2), "%")

# Find the material with the lowest waste percentage

lowest_waste = 100
best_material = ""

if ldpe_total > 0:
    ldpe_percentage = (ldpe_waste / ldpe_total) * 100

    if ldpe_percentage < lowest_waste:
        lowest_waste = ldpe_percentage
        best_material = "LDPE"

if hdpe_total > 0:
    hdpe_percentage = (hdpe_waste / hdpe_total) * 100

    if hdpe_percentage < lowest_waste:
        lowest_waste = hdpe_percentage
        best_material = "HDPE"

if bopp_total > 0:
    bopp_percentage = (bopp_waste / bopp_total) * 100

    if bopp_percentage < lowest_waste:
        lowest_waste = bopp_percentage
        best_material = "BOPP"

print("\nBEST MATERIAL PERFORMANCE")
print("-------------------------")

if best_material != "":
    print("Lowest waste material:", best_material)
    print("Waste percentage:", round(lowest_waste, 2), "%")
else:
    print("No recognised material types were entered.")
