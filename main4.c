#include <stdio.h>

int main(){


        float base_menor, base_maior, altura;


        printf('Digite a base menor: ');
        scanf("%f", base_menor);
        printf('Digite a base maior: ');
        scanf("%f", &base_maior);
        printf("Digite a altura: ");
        scanf("%f", &altura);


        if (base_maior <= 0){
            printf("A base maior não pode ser menor que 0");
        }
        else if (base_menor <= 0){
            printf("A base menor não pode ser menor que 0");
        }
        else{

            float area_trapezio = ((base_maior + base_menor) * altura) / 2;
            printf("A area do trapezio %f", area_trapezio);
        };





    return 0;
}