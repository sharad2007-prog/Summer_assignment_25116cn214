#include <stdio.h>

// Function to check palindrome
int isPalindrome(int num)
{
    int rev = 0, temp = num;

    while(temp != 0)
    {
        rev = rev * 10 + temp % 10;
        temp /= 10;
    }

    return (rev == num);
}

int main()
{
    int n;

    printf("Enter a number: ");
    scanf("%d", &n);

    if(isPalindrome(n))
        printf("Palindrome Number");
    else
        printf("Not a Palindrome Number");

    return 0;
}
