#include <stdio.h>
#include<math.h>

int main(){
	long long int num;
	scanf("%d",&num);
	 int  arr[num];             			// Reading input from STDIN
	long long int i;
	long long int var=1;
	int pow1=pow(10,9);
	for(i=0;i<num;i++)
	{
		scanf("%d",&arr[i]);
		
		var=(var*arr[i])%(pow1+7);

	}
	printf("%d",var);
	
	     // Writing output to STDOUT
}
