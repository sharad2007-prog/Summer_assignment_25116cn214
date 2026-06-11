#include <stdio.h>

int main()
{
    long long n, largest = -1;

    printf("Enter a number: ");
    scanf("%lld", &n);

    // Remove factor 2
    while(n % 2 == 0)
    {
        largest = 2;
        n /= 2;
    }

    // Check odd factors
    for(long long i = 3; i * i <= n; i += 2)
    {
        while(n % i == 0)
        {
            largest = i;
            n /= i;
        }
    }

    if(n > 2)
        largest = n;

    printf("Largest Prime Factor = %lld", largest);

    return 0;
}
