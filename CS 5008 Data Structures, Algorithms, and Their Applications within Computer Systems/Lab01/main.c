// Hang Zhao
// Date:1/19/2024
//
#include <stdio.h>

// Function to calculate power
double power(double base, double n)
{
    double result = 1.0;
    for (int i = 0; i < n; i++)
    {
        result *= base;
    }
    return result;
}

int main()
{
    // Loop to compute and print power(2, 1) to power(2, 10)
    for (int i = 1; i <= 10; i++)
    {
        double result = power(2.0, (double)i);
        printf("power(2, %d) = %.2f\n", i, result);
    }

    return 0;
}

