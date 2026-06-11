#include <stdio.h>

int main()
{
    int rows;

    printf("Enter number of rows: ");
    scanf("%d", &rows);

    for(int i = 1; i <= rows; i++)
    {
        // Print spaces
        for(int j = 1; j <= rows - i; j++)
            printf(" ");

        // Ascending numbers
        for(int j = 1; j <= i; j++)
            printf("%d", j);

        // Descending numbers
        for(int j = i - 1; j >= 1; j--)
            printf("%d", j);

        printf("\n");
    }

    return 0;
}
