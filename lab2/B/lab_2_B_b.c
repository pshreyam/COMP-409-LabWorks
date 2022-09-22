/* Definitions */
%{
	#include <stdio.h>
    int positive_numbers_count = 0;
    int negative_numbers_count = 0;
    int positive_float_count = 0;
    int negative_float_count = 0;
    extern FILE *yyin, *yout;
%}

/* Rules */
x[0-9]
%%
\+?{x}+    {positive_numbers_count++;}
-{x}+      {negative_numbers_count++;}

\+?{x}*\.{x}+   {positive_float_count++;}
-{x}*\.{x}+     {negative_float_count++;}
. ;
%%

/* User subroutines */
int yywrap(){}

int main() {
    yyin = fopen("code.txt", "r");
    yylex();
	printf("Number of positive integer numbers = %d\n", positive_numbers_count);
	printf("Number of negative integer numbers = %d\n", negative_numbers_count);
	printf("Number of positive float numbers = %d\n", positive_float_count);
	printf("Number of negative float numbers = %d\n", negative_float_count);
    return 0;
}
