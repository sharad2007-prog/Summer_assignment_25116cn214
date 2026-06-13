#include <stdio.h>

int main()
{
    int n, even = 0, odd = 0;

    printf("Enter array size: ");
    scanf("%d", &n);

    int arr[n];

    for(int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    // Count even and odd elements
    for(int i = 0; i < n; i++)
    {
        if(arr[i] % 2 == 0)
            even++;
        else
            odd++;
    }

    printf("Even Elements = %d\n", even);
    printf("Odd Elements = %d", odd);

    return 0;
}
