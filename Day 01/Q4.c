#include <stdio.h>

int main()
{
    int n, count = 0;

    printf("Enter a number: ");
    scanf("%d", &n);

    // Count digits
    while(n != 0)
    {
        count++;
        n /= 10;
    }

    printf("Total Digits = %d", count);

    return 0;
}
