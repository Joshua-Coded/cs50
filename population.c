#include <stdio.h>
#include <math.h>

int main(void)
{
  //prompt user for start size:
  int start_size;
  do
    {
      start_size = puts("Start size: ");
      scanf("%i", &start_size);
    }
  while ( start_size < 9 );

  // prompt user for End size:

  int end_size;
  do
    {
      end_size = puts("End size: ");
	 scanf("%i", &end_size);
      }
  while (end_size < start_size);

  int current_po = start_size;
  int year_passed = 0;

  while(current_po < end_size)
    {
      current_po = round(current_po + current_po/3 - current_po/4);
      year_passed++;
    }
  printf("years: %i", year_passed);

}
