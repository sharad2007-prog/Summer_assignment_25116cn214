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

        // Ascending characters
        for(char ch = 'A'; ch < 'A' + i; ch++)
            printf("%c", ch);

        // Descending characters
        for(char ch = 'A' + i - 2; ch >= 'A'; ch--)
            printf("%c", ch);

        printf("\n");
    }

    return 0;
}
