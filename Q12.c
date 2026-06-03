#include <stdio.h>

int main() {
    int num1, num2, max;

    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);

    // Start checking from the greater number
    max = (num1 > num2) ? num1 : num2;

    while (1) {
        // If max is divisible by both numbers, it is the LCM
        if (max % num1 == 0 && max % num2 == 0) {
            printf("LCM of %d and %d = %d\n", num1, num2, max);
            break;
        }
        max++;
    }

    return 0;
}