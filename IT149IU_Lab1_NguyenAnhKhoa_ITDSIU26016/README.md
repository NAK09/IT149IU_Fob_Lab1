# IT149IU Lab 1 Submission

## Student information

- **Name:** Nguyen Anh Khoa
- **Student ID:** ITDSIU26016
- **Course:** IT149IU
- **Lab:** Programming Fundamentals Lab 1

## Included files

- `IT149IU_Lab1_Report.docx` - the written lab report with goals, theory, objectives, step-by-step explanations, sample outputs, extended exercises, and scholar discussion.
- `IT149IU_Lab1_Completed.ipynb` - a completed Jupyter Notebook. All code cells contain deterministic examples and recorded outputs.
- `README.md` - this submission guide.
- `ex1.py` through `ex15.py` - the original Python exercise files.
- `bacteria_growth.csv` - the bacteria-growth table produced by Exercise 7.
- `course_grades.csv` - the course-grade table produced by Exercise 9.

## How to run the Python files

1. Install Python 3.10 or newer.
2. Install the data and plotting packages used by the lab:

   ```bash
   python -m pip install pandas matplotlib
   ```

3. Open a terminal in the folder containing the exercise files.
4. Run an exercise, for example:

   ```bash
   python ex6.py
   ```

5. Enter the values requested by the program. Exercises 6 and 11 open a Matplotlib chart. Exercises 7 and 9 write CSV files beside their scripts.

## How to open the notebook

Install Jupyter if it is not already available:

```bash
python -m pip install jupyter pandas matplotlib
jupyter notebook IT149IU_Lab1_Completed.ipynb
```

The notebook is already completed with executed cells and recorded sample outputs. Re-running it will reproduce the examples with the same deterministic inputs.

## Notes

- The original interactive scripts are preserved as submitted. They expect keyboard input and do not all validate invalid input.
- The notebook uses representative fixed inputs so that every cell can run from top to bottom without manual interaction.
- The growth model used in Exercises 6 and 7 is `B = 200 * 2**hour`.
- The grade and bacteria CSV files in this package match the supplied data files.
- For a full explanation of the lab, see `IT149IU_Lab1_Report.docx`.
