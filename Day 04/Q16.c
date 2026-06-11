#include <stdio.h>
#include <math.h>

int main()
{
    int start, end;

    printf("Enter range: ");
    scanf("%d%d", &start, &end);

    for(int num = start; num <= end; num++)
    {
        int temp = num;
        int count = 0, sum = 0, digit;

        while(temp != 0)
        {
            count++;
            temp /= 10;
        }

        temp = num;

        while(temp != 0)
        {
            digit = temp % 10;
            sum += pow(digit, count);
            temp /= 10;
        }

        if(sum == num)
            printf("%d ", num);
    }

    return 0;
}
