#include <stdio.h>
#include <stdbool.h>
#include <math.h>

// int main()
// {
//     ESEMPIO VARIABILI
//     int eta = 25;  //inizializzazione
//     int etaNonna;  //dichiarazione
//     etaNonna = 80; // assegnazione
//     printf("%d", eta);
    


   
//     return 0; 
// }


// int main()
// {
//     //ESEMPIO COSTANTI
   
//     const int ETA_NONNA = 30; //per dire che  è una costante si scrive in maiuscolo solitamente, è una regola non scritta.
//     eta = 30;

//     printf("ciao ho %d anni", ETA_NONNA);

   
//     return 0; 
// }



// int main()
// {
//     //
   
//     const int ETA_NONNA = 30; //per dire che  è una costante si scrive in maiuscolo solitamente, è una regola non scritta.
//     int eta_nonna = 30; //%d
//     double eta_nonna = 100.23; //%f
//     char carattere = 'A';   //%c
//     bool isOnline = true;
//     int* pointer =
    
//     // short, long , long long = va in base a quanto è grande il numero piu è grande quindi prima short poi long poi long long,
//     // (int = 4 byte, short = 2byte, long = 4byte, long long = 8byte )

//     // float , double , long double = si usa con i numeri con la virgola in base a quante cifre con la virgola sono si userà
//     // prima float poi double poi long double( si usa sempre double per andare sul sicuro)

//     // char = è un carattere si usano gli apici singoli e non i doppi apici

//     // booleano è o true o false o vero o falso

//     printf("ciao ho %d anni", ETA_NONNA);

   
//     return 0; 
// }



    // int main()
    // {       //CASTING
    //     double x = 30.12312;
    //     int y = (int)x;

    //     printf("ciao ho %d anni", (int)x);

    //     return 0;
    // }



    // int main()
    // {

    //     int x = 30 / 5; 
        
    //     //facendo questa cosa il risultato sarà 6 con resto 0 ma se è 31 / 5? prenderà sempre 6 perchè prende l'intero dato
    //     // che è int, come faccio a far prendere anche il resto? usando % al posto di / ma prenderà poi solo il resto e non l'intero del numero

    //     int x = 11;

    //     x++;
    //     x--;

         // in questo caso il ++ vedendo il valore int x = 11 il risultato verra 12, mentre con -- vedendo come esempio int x = 11 il risultato
         // verra 10

    //         esempio:

    //         int x = 11;
    //         int y = ++x;
  
    //     printf("%d"\n, x);
    //         print("%d", y);
        //in questo caso il risultato sarà 12 12, perchè? perchè il ++ è messo prima della x invece che dopo come nell'esempio prima.
         // se fosse stato x++ invece il risualtato sarebbe stato 12 11.

    // //     return 0;
    // }



    // int main()
    // {
    //     int x = 11;
    //     int y = 20;
    //     bool condizione = x < y;

    //     //  quando si usa bool e il risultato nel terminale vieni 1 vuol dire che è vero, se invece viene 0 il risultato sara allora falso
    //     // nel caso in cui si volesse usare 10 = 10 verebbe errore questo perchè c'è gia un = in precendenza quindi si usa ==
    //     // != significa diverso uguale

    //     printf("%d", condizione);

    // }



        int main()
    {
        int x = 11;
        int y = 20;
        bool condizione = x > 5  || x < 20;

        //la doppia && si usa per definire AND(anche o e), se ci fosse stato solo x e non y con numero x=21 verrebbe falso ossia 0 perchè le condizoni devono essere uguali, 
        // or = oppure, ed è || qui se hai una delle due opzioni vere il risultato verra vero ossia 1.
        // not = è il ! ossia verrà il contrario del risultato che dovrebbe essere

        int x =100;
        bool condizione = (x % 2 == 0 && x < 200) || (x % 2 == 1 && x > 1000);

        
        printf("%d", condizione);

    }