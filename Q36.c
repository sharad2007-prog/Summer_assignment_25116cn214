#include <stdio.h>

int main() {
    int i, j;
    int n = 5;  // Size of the square

    // Outer loop for rows
    for(i = 1; i <= n; i++) {

        // Inner loop for columns
        for(j = 1; j <= n; j++) {

            // Print '*' on borders, otherwise print space
            if(i == 1 || i == n || j == 1 || j == n)
                printf("*");
            else
                printf(" ");
        }

        // Move to the next line after each row
        printf("\n");
    }

    return 0;
}