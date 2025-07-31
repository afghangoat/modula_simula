#include "cpp_simula_bridge.hpp"
int main() Begin
    Class Person Begin public:

            Text name;
            Integer age;

            Procedure print()
                Begin
                    OutText("Name: ");
					OutText(name);
					OutImage();
                    OutText("Age: ");
					OutInt(age,0);
					OutImage();
                End;
        End;

    Person p;
    p.name = "Alice";
    p.age = 25;
    Call p.print();
	
	

    OutText ("Hello, World!");
    OutImage();
	
	If 2==2 Then
		OutText("Wow");
	Else
		
		OutText("Not Wow");
	End;
End;
