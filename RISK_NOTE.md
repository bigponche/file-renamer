# Risk Note — BMI Calculator

## Known limitations

### 1. No data persistence
The program does not save the data obtained from the BMI calculation in any file or database. All results are lost once the program closes.

### 2. No upper range validation
The program validates that weight and height are not negative or zero, but does not check for unrealistic values. Entering data like 1000 kg or 11000 cm will run without errors, but the result is not meaningful in real life.

### 3. Muscle mass is not considered
The BMI formula only uses weight and height. It does not account for body composition, so a person with a high muscle mass and low body fat may be incorrectly classified as overweight or obese.