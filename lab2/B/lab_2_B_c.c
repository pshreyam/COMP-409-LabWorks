/* Definitions */
%{
	#include <stdio.h>
    int words_count = 0;
    int characters_count = 0;
    int blank_spaces_count = 0;
    int lines_count = 0;
    extern FILE *yyin, *yout;
%}

/* Rules */
%%
[\n] { lines_count++; characters_count+=yyleng;}
[  \t] { blank_spaces_count++; characters_count+=yyleng;}
[^\t\n ]+ { words_count++;  characters_count+=yyleng;}
%%

/* User subroutines */
int yywrap(){}

int main() {
    yyin = fopen("code.txt", "r");
    yylex();
	printf("Number of words = %d\n", words_count);
	printf("Number of characters = %d\n", characters_count);
	printf("Number of blank spaces = %d\n", blank_spaces_count);
	printf("Number of lines = %d\n", lines_count);
    return 0;
}
