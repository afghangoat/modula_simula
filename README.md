# Simula-Modula-2 to C++ transpiler

Or in short: **S.M.2.T.C.T** Is a quick Simula and Modula 2 interpreter. By the time of making, this is the only public software which can interpret Simula or Modula 2.
The repository contains examples for the usage of both languages, so far, these are the supported features:

## Simula keywords

Keywords:
- Begin
- End
- Call
- Class
- Procedure
- Ref(T)
- New(T)
- :=
- :-
- If
- Then
- ElseIf
- EndIf
- Do
- Until
- Step
- Starts
- For
- While

Types:
- Text
- Integer
- Array

Build-in:
- OutText
- OutInt
- OutImage

## Simula changes

Array starts at 0. I dont care about breaking compat. I hate to start at 1.

## Modula 2 keywords

Keywords:
- BEGIN
- END
- PROCEDURE
- CALL
- CLASS

Data types:
- CARDINAL
- BITSET

## Requirements

The following dependencies are required for the transpiler:

- Python 3
- C++ compiler (C++17 or above)

## Usage

Run:
`python simula_replace.py <filename>.sim/mi`
Running it will generate a compileable and a runnable c++ file.