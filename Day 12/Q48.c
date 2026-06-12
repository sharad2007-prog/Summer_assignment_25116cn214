#include <stdio.h>

// Function to check perfect number
int isPerfect(int num)
{
    int sum = 0;

    // Find sum of proper divisors
    for(int i = 1; i < num; i++)
    {
        if(num % i == 0)
            sum += i;
    }

    return (sum == num);
}

int main()
{
    int n;

    printf("Enter a number: ");
    scanf("%d", &n);

    if(isPerfect(n))
        printf("Perfect Number");
    else
        printf("Not a Perfect Number");

    return 0;
}
