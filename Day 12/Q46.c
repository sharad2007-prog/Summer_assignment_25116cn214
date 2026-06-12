#include <stdio.h>
#include <math.h>

// Function to check Armstrong number
int isArmstrong(int num)
{
    int temp = num;
    int digits = 0;
    int sum = 0, rem;

    // Count digits
    while(temp != 0)
    {
        digits++;
        temp /= 10;
    }

    temp = num;

    // Calculate Armstrong sum
    while(temp != 0)
    {
        rem = temp % 10;
        sum += pow(rem, digits);
        temp /= 10;
    }

    return (sum == num);
}

int main()
{
    int n;

    printf("Enter a number: ");
    scanf("%d", &n);

    if(isArmstrong(n))
        printf("Armstrong Number");
    else
        printf("Not an Armstrong Number");

    return 0;
}
