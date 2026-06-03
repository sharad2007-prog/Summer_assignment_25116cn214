#include <stdio.h>

int main() {
    int num1, num2, gcd, i;

    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);

    // Find the smaller number
    int min = (num1 < num2) ? num1 : num2;

    // Check all factors up to min
    for (i = 1; i <= min; i++) {
        if (num1 % i == 0 && num2 % i == 0) {
            gcd = i;
        }
    }

    printf("GCD of %d and %d = %d\n", num1, num2, gcd);

    return 0;
}