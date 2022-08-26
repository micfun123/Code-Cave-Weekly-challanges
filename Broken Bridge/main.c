#include <stdio.h>
#include <string.h>

int main(){
    char sentance[150];
    char *s;
    printf("enter the bridge\n");
    fgets(sentance, 150, stdin);
    
    if (strchr (sentance,' ') == NULL){
        printf("There is no gap in the brige");
    }
    else{
        printf("There is a gap in the bridge");
    }
    
    return 0;
}