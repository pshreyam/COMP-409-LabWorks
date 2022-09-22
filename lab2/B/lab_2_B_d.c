/* Definitions */
%{
    #include <stdio.h>
    #include <string.h>
    int flag = 0, i = 0, j = 0, k = 0;
    char operand[20][20], operator[20][20];
%}

/* Rules */
%%
[a-zA-Z0-9]+  {flag++; strcpy(operand[i], yytext); i++;}
[-+*/]	{flag--; strcpy(operator[k], yytext); k++;}
%%

/* User subroutines */
int yywrap(){}

int main() {
    printf("Enter an expression (Press Ctrl + D to stop input): ");
	yylex();
	
	if (flag != 1) {
		printf("The expression is invalid.\n");
    }
	else {
		printf("The expression is valid.\n");
	}
    return 0;
}
