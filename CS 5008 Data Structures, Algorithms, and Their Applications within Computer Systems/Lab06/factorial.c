// Hang Zhao
// 2/23/2024
//
// gcc -Wall factorial.c -o factorial
// ./factorial

#include <stdio.h>

int factorial(int n)
{
  // TODO: Implement iterative solution here
  int result = 1;
  for (int i = 1; i <= n; i++)
  {
    result *= i;
  }
  return result;
};

int factorial_rec(int n)
{
  // TODO: Implement recursive solution here
  if(1 == n){
    return 1;
  } else {
    return n * factorial_rec(n-1);
  }
}

int main(){

  // Both of these should print the same result!
  printf("factorial(31) = %d\n", factorial(31));
  printf("factorial_recursion(31) = %d\n", factorial_rec(31));

  return 0;
}
