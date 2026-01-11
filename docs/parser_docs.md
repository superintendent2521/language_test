# Parser Documentation

## Overview

This parser is designed for a simple arithmetic language that uses English words for operations. It tokenizes input strings and converts them into executable operations.

## Token Types

- **NUMBER**: Integer values
- **OPERATOR**: Mathematical operations (+, -, *, /)

## Supported Operations

The parser supports the following operations:
- **PLUS**: Addition (+)
- **SUBTRACT**: Subtraction (-)
- **MULTIPLY**: Multiplication (*)
- **DIVIDE**: Division (/)

## Code Structure

### Token Class

A dataclass representing tokens in the language:
- : The type of token (NUMBER, OPERATOR)
- : The value associated with the token (integer for numbers, string for operators)
