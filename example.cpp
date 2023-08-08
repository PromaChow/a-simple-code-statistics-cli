#include <iostream>

// Function with a for loop
int factorial(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

// Function with if-else statements
void checkNumber(int num) {
    if (num > 0) {
        std::cout << "Positive number" << std::endl;
    } else if (num < 0) {
        std::cout << "Negative number" << std::endl;
    } else {
        std::cout << "Zero" << std::endl;
    }
}

// Function with a switch statement
void printDayOfWeek(int day) {
    switch (day) {
        case 1:
            std::cout << "Monday" << std::endl;
            break;
        case 2:
            std::cout << "Tuesday" << std::endl;
            break;
        case 3:
            std::cout << "Wednesday" << std::endl;
            break;
        case 4:
            std::cout << "Thursday" << std::endl;
            break;
        case 5:
            std::cout << "Friday" << std::endl;
            break;
        case 6:
            std::cout << "Saturday" << std::endl;
            break;
        case 7:
            std::cout << "Sunday" << std::endl;
            break;
        default:
            std::cout << "Invalid day" << std::endl;
            break;
    }
}

// Main function
int main() {
    int num = 5;
    int result = factorial(num);
    std::cout << "Factorial of " << num << " is: " << result << std::endl;

    checkNumber(-10);
    checkNumber(0);
    checkNumber(42);

    printDayOfWeek(2);
    printDayOfWeek(7);
    printDayOfWeek(9);

    return 0;
}
