#include <stdio.h>

int cd=0,ca=0;
void bd(int array[], int placementlelo) {
  for (int step = 0; step < placementlelo - 1; ++step) {
    for (int i = 0; i < placementlelo - step - 1; ++i) {
      if (array[i] < array[i + 1]) {
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
        cd++;
      }
    }
  }
}

void ba(int array[], int placementlelo) {
  for (int step = 0; step < placementlelo - 1; ++step) {
    for (int i = 0; i < placementlelo - step - 1; ++i) {
      if (array[i] > array[i + 1]) {
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
        ca++;
      }
    }
  }
}

int main() {
    int placementlelo;
    scanf("%d",&placementlelo);
    int da[placementlelo],dd[placementlelo];
    for(int i=0;i<placementlelo;i++){
        scanf("%d",&da[i]);
        dd[i]=da[i];
    }
  bd(da, placementlelo);
  ba(dd, placementlelo);
  if(cd>ca)
  printf("%d",ca);
  else
  printf("%d",cd);
}