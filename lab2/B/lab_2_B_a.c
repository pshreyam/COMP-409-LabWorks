/* Definitions */
%{
	#include <stdio.h>
	int vowel_count = 0;
    int consonant_count = 0;
    extern FILE *yyin, *yout;
%}

/* Rules */
/* if character belongs to vowel, increment vowel count by 1 */
/* if character belongs to consonant (does not belong to vowel), increment consonant count by 1 */

%%
[ \t\n]+    ;
[aeiouAEIOU]+    {vowel_count++;}
[^aeiouAEIOU]     {consonant_count++;}
%%

/* User subroutines */
int yywrap(){}

int main() {
    yyin = fopen("code.txt", "r");
    yylex();
	printf("Number of vowels = %d\n", vowel_count);
	printf("Number of consonants = %d\n", consonant_count);
    return 0;
}
