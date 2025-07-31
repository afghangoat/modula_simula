#ifndef SIMULA_BRIDGE
	//Simula - 2025
	/*Changes:
	Array starts at 0. I dont care about breaking compat. I hate to start at 1.
	
	Also can run somewhat MODULA-2 compilant code snippets. Not perfect, but nothing is
	*/
	
	#define	SIMULA_BRIDGE
	
	#include <iostream>
	#include <string>
	#include <iomanip>
	
	using Text = std::string;
	using Integer = int;
	
	inline void OutText(const Text& t){
		std::cout << t;
	}
	inline void OutInt(Integer val, int width) {
		std::cout << std::setprecision(width) << std::setw(width) << std::setfill(' ') << val;
	}

	inline void OutImage() {
		std::cout << std::endl;
	}
	
	#define Begin {
	#define End }
	#define Procedure void
	#define Call
	#define Class class
	#define BEGIN {
	#define END }
	#define PROCEDURE void
	#define CALL
	#define CLASS class
	#define CARDINAL unsigned int
	#define BITSET [32]
	
	#define Ref(T) T*
	#define New(T) new T
	
	#define New new
	
	#define If if(
	#define Then ) {
	#define Else } else {
	#define ElseIf } else if(
	#define EndIf }
	#define Do ) {
	#define Until ,
	#define Step ,
	#define Starts ,
	#define For(var,from,to,step) for (int var = from; var <=to;var+=step
	//Example For( i Starts 1 Until 10 Step 1) Do
	
	#define While while (
	
	// Integer Arr[1:10]
	// Arr[1] =42
#endif