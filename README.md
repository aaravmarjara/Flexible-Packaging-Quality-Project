# Flexible Packaging Quality Project

## About the Project

This is a beginner-level Python project developed to explore how programming can be applied to real-world manufacturing operations.

The idea came from observing the repetitive process of collecting production data and entering it into Excel at my family's flexible packaging manufacturing business.

## What Does It Do?

The program collects production information for three batches, including:

- Total production (kg)
- Waste generated (kg)
- Material type (LDPE, HDPE or BOPP)

It then:

- Calculates good production and waste percentages.
- Generates an overall production summary.
- Identifies batches with the highest and lowest waste percentages.
- Compares waste rates across different materials.
- Calculates production and waste totals for each material.
- Exports the results into a CSV file that can be opened in Microsoft Excel.

## Technologies Used

- Python
- CSV module
- Microsoft Excel (for viewing exported reports)

## What I Learned

Through this project, I applied Python concepts such as:

- Variables and data types
- Loops
- Conditional statements
- Lists
- Basic calculations
- File handling and CSV export
- Debugging

## Current Limitations

- The program currently accepts only three production batches per run.
- It is a prototype and has not yet been implemented in the factory.
- The report is overwritten each time the program runs.

## Future Improvements

- Allow users to enter any number of production batches.
- Preserve historical production records.
- Improve material-wise comparisons across multiple batches.
- Make the program easier for factory employees to use.

## Motivation

I built this project to apply my newly acquired Python skills to a practical problem I observed in my family's manufacturing business, and to explore how technology could help improve business operations.
## Project Screenshots

### Program Output
![Program Output](screenshots/program_output.png)

### Excel Report
![Excel Report](screenshots/excel_report.png)
